# TuplePackAttachmentContent

**Framework**: RealityKit  
**Kind**: struct

**Availability**:
- visionOS 26.0+

## Declaration

```swift
@MainActor
@frozen @preconcurrency struct TuplePackAttachmentContent<each T> where repeat each T : AttachmentContent
```

## Relationships

### Conforms To
- [AttachmentContent](attachmentcontent.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AttachmentContentBuilder](attachmentcontentbuilder.md)
  A result builder that creates attachment content from closures.
- [protocol AttachmentContent](attachmentcontent.md)
  A type that provides content for an attachment content builder.
- [struct ConditionalAttachmentContent](conditionalattachmentcontent.md)
- [struct EmptyAttachmentContent](emptyattachmentcontent.md)
  A attachment content that doesn’t contain any content.
- [struct TupleAttachmentContent](tupleattachmentcontent.md)
- [struct AnyAttachmentContent](anyattachmentcontent.md)
  A type-erased attachment content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/tuplepackattachmentcontent)*