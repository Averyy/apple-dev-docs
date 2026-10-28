# willMove(from:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Tells you when the scene is about to be removed from a view.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func willMove(from view: SKView)
```

```objc
- (void) willMoveFromView:(SKView *) view;
```

## Discussion

This method is intended to be overridden in a subclass. You can use this method to implement any custom behavior for your scene when it is about to be removed from the view.

## Parameters

- `view`: The view that is presenting the scene.

## See Also

### Responding to Loading and Resizing Events
- [func sceneDidLoad()](./scenedidload%28%29.md)
  Tells you when the scene is presented.
- [func didChangeSize(CGSize)](./didchangesize%28_%29.md)
  Tells you when the scene’s size has changed.
- [func didMove(to: SKView)](./didmove%28to%29.md)
  Tells you when the scene is presented by a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/willmove(from:))*