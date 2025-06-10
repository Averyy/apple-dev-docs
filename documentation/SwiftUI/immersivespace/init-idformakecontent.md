# init(id:for:makeContent:)

**Framework**: SwiftUI  
**Kind**: init

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
init<C>(id: String, for type: Data.Type, @CompositorContentBuilder makeContent: @escaping (Binding<Data?>) -> C) where Content == CompositorContentBuilder.Content<C>, C : CompositorContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivespace/init(id:for:makecontent:))*