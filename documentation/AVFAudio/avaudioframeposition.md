# AVAudioFramePosition

**Framework**: AVFAudio  
**Kind**: typealias  
**Role**: Type Alias

A position in an audio file or stream.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias AVAudioFramePosition = Int64
```

```c
typedef int64_t AVAudioFramePosition;
```

## See Also

### Getting audio file properties
- [var url: URL](./avaudiofile/url.md)
  The location of the audio file.
- [var fileFormat: AVAudioFormat](./avaudiofile/fileformat.md)
  The on-disk format of the file.
- [var processingFormat: AVAudioFormat](./avaudiofile/processingformat.md)
  The processing format of the file.
- [var length: AVAudioFramePosition](./avaudiofile/length.md)
  The number of sample frames in the file.
- [var framePosition: AVAudioFramePosition](./avaudiofile/frameposition.md)
  The position in the file where the next read or write operation occurs.
- [typealias AVAudioFrameCount](./avaudioframecount.md)
  A number of audio sample frames.
- [let AVAudioFileTypeKey: String](./avaudiofiletypekey.md)
  A string that indicates the audio file type.
- [var isOpen: Bool](./avaudiofile/isopen.md)
  A Boolean value that indicates whether the file is open.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioframeposition)*