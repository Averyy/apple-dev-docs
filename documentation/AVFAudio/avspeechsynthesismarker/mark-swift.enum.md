# AVSpeechSynthesisMarker.Mark

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the type of text.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum Mark
```

```c
enum AVSpeechSynthesisMarkerMark : NSInteger;
```

## Topics

### Creating a mark
- [init?(rawValue: Int)](./mark-swift.enum/init%28rawvalue%29.md)
### Identifying marker types
- [AVSpeechSynthesisMarker.Mark.word](./mark-swift.enum/word.md)
  A type of text that represents a word.
- [AVSpeechSynthesisMarker.Mark.sentence](./mark-swift.enum/sentence.md)
  A type of text that represents a sentence.
- [AVSpeechSynthesisMarker.Mark.paragraph](./mark-swift.enum/paragraph.md)
  A type of text that represents a paragraph.
- [AVSpeechSynthesisMarker.Mark.phoneme](./mark-swift.enum/phoneme.md)
  A type of text that represents a phoneme.
- [AVSpeechSynthesisMarker.Mark.bookmark](./mark-swift.enum/bookmark.md)
  A Speech Synthesis Markup Language (SSML) mark tag.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting a marker
- [var mark: AVSpeechSynthesisMarker.Mark](./mark-swift.property.md)
  The type that describes the text.
- [var bookmarkName: String](./bookmarkname.md)
  A string that represents the name of a bookmark.
- [var phoneme: String](./phoneme.md)
  A string that represents a distinct sound.
- [var textRange: NSRange](./textrange.md)
  The location and length of the request’s text.
- [var byteSampleOffset: Int](./bytesampleoffset.md)
  The byte offset into the audio buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesismarker/mark-swift.enum)*