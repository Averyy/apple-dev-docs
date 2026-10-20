# init(makeContent:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

**Availability**:
- visionOS 26.0+

## Declaration

```swift
nonisolated
init<C>(@CompositorContentBuilder makeContent: @escaping () -> C) where Content == CompositorContentBuilder.Content<C>, Data == Never, C : CompositorContent
```

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to `Hashable`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivespace/init(makecontent:))*