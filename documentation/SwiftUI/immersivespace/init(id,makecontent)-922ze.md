# init(id:makeContent:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

**Availability**:
- visionOS 26.0+

## Declaration

```swift
nonisolated
init<C>(id: String, @CompositorContentBuilder makeContent: @escaping () -> C) where Content == CompositorContentBuilder.Content<C>, Data == Never, C : CompositorContent
```

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to `Hashable`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(id: String, @ImmersiveSpaceContentBuilder makeContent: @escaping () -> Content) where Data == Never
```

```swift
@export(implementation)
nonisolated init<V>(id: String, @ContentBuilder makeContent: @escaping () -> V) where Content == ImmersiveSpaceViewContent<V>, Data == Never, V : View
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivespace/init(id:makecontent:)-922ze)*