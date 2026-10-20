# init(for:makeContent:defaultValue:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

**Availability**:
- visionOS 26.0+

## Declaration

```swift
nonisolated
init<C>(for type: Data.Type = Data.self, @CompositorContentBuilder makeContent: @escaping (Binding<Data>) -> C, defaultValue: @escaping () -> Data) where Content == CompositorContentBuilder.Content<C>, C : CompositorContent
```

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to `Hashable`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivespace/init(for:makecontent:defaultvalue:))*