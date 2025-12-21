# TN3136: AVAudioConverter - performing sample rate conversions

**Framework**: Technotes

Use AVAudioConverter to perform sample rate conversions between PCM audio buffers.

#### Overview

Using [`AVAudioConverter`](https://developer.apple.com/documentation/AVFAudio/AVAudioConverter) to perform sample rate conversions between PCM audio buffers requires making calls to [`convert(to:error:withInputFrom:)`](https://developer.apple.com/documentation/AVFAudio/AVAudioConverter/convert(to:error:withInputFrom:)). This method takes an instance of [`AVAudioBuffer`](https://developer.apple.com/documentation/AVFAudio/AVAudioBuffer), which stores the output of the conversion, as well as a closure that provides instances of [`AVAudioBuffer`](https://developer.apple.com/documentation/AVFAudio/AVAudioBuffer) to serve as input to the conversion.

> ❗ **Important**: The simpler method [`convert(to:from:)`](https://developer.apple.com/documentation/AVFAudio/AVAudioConverter/convert(to:from:)) does not require callbacks to convert between PCM audio buffers, but cannot handle sample rate conversions.

When converting between sample rates, the total number of input frames may be hard to predict. One way to cope with variable buffer sizes while providing input to [`AVAudioConverter`](https://developer.apple.com/documentation/AVFAudio/AVAudioConverter) is to fill the input buffers on a sample-by-sample basis. This tech note illustrates such a mechanism using a hypothetical [`SampleProvider`](https://developer.apple.com#Creating-a-protocol-for-providing-samples) protocol that generates one sample at a time.

The [`Resampler`](https://developer.apple.com#Creating-a-resampler) class gathers all of the components necessary for the conversion: the sample provider that conforms to [`SampleProvider`](https://developer.apple.com#Creating-a-protocol-for-providing-samples), the [`AVAudioConverter`](https://developer.apple.com/documentation/AVFAudio/AVAudioConverter) instance, and the source [`AVAudioPCMBuffer`](https://developer.apple.com/documentation/AVFAudio/AVAudioPCMBuffer) instance used in the call to [`convert(to:error:withInputFrom:)`](https://developer.apple.com/documentation/AVFAudio/AVAudioConverter/convert(to:error:withInputFrom:)). While the [`Resampler`](https://developer.apple.com#Creating-a-resampler) class is concerned with providing the output of the sample rate conversion, the [`SampleProvider`](https://developer.apple.com#Creating-a-protocol-for-providing-samples) implementation is concerned with providing the input.

#### Defining a Protocol for Providing Samples

The [`SampleProvider`](https://developer.apple.com#Creating-a-protocol-for-providing-samples) protocol is an example of how the [`Resampler`](https://developer.apple.com#Creating-a-resampler) class might interface with a provider class that produces audio samples. The protocol requires a single method to achieve this behavior, which returns the next sample in time.

The mechanism used by the conforming provider class to produce audio samples is an implementation detail and therefore omitted. What is important is that an instance of [`Resampler`](https://developer.apple.com#Creating-a-resampler) be able to ask for a number of samples at each conversion operation.

```swift
/// A protocol that specifies requirements of a type that is capable of producing audio data on a sample-by-sample basis.
protocol SampleProvider {
    /// Returns the next audio sample.
    func getNextSample() -> Float
}
```

The [`SampleProvider`](https://developer.apple.com#Creating-a-protocol-for-providing-samples) protocol might be implemented by a signal generator, such as the one described in [`Building a signal generator`](https://developer.apple.com/documentation/AVFAudio/building-a-signal-generator), by a synthesizer or by a circular buffer, for example.

#### Creating a Resampler

The [`Resampler`](https://developer.apple.com#Creating-a-resampler) class takes the output of a sample provider, resamples it using [`AVAudioConverter`](https://developer.apple.com/documentation/AVFAudio/AVAudioConverter), and copies the result to all channels of an [`AudioBufferList`](https://developer.apple.com/documentation/CoreAudioTypes/AudioBufferList):

```swift
/// A class that resamples the audio data furnished by a sample provider.
class Resampler {
    /// The generic class that implements the SampleProvider protocol.
    let sampleProvider: SampleProvider
    /// The converter that performs the resampling.
    let converter: AVAudioConverter
    /// The source audio buffer that stores the samples which will be fed to the converter.
    let sourceBuffer: AVAudioPCMBuffer
    
    /// Initializes a resampler with a source sample rate, a destination sample rate, and a sample provider.
    init(sourceSampleRate: Double, destinationSampleRate: Double, provider: SampleProvider) {
        self.sampleProvider = provider

        /// Create source and destination formats with the source and destination sample rates.
        let sourceFormat = AVAudioFormat(commonFormat: .pcmFormatFloat32, sampleRate: sourceSampleRate, channels: 1, interleaved: false)
        let destinationFormat = AVAudioFormat(commonFormat: .pcmFormatFloat32, sampleRate: destinationSampleRate, channels: 2, interleaved: false)

        /// Create the converter with the source and destination formats.
        self.converter = AVAudioConverter(from: sourceFormat, to: destinationFormat)

        /// Create the source audio buffer with the source format and enough capacity.
        self.sourceBuffer = AVAudioPCMBuffer(pcmFormat: sourceFormat, frameCapacity: 4096)
    }
    
    func refill(inNumberOfPackets: AVAudioPacketCount) -> AVAudioPCMBuffer {
        /// See code for this function below.
    }

    func resample(ioData: UnsafeMutablePointer<AudioBufferList>, inNumberFrames: UInt32) {
        /// See code for this function below.
    }
}
```

The converter asks for input buffers in the closure provided to [`convert(to:error:withInputFrom:)`](https://developer.apple.com/documentation/AVFAudio/AVAudioConverter/convert(to:error:withInputFrom:)). In order to avoid allocating audio buffers every time the converter asks for more input, the [`Resampler`](https://developer.apple.com#Creating-a-resampler) class reuses the source buffer that is passed as input to the converter. The source buffer’s underlying memory is simply refilled with the [`SampleProvider`](https://developer.apple.com#Creating-a-protocol-for-providing-samples) output for the requested number of frames and returned.

```swift
/// Takes as input the number of frames to be refilled.
/// Returns an audio buffer that references memory owned by the resampler, after refilling this memory with the output of the sample provider.
func refill(numberOfFrames: AVAudioPacketCount) -> AVAudioPCMBuffer {
    /// Store a pointer to the source buffer sample data.
    let sourceData = sourceBuffer.floatChannelData[0]
    
    /// Refill the source audio buffer with the requested number of frames.
    for frameIndex in 0..<Int(numberOfFrames) {
        sourceData[frameIndex] = sampleProvider.getNextSample()
    }
    
    /// Update the source buffer's frame length.
    sourceBuffer.frameLength = numberOfFrames;
    
    /// Return the refilled source buffer.
    return sourceBuffer
}
```

The [`AudioBufferList`](https://developer.apple.com/documentation/CoreAudioTypes/AudioBufferList) pointer that is provided in the call to `resample(ioData:)` is wrapped in an instance of [`AVAudioPCMBuffer`](https://developer.apple.com/documentation/AVFAudio/AVAudioPCMBuffer) using the [`init(pcmFormat:bufferListNoCopy:deallocator:)`](https://developer.apple.com/documentation/AVFAudio/AVAudioPCMBuffer/init(pcmFormat:bufferListNoCopy:deallocator:)) initializer. This buffer is passed to the converter in the call to [`convert(to:error:withInputFrom:)`](https://developer.apple.com/documentation/AVFAudio/AVAudioConverter/convert(to:error:withInputFrom:)) to store the output of the conversion. The converter calls the provided closure, passing it the input length and asking for a status flag and a returned audio buffer. The status is always [`AVAudioConverterInputStatus.haveData`](https://developer.apple.com/documentation/AVFAudio/AVAudioConverterInputStatus/haveData) in this case, since the sample provider can always produce an arbitrary number of samples. The returned audio buffer is the result of a call to `refill(inNumberOfPackets:)`, using the provided input length.

```swift
/// Takes as input an AudioBufferList pointer.
/// Resamples the output of the sample provider and copies the result to the given audio buffer list.
func resample(ioData: UnsafeMutablePointer<AudioBufferList>) {
    /// Create the destination audio buffer with the converter output format and referencing the provided AudioBufferList pointer.
    /// The buffers referred to by ioData are provided by the caller to be filled with output samples only and should not contain input samples.
    guard let destinationBuffer = AVAudioPCMBuffer(pcmFormat: converter.outputFormat, bufferListNoCopy: ioData) else { return }
    /// Create a local variable to hold a conversion error.
    var error: NSError?
    
    /// Perform a conversion operation and store the output in the destination buffer. The provided input will be the returned value of the trailing closure.
    let outputStatus = converter.convert(to: destinationBuffer, error: &error) { [unowned self] numberOfFrames, inputStatus in
        /// Tell the converter there is data available, since a SampleProvider can produce audio data on a sample-by-sample basis.
        inputStatus.pointee = .haveData
        /// Return the refilled source buffer.
        return self.refill(numberOfFrames: numberOfFrames)
    }
    
    if outputStatus == .error {
        /// If a conversion error occurred, log its localized description.
        if let error = error {
            print(error.localizedDescription)
        }
    }
}
```

The call to [`convert(to:error:withInputFrom:)`](https://developer.apple.com/documentation/AVFAudio/AVAudioConverter/convert(to:error:withInputFrom:)) attempts to fill the output buffer to its capacity, hence a single call is made to [`convert(to:error:withInputFrom:)`](https://developer.apple.com/documentation/AVFAudio/AVAudioConverter/convert(to:error:withInputFrom:)) in `resample(ioData:)`. Other conversion scenarios, such as audio data streamed from a file or over a network, or when the conversion involves compressed formats will often involve multiple calls to [`convert(to:error:withInputFrom:)`](https://developer.apple.com/documentation/AVFAudio/AVAudioConverter/convert(to:error:withInputFrom:)), depending on the returned [`AVAudioConverterOutputStatus`](https://developer.apple.com/documentation/AVFAudio/AVAudioConverterOutputStatus).

#### Revision History

-  First published.

## See Also

- [TN3190: USB audio device design considerations](tn3190-usb-audio-device-design-considerations.md)
  Learn the best techniques for designing devices that conform to the USB Audio Device Class specifications.
- [TN3194: Handling account deletions and revoking tokens for Sign in with Apple](tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple.md)
  Learn the best techniques for managing Sign in with Apple user sessions and responding to account deletion requests.
- [TN3193: Managing the on-device foundation model’s context window](tn3193-managing-the-on-device-foundation-model-s-context-window.md)
  Learn how to budget for the context window limit of Apple’s on-device foundation model and handle the error when reaching the limit.
- [TN3115: Bluetooth State Restoration app relaunch rules](tn3115-bluetooth-state-restoration-app-relaunch-rules.md)
  Learn about the conditions under which an iOS app will be relaunched by Bluetooth State Restoration.
- [TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key](tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md)
  Support iPad multitasking and dynamic resizing while updating your app to remove the deprecated full-screen compatibility mode.
- [TN3151: Choosing the right networking API](tn3151-choosing-the-right-networking-api.md)
  Learn which networking API is best for you.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3191: IMAP extensions supported by Mail for iOS, iPadOS, and visionOS](tn3191-imap-extensions-supported-by-mail.md)
  Learn which extensions to the RFC 3501 IMAP protocol are supported by Mail for iOS, iPadOS, and visionOS.
- [TN3134: Network Extension provider deployment](tn3134-network-extension-provider-deployment.md)
  Explore the platforms, packaging, OS versions, and device configurations for Network Extension provider deployment.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3136-avaudioconverter-performing-sample-rate-conversions)*