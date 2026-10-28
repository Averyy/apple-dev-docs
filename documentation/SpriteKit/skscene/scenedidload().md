# sceneDidLoad()

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

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
func sceneDidLoad()
```

```objc
- (void) sceneDidLoad;
```

## Mentions

- [Controlling User Interaction on Nodes](../controlling-user-interaction-on-nodes.md)

## Discussion

This method is intended to be overridden in a subclass. It is the preferred location to peform custom setup after the scene has been initialized or decoded.

## See Also

### Responding to Loading and Resizing Events
- [func didChangeSize(CGSize)](./didchangesize%28_%29.md)
  Tells you when the scene’s size has changed.
- [func willMove(from: SKView)](./willmove%28from%29.md)
  Tells you when the scene is about to be removed from a view.
- [func didMove(to: SKView)](./didmove%28to%29.md)
  Tells you when the scene is presented by a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/scenedidload())*