# removeAnchor(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified anchor from the scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func removeAnchor(_ anchor: any HasAnchoring)
```

## Parameters

- `anchor`: The anchor to remove.

## See Also

### Adding and removing anchors
- [var anchors: Scene.AnchorCollection](./anchors.md)
  The collection of anchors contained in the scene.
- [func addAnchor(any HasAnchoring)](./addanchor%28_%29.md)
  Adds an anchor to the scene’s list of anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/removeanchor(_:))*