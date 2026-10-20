# buildBlock(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Creates a single content result.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
static func buildBlock<C>(_ content: C) -> C where C : AttachmentContent
```

**Other overloads**:

```swift
static func buildBlock<each Content>(_ content: repeat each Content) -> TuplePackAttachmentContent<repeat each Content> where repeat each Content : AttachmentContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/attachmentcontentbuilder/buildblock(_:))*