# init(id:makeContent:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates the immersive space associated with the specified identifier using view-based content.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init<V>(id: String, @ContentBuilder makeContent: @escaping () -> V) where Content == ImmersiveSpaceViewContent<V>, Data == Never, V : View
```

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to `Hashable`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(id: String, @ImmersiveSpaceContentBuilder makeContent: @escaping () -> Content) where Data == Never
```

```swift
nonisolated
init<C>(id: String, @CompositorContentBuilder makeContent: @escaping () -> C) where Content == CompositorContentBuilder.Content<C>, Data == Never, C : CompositorContent
```

## Discussion

The immersive space uses the specified view as a template to form the content of the space.

## Parameters

- `id`: A string that uniquely identifies the immersive space. Ensure that identifiers are unique among the immersive spaces in your app.
- `makeContent`: A content builder that defines the content for each instance of the immersive space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivespace/init(id:makecontent:)-4jicn)*