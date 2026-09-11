# read(frameCount:)

**Framework**: AVFAudio  
**Kind**: method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func read(frameCount: AVAudioFrameCount) throws -> AVReadOnlyAudioPCMBuffer
```

## See Also

- [func read(into: AVAudioPCMBuffer) throws](avaudiofile/read(into:).md)
  Reads an entire audio buffer.
- [func read(into: AVAudioPCMBuffer, frameCount: AVAudioFrameCount) throws](avaudiofile/read(into:framecount:).md)
  Reads a portion of an audio buffer using the number of frames you specify.
- [func close()](avaudiofile/close.md)
  Closes the audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiofile/read(framecount:))*