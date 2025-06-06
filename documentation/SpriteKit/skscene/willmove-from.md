# willMove(from:)

**Framework**: SpriteKit  
**Kind**: method

Tells you when the scene is about to be removed from a view.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func willMove(from view: SKView)
```

#### Discussion

This method is intended to be overridden in a subclass. You can use this method to implement any custom behavior for your scene when it is about to be removed from the view.

## Parameters

- `view`: The view that is presenting the scene.

## See Also

- [func sceneDidLoad()](skscene/scenedidload.md)
  Tells you when the scene is presented.
- [func didChangeSize(CGSize)](skscene/didchangesize(_:).md)
  Tells you when the scene’s size has changed.
- [func didMove(to: SKView)](skscene/didmove(to:).md)
  Tells you when the scene is presented by a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/willmove(from:))*