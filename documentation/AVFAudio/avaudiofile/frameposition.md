# framePosition

**Framework**: AVFAudio  
**Kind**: property

The position in the file where the next read or write operation occurs.

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
var framePosition: AVAudioFramePosition { get set }
```

#### Discussion

Set the `framePosition` property to perform a seek before a read or write. A read or write operation advances the frame position value by the number of frames it reads or writes.

## See Also

- [var url: URL](avaudiofile/url.md)
  The location of the audio file.
- [var fileFormat: AVAudioFormat](avaudiofile/fileformat.md)
  The on-disk format of the file.
- [var processingFormat: AVAudioFormat](avaudiofile/processingformat.md)
  The processing format of the file.
- [var length: AVAudioFramePosition](avaudiofile/length.md)
  The number of sample frames in the file.
- [typealias AVAudioFramePosition](avaudioframeposition.md)
  A position in an audio file or stream.
- [typealias AVAudioFrameCount](avaudioframecount.md)
  A number of audio sample frames.
- [let AVAudioFileTypeKey: String](avaudiofiletypekey.md)
  A string that indicates the audio file type.
- [var isOpen: Bool](avaudiofile/isopen.md)
  A Boolean value that indicates whether the file is open.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiofile/frameposition)*