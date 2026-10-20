# processingFormat

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The processing format of the file.

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
var processingFormat: AVAudioFormat { get }
```

```objc
@property (nonatomic, readonly) AVAudioFormat * processingFormat;
```

## See Also

### Getting audio file properties
- [var url: URL](./url.md)
  The location of the audio file.
- [var fileFormat: AVAudioFormat](./fileformat.md)
  The on-disk format of the file.
- [var length: AVAudioFramePosition](./length.md)
  The number of sample frames in the file.
- [typealias AVAudioFramePosition](../avaudioframeposition.md)
  A position in an audio file or stream.
- [var framePosition: AVAudioFramePosition](./frameposition.md)
  The position in the file where the next read or write operation occurs.
- [typealias AVAudioFrameCount](../avaudioframecount.md)
  A number of audio sample frames.
- [let AVAudioFileTypeKey: String](../avaudiofiletypekey.md)
  A string that indicates the audio file type.
- [var isOpen: Bool](./isopen.md)
  A Boolean value that indicates whether the file is open.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiofile/processingformat)*