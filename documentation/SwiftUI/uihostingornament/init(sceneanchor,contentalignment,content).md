# init(sceneAnchor:contentAlignment:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an ornament with the specified alignment and content.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
init(sceneAnchor: UnitPoint, contentAlignment: Alignment = .center, @ContentBuilder content: () -> Content)
```

**Other overloads**:

```swift
init(sceneAnchor: UnitPoint, contentAlignment: Alignment3D = .back, @ContentBuilder content: () -> Content)
```

## Parameters

- `sceneAnchor`: The anchor point for aligning the ornament’s content (based on the `contentAlignment`) with the scene.
- `contentAlignment`: The alignment in the ornament used to position it.
- `content`: The content of the ornament.

## See Also

### Creating a hosting ornament
- [var rootView: Content](./rootview.md)
  The root view of the SwiftUI view hierarchy managed by this ornament.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingornament/init(sceneanchor:contentalignment:content:))*