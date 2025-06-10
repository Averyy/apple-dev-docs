# AVSpeechSynthesisMarker.Mark

**Framework**: AVFAudio  
**Kind**: enum

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

## Topics

### Marks
- [AVSpeechSynthesisMarker.Mark.word](avspeechsynthesismarker/mark-swift.enum/word.md)
  A type of text that represents a word.
- [AVSpeechSynthesisMarker.Mark.sentence](avspeechsynthesismarker/mark-swift.enum/sentence.md)
  A type of text that represents a sentence.
- [AVSpeechSynthesisMarker.Mark.paragraph](avspeechsynthesismarker/mark-swift.enum/paragraph.md)
  A type of text that represents a paragraph.
- [AVSpeechSynthesisMarker.Mark.phoneme](avspeechsynthesismarker/mark-swift.enum/phoneme.md)
  A type of text that represents a phoneme.
- [AVSpeechSynthesisMarker.Mark.bookmark](avspeechsynthesismarker/mark-swift.enum/bookmark.md)
  A Speech Synthesis Markup Language (SSML) mark tag.
### Initializers
- [init?(rawValue: Int)](avspeechsynthesismarker/mark-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var mark: AVSpeechSynthesisMarker.Mark](avspeechsynthesismarker/mark-swift.property.md)
  The type that describes the text.
- [var bookmarkName: String](avspeechsynthesismarker/bookmarkname.md)
  A string that represents the name of a bookmark.
- [var phoneme: String](avspeechsynthesismarker/phoneme.md)
  A string that represents a distinct sound.
- [var textRange: NSRange](avspeechsynthesismarker/textrange.md)
  The location and length of the request’s text.
- [var byteSampleOffset: Int](avspeechsynthesismarker/bytesampleoffset.md)
  The byte offset into the audio buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesismarker/mark-swift.enum)*