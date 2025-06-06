# buildEither(first:)

**Framework**: RealityKit  
**Kind**: method

Provides support for “if” statements in multi-statement closures, producing conditional content for the “then” branch.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> ConditionalAttachmentContent<TrueContent, FalseContent> where TrueContent : AttachmentContent, FalseContent : AttachmentContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/attachmentcontentbuilder/buildeither(first:))*