# TuplePackAttachmentContent

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Attachment content that combines any number of attachment content values from an attachment content builder.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
@MainActor
@frozen @preconcurrency struct TuplePackAttachmentContent<each T> where repeat each T : AttachmentContent
```

## Relationships

### Conforms To
- [AttachmentContent](./attachmentcontent.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Attachment types
- [struct AttachmentContentBuilder](./attachmentcontentbuilder.md)
  A result builder that creates attachment content from closures.
- [protocol AttachmentContent](./attachmentcontent.md)
  A type that provides content for an attachment content builder.
- [struct ConditionalAttachmentContent](./conditionalattachmentcontent.md)
  Attachment content that holds the result of one branch of a conditional statement in an attachment content builder.
- [struct EmptyAttachmentContent](./emptyattachmentcontent.md)
  A attachment content that doesn’t contain any content.
- [struct TupleAttachmentContent](./tupleattachmentcontent.md)
  Attachment content that wraps a tuple of attachment content values.
- [struct AnyAttachmentContent](./anyattachmentcontent.md)
  A type-erased attachment content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/tuplepackattachmentcontent)*