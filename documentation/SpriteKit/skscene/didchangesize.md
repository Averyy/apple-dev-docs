# didChangeSize(_:)

**Framework**: SpriteKit  
**Kind**: method

Tells you when the scene’s size has changed.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func didChangeSize(_ oldSize: CGSize)
```

## Mentions

- [Scaling a Scene’s Content to Fit the View](scaling-a-scene-s-content-to-fit-the-view.md)

#### Discussion

This method is intended to be overridden in a subclass. Typically, you use this method to adjust the positions of nodes in the scene.

## Parameters

- `oldSize`: The old size of the scene, in points.

## See Also

- [func sceneDidLoad()](skscene/scenedidload.md)
  Tells you when the scene is presented.
- [func willMove(from: SKView)](skscene/willmove(from:).md)
  Tells you when the scene is about to be removed from a view.
- [func didMove(to: SKView)](skscene/didmove(to:).md)
  Tells you when the scene is presented by a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/didchangesize(_:))*