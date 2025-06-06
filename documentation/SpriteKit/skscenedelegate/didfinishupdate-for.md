# didFinishUpdate(for:)

**Framework**: SpriteKit  
**Kind**: method

Tells you to peform any necessary logic after the scene has finished all of the steps required to process animations.

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
optional func didFinishUpdate(for scene: SKScene)
```

#### Discussion

Do not call this method directly; it is called by the system exactly once per frame, so long as the scene is presented in a view and is not paused. It is called after all update logic has been completed and before the scene is rendered.

Any additional actions applied are not evaluated until the next update.

Any changes to physics bodies are not simulated until the next update.

Any changes to constraints will not be applied until the next update.

No further update logic will be applied to the scene after this call. Any values set on nodes here will be used when the scene is rendered for the current frame.

## Parameters

- `scene`: The scene that is being animated.

## See Also

- [Use SpriteKit Objects within Scene Delegate Callbacks](use-spritekit-objects-within-scene-delegate-callbacks.md)
  Follow threading guidelines to keep your SpriteKit app thread safe.
- [func update(TimeInterval, for: SKScene)](skscenedelegate/update(_:for:).md)
  Tells you to perform any app specific logic to update your scene.
- [func didEvaluateActions(for: SKScene)](skscenedelegate/didevaluateactions(for:).md)
  Tells you to peform any necessary logic after scene actions are evaluated.
- [func didSimulatePhysics(for: SKScene)](skscenedelegate/didsimulatephysics(for:).md)
  Tells you to peform any necessary logic after physics simulations are performed.
- [func didApplyConstraints(for: SKScene)](skscenedelegate/didapplyconstraints(for:).md)
  Tells you to peform any necessary logic after constraints are applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscenedelegate/didfinishupdate(for:))*