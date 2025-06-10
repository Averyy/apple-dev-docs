# didEvaluateActions()

**Framework**: SpriteKit  
**Kind**: method

Tells your app to peform any necessary logic after scene actions are evaluated.

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
@MainActor
func didEvaluateActions()
```

## Mentions

- [Responding to Frame-Cycle Events](responding-to-frame-cycle-events.md)

#### Discussion

Do not call this method directly; it is called by the system exactly once per frame, so long as the scene is presented in a view and is not paused. It is called after any actions have been evaluated by nodes in the scene but before any physics are simulated.

Any additional actions applied are not evaluated until the next update.

## See Also

- [Responding to Frame-Cycle Events](responding-to-frame-cycle-events.md)
  Implement per-frame app logic, such as the scene’s update function that’s called every frame.
- [func update(TimeInterval)](skscene/update(_:).md)
  Tells your app to perform any app-specific logic to update your scene.
- [func didSimulatePhysics()](skscene/didsimulatephysics.md)
  Tells your app to peform any necessary logic after physics simulations are performed.
- [func didApplyConstraints()](skscene/didapplyconstraints.md)
  Tells your app to peform any necessary logic after constraints are applied.
- [func didFinishUpdate()](skscene/didfinishupdate.md)
  Tells your app to peform any necessary logic after the scene has finished all of the steps required to process animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/didevaluateactions())*