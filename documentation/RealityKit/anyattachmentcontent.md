# AnyAttachmentContent

**Framework**: RealityKit  
**Kind**: struct

A type-erased attachment content.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
@frozen @preconcurrency struct AnyAttachmentContent
```

#### Overview

An `AnyAttachmentContent` allows changing the type of attachment used in a given attachment content. Whenever the type of attachment content used with an `AnyAttachmentContent` changes, the old content is destroyed and the new content is created for the new type.

## Topics

### Initializers
- [init<Content>(Content)](anyattachmentcontent/init(_:).md)
  Creates an instance that type-erases [`AttachmentContent`](attachmentcontent.md).
### Type Aliases
- [AnyAttachmentContent.Body](anyattachmentcontent/body.md)

## Relationships

### Conforms To
- [AttachmentContent](attachmentcontent.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct AttachmentContentBuilder](attachmentcontentbuilder.md)
  A result builder that creates attachment content from closures.
- [protocol AttachmentContent](attachmentcontent.md)
  A type that provides content for an attachment content builder.
- [struct ConditionalAttachmentContent](conditionalattachmentcontent.md)
- [struct EmptyAttachmentContent](emptyattachmentcontent.md)
  A attachment content that doesn’t contain any content.
- [struct TupleAttachmentContent](tupleattachmentcontent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anyattachmentcontent)*