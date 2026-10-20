# close()

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Closes the audio file.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func close()
```

```objc
- (void) close;
```

#### Discussion

Calling this method closes the underlying file, if open. It’s normally unnecessary to close a file opened for reading because it’s automatically closed when released. It’s only necessary to close a file opened for writing in order to achieve specific control over when the file’s header is updated.

> **Note**:  Once closed, further file read or write operations fail with a [`kAudio_FileNotFoundError`](../../CoreAudioTypes/kaudio_filenotfounderror.md).

## See Also

### Reading and writing audio
- [func read(into: AVAudioPCMBuffer) throws](./read%28into%29.md)
  Reads an entire audio buffer.
- [func read(into: AVAudioPCMBuffer, frameCount: AVAudioFrameCount) throws](./read%28into,framecount%29.md)
  Reads a portion of an audio buffer using the number of frames you specify.
- [func read(frameCount: AVAudioFrameCount) throws -> AVReadOnlyAudioPCMBuffer](./read%28framecount%29.md)
- [func write(from: AVAudioPCMBuffer) throws](./write%28from%29-6qgec.md)
  Writes an audio buffer sequentially.
- [func write(from: AVReadOnlyAudioPCMBuffer) throws](./write%28from%29-4zfhf.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiofile/close())*