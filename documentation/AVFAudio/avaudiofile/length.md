# length

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The number of sample frames in the file.

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
var length: AVAudioFramePosition { get }
```

```objc
@property (nonatomic, readonly) AVAudioFramePosition length;
```

#### Discussion

This can be computationally expensive to compute for the first time.

## See Also

### Getting audio file properties
- [var url: URL](./url.md)
  The location of the audio file.
- [var fileFormat: AVAudioFormat](./fileformat.md)
  The on-disk format of the file.
- [var processingFormat: AVAudioFormat](./processingformat.md)
  The processing format of the file.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiofile/length)*