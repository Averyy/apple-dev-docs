# buildIf(_:)

**Framework**: RealityKit  
**Kind**: method

Provides support for “if” statements in multi-statement closures, producing an optional view that is visible only when the condition evaluates to `true`.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
static func buildIf<Content>(_ content: Content?) -> Content? where Content : AttachmentContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/attachmentcontentbuilder/buildif(_:))*