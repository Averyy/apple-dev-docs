# init(makeContent:)

**Framework**: SwiftUI  
**Kind**: init

**Availability**:
- visionOS 26.0+

## Declaration

```swift
nonisolated
init<C>(@CompositorContentBuilder makeContent: @escaping () -> C) where Content == CompositorContentBuilder.Content<C>, Data == Never, C : CompositorContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivespace/init(makecontent:))*