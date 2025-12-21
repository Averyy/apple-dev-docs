# init(for:makeContent:defaultValue:)

**Framework**: SwiftUI  
**Kind**: init

**Availability**:
- visionOS 26.0+

## Declaration

```swift
nonisolated
init<C>(for type: Data.Type = Data.self, @CompositorContentBuilder makeContent: @escaping (Binding<Data>) -> C, defaultValue: @escaping () -> Data) where Content == CompositorContentBuilder.Content<C>, C : CompositorContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivespace/init(for:makecontent:defaultvalue:))*