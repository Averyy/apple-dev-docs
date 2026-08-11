# Transcript.AttachmentSegment

**Framework**: Foundation Models  
**Kind**: struct

A segment containing attached files or images.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct AttachmentSegment
```

## Topics

### Creating an attachment segment
- [init(id: String, content: Transcript.Attachment, label: String?)](transcript/attachmentsegment/init(id:content:label:).md)
### Inspecting an attachment segment
- [var content: Transcript.Attachment](transcript/attachmentsegment/content.md)
- [var label: String?](transcript/attachmentsegment/label.md)

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
- [Transcript.StructuredSegment](transcript/structuredsegment.md)
  A segment containing structured content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/attachmentsegment)*