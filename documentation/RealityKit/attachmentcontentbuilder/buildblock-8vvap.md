# buildBlock(_:)

**Framework**: RealityKit  
**Kind**: method

Provides support for lists of Attachments to be created in parallel.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
static func buildBlock<each Content>(_ content: repeat each Content) -> TupleAttachmentContent<(repeat each Content)> where repeat each Content : AttachmentContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/attachmentcontentbuilder/buildblock(_:)-8vvap)*