# init(content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an immersive space using view-based content.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<V>(@ContentBuilder content: @escaping () -> V) where Content == ImmersiveSpaceViewContent<V>, Data == Never, V : View
```

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to `Hashable`.

**Other overloads**:

```swift
nonisolated
init(@ImmersiveSpaceContentBuilder content: @escaping () -> Content) where Data == Never
```

## Discussion

The immersive space uses the specified view as a template to form the content of the space.

## Parameters

- `content`: A content builder that defines the content for each instance of the immersive space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivespace/init(content:)-5di5z)*