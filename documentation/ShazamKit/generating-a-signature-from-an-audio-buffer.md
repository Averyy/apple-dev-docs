# Generating a signature from an audio buffer

**Framework**: ShazamKit

Create a signature from an audio file or the microphone for a reference track in a custom catalog, or for matching tracks in a catalog.

#### Overview

Generate a signature by adding an audio buffer in a supported format to an [`SHSignatureGenerator`](shsignaturegenerator.md) object. You can add the audio buffer in one call or incrementally.

The most common sources for audio are files in the app or the microphone.

##### Create a Signature From an Audio File

Creating a signature from an audio file takes four steps:

1. Create an object for reading the audio file.
2. Convert the audio to a supported format. For a list of supported formats, see [`append(_:at:)`](shsignaturegenerator/append(_:at:).md).
3. Append the converted audio to a signature generator.
4. Generate the signature.

The following demonstrates how to generate the signature from the audio file:

```swift
// Return the signature of an audio file.
func generateSignature(from audioURL: URL) -> SHSignature? {
    // Step 1.
    // Create an audio format that's compatible with ShazamKit.
    guard let audioFormat = AVAudioFormat(standardFormatWithSampleRate: 44100, channels: 1) else {
        // Handle an error in creating the audio format.
        return nil
    }

    // Create a signature generator to generate the final signature.
    let signatureGenerator = SHSignatureGenerator()
    
    do {
        // Create an object for reading the audio file.
        let audioFile = try AVAudioFile(forReading: audioURL)

        // Step 2.
        // Convert the audio to a supported format.
        CustomCatalog.convert(audioFile: audioFile, outputFormat: audioFormat) { buffer in
            do {
                // Step 3.
                // Append portions of the converted audio to the signature generator.
                try signatureGenerator.append(buffer, at: nil)
            } catch {
                // Handle an error generating the signature.
                return
            }
        }
    } catch {
        // Handle an error reading the audio file.
        return nil
    }

    // Step 4.
    // Generate the signature.
    return signatureGenerator.signature()
}
```

The convert function has two main parts. First it configures the buffers used for the conversion and the format for the converted audio:

```swift
// Convert an audio file to a new format one chunk at a time.
static func convert(audioFile: AVAudioFile,
                    outputFormat: AVAudioFormat,
                    processConvertedBlock: (AVAudioPCMBuffer) -> Void) {
    // Set the size of the conversion buffer.
    let frameCount = AVAudioFrameCount(
        (1024 * 64) / (audioFile.processingFormat.streamDescription.pointee.mBytesPerFrame)
    )
    // Calculate the number of frames for the output buffer.
    let outputFrameCapacity = AVAudioFrameCount(
         round(Double(frameCount) * (outputFormat.sampleRate / audioFile.processingFormat.sampleRate))
    )

    // Create the input and output buffers for converting the file.
    guard let inputBuffer = AVAudioPCMBuffer(pcmFormat: audioFile.processingFormat, frameCapacity: frameCount),
          let outputBuffer = AVAudioPCMBuffer(pcmFormat: outputFormat, frameCapacity: outputFrameCapacity) else {
        return
    }

    // Create the format for the converter.
    guard let converter = AVAudioConverter(from: audioFile.processingFormat, to: outputFormat) else {
        return
    }
    
   // Code to convert the file goes here. See the next listing.
}
```

Then the convert function reads chunks of audio from the input file and calls the block passed by `generateSignature`. That block appends the converted audio to the signature.

```swift
    // Convert the audio file.
    while true {
    // Convert frames in the input buffer, writing them to the output buffer.
        let status = converter.convert(to: outputBuffer,
                                       error: nil) { inNumPackets, outStatus in
            do {
                // Read a frame from the audio file into the input buffer.
                try audioFile.read(into: inputBuffer)
                outStatus.pointee = .haveData
                return inputBuffer
            } catch {
                // Check if it's the end of the file or if an error occurred.
                if audioFile.framePosition >= audioFile.length {
                    outStatus.pointee = .endOfStream
                    return nil
                } else {
                    outStatus.pointee = .noDataNow
                    return nil
                }
            }
        }

        switch status {
        case .error:
            // An error occurred during conversion; handle the error.
            return

        case .endOfStream:
            // All of the input is converted.
            return

        case .inputRanDry:
            // Some data was converted, but no more is available.
            processConvertedBlock(outputBuffer)
            return

        default:
            processConvertedBlock(outputBuffer)
        }

        // Reset the size of the buffers.
        inputBuffer.frameLength = 0
        outputBuffer.frameLength = 0
    }

```

##### Create a Signature From the Microphone

Using the microphone as the source for generating a signature is very similar to using it for matching.

Configure a mixer as described in [`Matching audio using the built-in microphone`](matching-audio-using-the-built-in-microphone.md). Change the `addAudio` function to append the audio to the signature generator:

```swift
func addAudio(buffer: AVAudioPCMBuffer, audioTime: AVAudioTime) {
    do {
        // Add the audio to the signature generator.
        try signatureGenerator.append(buffer, at: audioTime)
    } catch {
        // Handle an error in appending audio to the generator.
    }
}
```

Start and stop the audio engine as needed using the `startListening` and `stopListening` functions shown in [`Matching audio using the built-in microphone`](matching-audio-using-the-built-in-microphone.md).

## See Also

- [func append(AVAudioPCMBuffer, at: AVAudioTime?) throws](shsignaturegenerator/append(_:at:).md)
  Adds audio to the generator.
- [func signature() -> SHSignature](shsignaturegenerator/signature.md)
  Converts the audio buffer into a signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/generating-a-signature-from-an-audio-buffer)*