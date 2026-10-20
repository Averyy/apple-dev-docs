# write(from:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

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
func write(from buffer: AVReadOnlyAudioPCMBuffer) throws
```

## See Also

### Reading and writing audio
- [func read(into: AVAudioPCMBuffer) throws](./read%28into%29.md)
  Reads an entire audio buffer.
- [func read(into: AVAudioPCMBuffer, frameCount: AVAudioFrameCount) throws](./read%28into,framecount%29.md)
  Reads a portion of an audio buffer using the number of frames you specify.
- [func read(frameCount: AVAudioFrameCount) throws -> AVReadOnlyAudioPCMBuffer](./read%28framecount%29.md)
- [func write(from: AVAudioPCMBuffer) throws](./write%28from%29-6qgec.md)
  Writes an audio buffer sequentially.
- [func close()](./close%28%29.md)
  Closes the audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiofile/write(from:)-4zfhf)*