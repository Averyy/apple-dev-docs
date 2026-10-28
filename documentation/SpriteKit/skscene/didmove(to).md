# didMove(to:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Tells you when the scene is presented by a view.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func didMove(to view: SKView)
```

```objc
- (void) didMoveToView:(SKView *) view;
```

## Discussion

This method is intended to be overridden in a subclass. You can use this method to implement any custom behavior for your scene when it is about to be presented by a view. For example, you might use this method to create the scene’s contents.

## Parameters

- `view`: The view that is presenting the scene.

## See Also

### Responding to Loading and Resizing Events
- [func sceneDidLoad()](./scenedidload%28%29.md)
  Tells you when the scene is presented.
- [func didChangeSize(CGSize)](./didchangesize%28_%29.md)
  Tells you when the scene’s size has changed.
- [func willMove(from: SKView)](./willmove%28from%29.md)
  Tells you when the scene is about to be removed from a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/didmove(to:))*