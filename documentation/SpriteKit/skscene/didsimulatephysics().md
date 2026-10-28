# didSimulatePhysics()

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Tells your app to peform any necessary logic after physics simulations are performed.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func didSimulatePhysics()
```

```objc
- (void) didSimulatePhysics;
```

## Mentions

- [Responding to Frame-Cycle Events](../responding-to-frame-cycle-events.md)

## Discussion

Do not call this method directly; it is called by the system exactly once per frame, so long as the scene is presented in a view and is not paused. It is called after physics has been simulated in the scene.

Any additional actions applied are not evaluated until the next update.

Any changes to physics bodies are not simulated until the next update.

## See Also

### Responding to Frame-Cycle Events
- [Responding to Frame-Cycle Events](../responding-to-frame-cycle-events.md)
  Implement per-frame app logic, such as the scene’s update function that’s called every frame.
- [func update(TimeInterval)](./update%28_%29.md)
  Tells your app to perform any app-specific logic to update your scene.
- [func didEvaluateActions()](./didevaluateactions%28%29.md)
  Tells your app to peform any necessary logic after scene actions are evaluated.
- [func didApplyConstraints()](./didapplyconstraints%28%29.md)
  Tells your app to peform any necessary logic after constraints are applied.
- [func didFinishUpdate()](./didfinishupdate%28%29.md)
  Tells your app to peform any necessary logic after the scene has finished all of the steps required to process animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/didsimulatephysics())*