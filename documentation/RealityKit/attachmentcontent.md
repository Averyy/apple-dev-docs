# AttachmentContent

**Framework**: RealityKit  
**Kind**: protocol

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
- [associatedtype Body : AttachmentContent](attachmentcontent/body-swift.associatedtype.md)
### Instance Properties
- [var body: Self.Body](attachmentcontent/body-swift.property.md)

## Relationships

### Conforming Types
- [AnyAttachmentContent](anyattachmentcontent.md)
- [Attachment](attachment.md)
- [ConditionalAttachmentContent](conditionalattachmentcontent.md)
- [EmptyAttachmentContent](emptyattachmentcontent.md)
- [TupleAttachmentContent](tupleattachmentcontent.md)
- [TuplePackAttachmentContent](tuplepackattachmentcontent.md)

## See Also

- [struct AttachmentContentBuilder](attachmentcontentbuilder.md)
  A result builder that creates attachment content from closures.
- [struct TuplePackAttachmentContent](tuplepackattachmentcontent.md)
- [struct ConditionalAttachmentContent](conditionalattachmentcontent.md)
- [struct EmptyAttachmentContent](emptyattachmentcontent.md)
  A attachment content that doesn’t contain any content.
- [struct TupleAttachmentContent](tupleattachmentcontent.md)
- [struct AnyAttachmentContent](anyattachmentcontent.md)
  A type-erased attachment content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/attachmentcontent)*