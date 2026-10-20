# Transcript.StructuredSegment

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A segment containing structured content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
struct StructuredSegment
```

## Topics

### Creating a structured segment
- [init(id: String, source: String, content: GeneratedContent)](./structuredsegment/init%28id,source,content%29.md)
- [init(id: String, schemaName: String, content: GeneratedContent)](./structuredsegment/init%28id,schemaname,content%29.md)
  Creates a structured segment that contains the generated content you provide.
### Inspecting a structured segment
- [var content: GeneratedContent](./structuredsegment/content.md)
  The content of the segment.
- [var source: String](./structuredsegment/source.md)
  A source that can be used to understand which type the content represents.
- [var schemaName: String](./structuredsegment/schemaname.md)
  A name that can be used to understand which type the content represents.

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
- [Transcript.TextSegment](./textsegment.md)
  A segment containing text.
- [Transcript.AttachmentSegment](./attachmentsegment.md)
  A segment containing attached files or images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/structuredsegment)*