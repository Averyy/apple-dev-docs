# read(into:frameCount:)

**Framework**: AVFAudio  
**Kind**: method

Reads a portion of an audio buffer using the number of frames you specify.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func read(into buffer: AVAudioPCMBuffer, frameCount frames: AVAudioFrameCount) throws
```

#### Discussion

You use this method to read fewer frames than the buffer’s `frameCapacity`.

## Parameters

- `buffer`: The buffer from which to read the file. Its format must match the file’s processing format.
- `frames`: The number of frames to read.

## See Also

- [func read(into: AVAudioPCMBuffer) throws](avaudiofile/read(into:).md)
  Reads an entire audio buffer.
- [func write(from: AVAudioPCMBuffer) throws](avaudiofile/write(from:).md)
  Writes an audio buffer sequentially.
- [func close()](avaudiofile/close.md)
  Closes the audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiofile/read(into:framecount:))*