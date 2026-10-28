# init(id:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates the immersive space associated with the specified identifier using view-based content.

**Availability**:
- visionOS 1.0+ - Deprecated in 26.0 (renamed: init(id:makeContent:))

## Declaration

```swift
nonisolated
init<V>(id: String, @ContentBuilder content: () -> V) where Content == ImmersiveSpaceViewContent<V>, Data == Never, V : View
```

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to `Hashable`.

**Other overloads**:

```swift
nonisolated
init(id: String, @ImmersiveSpaceContentBuilder content: () -> Content) where Data == Never
```

## Discussion

The immersive space uses the specified view as a template to form the content of the space.

## Parameters

- `id`: A string that uniquely identifies the immersive space. Ensure that identifiers are unique among the immersive spaces in your app.
- `content`: A content builder that defines the content for each instance of the immersive space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivespace/init(id:content:)-5keb4)*