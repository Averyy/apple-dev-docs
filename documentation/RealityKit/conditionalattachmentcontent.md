# ConditionalAttachmentContent

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Attachment content that holds the result of one branch of a conditional statement in an attachment content builder.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@frozen
struct ConditionalAttachmentContent<TrueContent, FalseContent>
```

## Relationships

### Conforms To
- [AttachmentContent](./attachmentcontent.md)
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)

## See Also

### Attachment types
- [struct AttachmentContentBuilder](./attachmentcontentbuilder.md)
  A result builder that creates attachment content from closures.
- [protocol AttachmentContent](./attachmentcontent.md)
  A type that provides content for an attachment content builder.
- [struct TuplePackAttachmentContent](./tuplepackattachmentcontent.md)
  Attachment content that combines any number of attachment content values from an attachment content builder.
- [struct EmptyAttachmentContent](./emptyattachmentcontent.md)
  A attachment content that doesn’t contain any content.
- [struct TupleAttachmentContent](./tupleattachmentcontent.md)
  Attachment content that wraps a tuple of attachment content values.
- [struct AnyAttachmentContent](./anyattachmentcontent.md)
  A type-erased attachment content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/conditionalattachmentcontent)*