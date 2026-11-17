# AttachmentContent

**Framework**: RealityKit  
**Kind**: protocol  
**Role**: Protocol

A type that provides content for an attachment content builder.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol AttachmentContent
```

## Topics

### Associated Types
- [associatedtype Body : AttachmentContent](./attachmentcontent/body-swift.associatedtype.md)
### Instance Properties
- [var body: Self.Body](./attachmentcontent/body-swift.property.md)

## Relationships

### Conforming Types
- [AnyAttachmentContent](./anyattachmentcontent.md)
- [Attachment](./attachment.md)
- [ConditionalAttachmentContent](./conditionalattachmentcontent.md)
- [EmptyAttachmentContent](./emptyattachmentcontent.md)
- [TupleAttachmentContent](./tupleattachmentcontent.md)
- [TuplePackAttachmentContent](./tuplepackattachmentcontent.md)

## See Also

### Attachment types
- [struct AttachmentContentBuilder](./attachmentcontentbuilder.md)
  A result builder that creates attachment content from closures.
- [struct TuplePackAttachmentContent](./tuplepackattachmentcontent.md)
  Attachment content that combines any number of attachment content values from an attachment content builder.
- [struct ConditionalAttachmentContent](./conditionalattachmentcontent.md)
  Attachment content that holds the result of one branch of a conditional statement in an attachment content builder.
- [struct EmptyAttachmentContent](./emptyattachmentcontent.md)
  A attachment content that doesn’t contain any content.
- [struct TupleAttachmentContent](./tupleattachmentcontent.md)
  Attachment content that wraps a tuple of attachment content values.
- [struct AnyAttachmentContent](./anyattachmentcontent.md)
  A type-erased attachment content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/attachmentcontent)*