# Transcript.AttachmentSegment

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

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
- [init(id: String, content: Transcript.Attachment, label: String?)](./attachmentsegment/init%28id,content,label%29.md)
  Creates an attachment segment that wraps the content you provide.
### Inspecting an attachment segment
- [var content: Transcript.Attachment](./attachmentsegment/content.md)
  The attached file or image.
- [var label: String?](./attachmentsegment/label.md)
  An optional label that identifies the attachment.

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
- [Transcript.StructuredSegment](./structuredsegment.md)
  A segment containing structured content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/attachmentsegment)*