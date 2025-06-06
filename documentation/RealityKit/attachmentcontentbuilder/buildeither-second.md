# buildEither(second:)

**Framework**: RealityKit  
**Kind**: method

Provides support for “if-else” statements in multi-statement closures, producing conditional content for the “else” branch.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> ConditionalAttachmentContent<TrueContent, FalseContent> where TrueContent : AttachmentContent, FalseContent : AttachmentContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/attachmentcontentbuilder/buildeither(second:))*