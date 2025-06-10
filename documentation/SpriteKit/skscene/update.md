# update(_:)

**Framework**: SpriteKit  
**Kind**: method

Tells your app to perform any app-specific logic to update your scene.

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
func update(_ currentTime: TimeInterval)
```

## Mentions

- [Responding to Frame-Cycle Events](responding-to-frame-cycle-events.md)
- [Getting Started with Actions](getting-started-with-actions.md)

#### Discussion

Do not call this method directly; it is called by the system exactly once per frame, so long as the scene is presented in a view and is not paused. This is the first method called when animating the scene, before any actions are evaluated and before any physics are simulated.

## Parameters

- `currentTime`: The current system time.

## See Also

- [Responding to Frame-Cycle Events](responding-to-frame-cycle-events.md)
  Implement per-frame app logic, such as the scene’s update function that’s called every frame.
- [func didEvaluateActions()](skscene/didevaluateactions.md)
  Tells your app to peform any necessary logic after scene actions are evaluated.
- [func didSimulatePhysics()](skscene/didsimulatephysics.md)
  Tells your app to peform any necessary logic after physics simulations are performed.
- [func didApplyConstraints()](skscene/didapplyconstraints.md)
  Tells your app to peform any necessary logic after constraints are applied.
- [func didFinishUpdate()](skscene/didfinishupdate.md)
  Tells your app to peform any necessary logic after the scene has finished all of the steps required to process animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/update(_:))*