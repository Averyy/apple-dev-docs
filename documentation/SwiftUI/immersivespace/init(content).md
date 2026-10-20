# init(content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an immersive space.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(@ImmersiveSpaceContentBuilder content: @escaping () -> Content) where Data == Never
```

**Other overloads**:

```swift
nonisolated
init<V>(@ContentBuilder content: @escaping () -> V) where Content == ImmersiveSpaceViewContent<V>, Data == Never, V : View
```

#### Discussion

The space uses the specified content builder to form the content.

## Parameters

- `content`: An immersive space content builder that defines the content of the space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivespace/init(content:))*