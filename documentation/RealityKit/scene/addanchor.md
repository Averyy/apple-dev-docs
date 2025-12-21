# addAnchor(_:)

**Framework**: RealityKit  
**Kind**: method

Adds an anchor to the scene’s list of anchors.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func addAnchor(_ anchor: any HasAnchoring)
```

## Parameters

- `anchor`: The anchor to add.

## See Also

- [var anchors: Scene.AnchorCollection](scene/anchors.md)
  The collection of anchors contained in the scene.
- [func removeAnchor(any HasAnchoring)](scene/removeanchor(_:).md)
  Removes the specified anchor from the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/addanchor(_:))*