# init(id:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates the immersive space associated with the specified identifier.

**Availability**:
- visionOS 1.0+ - Deprecated in 26.0 (renamed: init(id:makeContent:))

## Declaration

```swift
nonisolated
init(id: String, @ImmersiveSpaceContentBuilder content: () -> Content) where Data == Never
```

**Other overloads**:

```swift
nonisolated
init<V>(id: String, @ContentBuilder content: () -> V) where Content == ImmersiveSpaceViewContent<V>, Data == Never, V : View
```

#### Discussion

The space uses the specified content builder to form the content.

## Parameters

- `id`: A string that uniquely identifies the immersive space. Ensure that identifiers are unique among the immersive spaces in your app.
- `content`: An immersive space content builder that defines the content of the space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivespace/init(id:content:))*