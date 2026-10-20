# read(into:frameCount:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) readIntoBuffer:(AVAudioPCMBuffer *) buffer frameCount:(AVAudioFrameCount) frames error:(NSError **) outError;
```

#### Discussion

You use this method to read fewer frames than the buffer’s `frameCapacity`.

## Parameters

- `buffer`: The buffer from which to read the file. Its format must match the file’s processing format.
- `frames`: The number of frames to read.

## See Also

### Reading and writing audio
- [func read(into: AVAudioPCMBuffer) throws](./read%28into%29.md)
  Reads an entire audio buffer.
- [func read(frameCount: AVAudioFrameCount) throws -> AVReadOnlyAudioPCMBuffer](./read%28framecount%29.md)
- [func write(from: AVAudioPCMBuffer) throws](./write%28from%29-6qgec.md)
  Writes an audio buffer sequentially.
- [func write(from: AVReadOnlyAudioPCMBuffer) throws](./write%28from%29-4zfhf.md)
- [func close()](./close%28%29.md)
  Closes the audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiofile/read(into:framecount:))*