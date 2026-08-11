# Transcript.StructuredSegment

**Framework**: Foundation Models  
**Kind**: struct

A segment containing structured content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct StructuredSegment
```

## Topics

### Creating a structured segment
- [init(id: String, source: String, content: GeneratedContent)](transcript/structuredsegment/init(id:source:content:).md)
- [init(id: String, schemaName: String, content: GeneratedContent)](transcript/structuredsegment/init(id:schemaname:content:).md)
### Inspecting a structured segment
- [var content: GeneratedContent](transcript/structuredsegment/content.md)
  The content of the segment.
- [var source: String](transcript/structuredsegment/source.md)
  A source that can be used to understand which type the content represents.
- [var schemaName: String](transcript/structuredsegment/schemaname.md)
  A name that can be used to understand which type the content represents.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Transcript.Segment](transcript/segment.md)
  The types of segments that may be included in a transcript entry.
- [Transcript.TextSegment](transcript/textsegment.md)
  A segment containing text.
- [Transcript.AttachmentSegment](transcript/attachmentsegment.md)
  A segment containing attached files or images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/structuredsegment)*