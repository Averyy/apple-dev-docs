# isOpen

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the file is open.

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
var isOpen: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isOpen;
```

## See Also

### Getting audio file properties
- [var url: URL](./url.md)
  The location of the audio file.
- [var fileFormat: AVAudioFormat](./fileformat.md)
  The on-disk format of the file.
- [var processingFormat: AVAudioFormat](./processingformat.md)
  The processing format of the file.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiofile/isopen)*