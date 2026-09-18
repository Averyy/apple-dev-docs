# Transcript.TextSegment

**Framework**: Foundation Models  
**Kind**: struct

A segment containing text.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
struct TextSegment
```

## Topics

### Creating a text segment
- [init(id: String, content: String)](transcript/textsegment/init(id:content:).md)
  Creates a text segment that contains the text you provide.
### Inspecting a text segment
- [var content: String](transcript/textsegment/content.md)
  The text of the segment.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Transcript.Segment](transcript/segment.md)
  The types of segments that may be included in a transcript entry.
- [Transcript.StructuredSegment](transcript/structuredsegment.md)
  A segment containing structured content.
- [Transcript.AttachmentSegment](transcript/attachmentsegment.md)
  A segment containing attached files or images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/textsegment)*