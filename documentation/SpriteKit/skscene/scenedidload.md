# sceneDidLoad()

**Framework**: SpriteKit  
**Kind**: method

Tells you when the scene is presented.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@MainActor
func sceneDidLoad()
```

## Mentions

- [Controlling User Interaction on Nodes](controlling-user-interaction-on-nodes.md)

#### Discussion

This method is intended to be overridden in a subclass. It is the preferred location to peform custom setup after the scene has been initialized or decoded.

## See Also

- [func didChangeSize(CGSize)](skscene/didchangesize(_:).md)
  Tells you when the scene’s size has changed.
- [func willMove(from: SKView)](skscene/willmove(from:).md)
  Tells you when the scene is about to be removed from a view.
- [func didMove(to: SKView)](skscene/didmove(to:).md)
  Tells you when the scene is presented by a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/scenedidload())*