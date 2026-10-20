# init(id:makeContent:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates the immersive space associated with the specified identifier.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init(id: String, @ImmersiveSpaceContentBuilder makeContent: @escaping () -> Content) where Data == Never
```

**Other overloads**:

```swift
@export(implementation)
nonisolated init<V>(id: String, @ContentBuilder makeContent: @escaping () -> V) where Content == ImmersiveSpaceViewContent<V>, Data == Never, V : View
```

```swift
nonisolated
init<C>(id: String, @CompositorContentBuilder makeContent: @escaping () -> C) where Content == CompositorContentBuilder.Content<C>, Data == Never, C : CompositorContent
```

#### Discussion

The space uses the specified content builder to form the content.

## Parameters

- `id`: A string that uniquely identifies the immersive space. Ensure that identifiers are unique among the immersive spaces in your app.
- `makeContent`: An immersive space content builder that defines the content of the space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivespace/init(id:makecontent:))*