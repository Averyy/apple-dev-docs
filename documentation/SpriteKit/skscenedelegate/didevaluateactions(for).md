# didEvaluateActions(for:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Tells you to peform any necessary logic after scene actions are evaluated.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
optional func didEvaluateActions(for scene: SKScene)
```

```objc
- (void) didEvaluateActionsForScene:(SKScene *) scene;
```

## Mentions

- [Detecting Changes at Each Step of an Animation](../detecting-changes-at-each-step-of-an-animation.md)

## Discussion

Do not call this method directly; it is called by the system exactly once per frame, so long as the scene is presented in a view and is not paused. It is called after any actions have been evaluated by nodes in the scene but before any physics are simulated.

Any additional actions applied are not evaluated until the next update.

## Parameters

- `scene`: The scene that is being animated.

## See Also

### Handling Animation Events
- [Use SpriteKit Objects within Scene Delegate Callbacks](../use-spritekit-objects-within-scene-delegate-callbacks.md)
  Follow threading guidelines to keep your SpriteKit app thread safe.
- [func update(TimeInterval, for: SKScene)](./update%28_,for%29.md)
  Tells you to perform any app specific logic to update your scene.
- [func didSimulatePhysics(for: SKScene)](./didsimulatephysics%28for%29.md)
  Tells you to peform any necessary logic after physics simulations are performed.
- [func didApplyConstraints(for: SKScene)](./didapplyconstraints%28for%29.md)
  Tells you to peform any necessary logic after constraints are applied.
- [func didFinishUpdate(for: SKScene)](./didfinishupdate%28for%29.md)
  Tells you to peform any necessary logic after the scene has finished all of the steps required to process animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscenedelegate/didevaluateactions(for:))*