# write(from:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Writes an audio buffer sequentially.

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
func write(from buffer: AVAudioPCMBuffer) throws
```

```objc
- (BOOL) writeFromBuffer:(const AVAudioPCMBuffer *) buffer error:(NSError **) outError;
```

## Discussion

The buffer’s [`frameLength`](../avaudiopcmbuffer/framelength.md) signifies how much of the buffer the method writes.

## Parameters

- `buffer`: The buffer from which to write to the file. Its format must match the file’s processing format.

## See Also

### Reading and writing audio
- [func read(into: AVAudioPCMBuffer) throws](./read%28into%29.md)
  Reads an entire audio buffer.
- [func read(into: AVAudioPCMBuffer, frameCount: AVAudioFrameCount) throws](./read%28into,framecount%29.md)
  Reads a portion of an audio buffer using the number of frames you specify.
- [func read(frameCount: AVAudioFrameCount) throws -> AVReadOnlyAudioPCMBuffer](./read%28framecount%29.md)
- [func write(from: AVReadOnlyAudioPCMBuffer) throws](./write%28from%29-4zfhf.md)
- [func close()](./close%28%29.md)
  Closes the audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiofile/write(from:)-6qgec)*