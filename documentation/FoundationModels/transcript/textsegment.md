# Transcript.TextSegment

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

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
- [init(id: String, content: String)](./textsegment/init%28id,content%29.md)
  Creates a text segment that contains the text you provide.
### Inspecting a text segment
- [var content: String](./textsegment/content.md)
  The text of the segment.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Identifiable](../../Swift/identifiable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Segments
- [Transcript.Segment](./segment.md)
  The types of segments that may be included in a transcript entry.
- [Transcript.StructuredSegment](./structuredsegment.md)
  A segment containing structured content.
- [Transcript.AttachmentSegment](./attachmentsegment.md)
  A segment containing attached files or images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/textsegment)*