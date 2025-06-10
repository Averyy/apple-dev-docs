# close()

**Framework**: AVFAudio  
**Kind**: method

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

#### Discussion

Calling this method closes the underlying file, if open. It’s normally unnecessary to close a file opened for reading because it’s automatically closed when released. It’s only necessary to close a file opened for writing in order to achieve specific control over when the file’s header is updated.

> **Note**:  Once closed, further file read or write operations fail with a [`kAudio_FileNotFoundError`](https://developer.apple.com/documentation/CoreAudioTypes/kAudio_FileNotFoundError).

## See Also

- [func read(into: AVAudioPCMBuffer) throws](avaudiofile/read(into:).md)
  Reads an entire audio buffer.
- [func read(into: AVAudioPCMBuffer, frameCount: AVAudioFrameCount) throws](avaudiofile/read(into:framecount:).md)
  Reads a portion of an audio buffer using the number of frames you specify.
- [func write(from: AVAudioPCMBuffer) throws](avaudiofile/write(from:).md)
  Writes an audio buffer sequentially.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiofile/close())*