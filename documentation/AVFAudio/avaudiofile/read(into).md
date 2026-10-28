# read(into:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Reads an entire audio buffer.

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
func read(into buffer: AVAudioPCMBuffer) throws
```

```objc
- (BOOL) readIntoBuffer:(AVAudioPCMBuffer *) buffer error:(NSError **) outError;
```

## Discussion

When reading sequentially from the [`framePosition`](./frameposition.md) property, the method attempts to fill the buffer to its capacity. On return, the buffer’s [`length`](./length.md) property indicates the number of sample frames it successfully reads.

## Parameters

- `buffer`: The buffer from which to read the file. Its format must match the file’s processing format.

## See Also

### Related Documentation
- [var framePosition: AVAudioFramePosition](./frameposition.md)
  The position in the file where the next read or write operation occurs.
- [var length: AVAudioFramePosition](./length.md)
  The number of sample frames in the file.
### Reading and writing audio
- [func read(into: AVAudioPCMBuffer, frameCount: AVAudioFrameCount) throws](./read%28into,framecount%29.md)
  Reads a portion of an audio buffer using the number of frames you specify.
- [func read(frameCount: AVAudioFrameCount) throws -> AVReadOnlyAudioPCMBuffer](./read%28framecount%29.md)
- [func write(from: AVAudioPCMBuffer) throws](./write%28from%29-6qgec.md)
  Writes an audio buffer sequentially.
- [func write(from: AVReadOnlyAudioPCMBuffer) throws](./write%28from%29-4zfhf.md)
- [func close()](./close%28%29.md)
  Closes the audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiofile/read(into:))*