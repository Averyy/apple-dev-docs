# Transcript.AttachmentSegment

**Framework**: Foundation Models  
**Kind**: struct

A segment containing attached files or images.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct AttachmentSegment
```

## Topics

### Creating an attachment segment
- [init(id: String, content: Transcript.Attachment, label: String?)](transcript/attachmentsegment/init(id:content:label:).md)
  Creates an attachment segment that wraps the content you provide.
### Inspecting an attachment segment
- [var content: Transcript.Attachment](transcript/attachmentsegment/content.md)
  The attached file or image.
- [var label: String?](transcript/attachmentsegment/label.md)
  An optional label that identifies the attachment.

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
- [Transcript.TextSegment](transcript/textsegment.md)
  A segment containing text.
- [Transcript.StructuredSegment](transcript/structuredsegment.md)
  A segment containing structured content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/attachmentsegment)*