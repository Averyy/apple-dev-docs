# didApplyConstraints()

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Tells your app to peform any necessary logic after constraints are applied.

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
func didApplyConstraints()
```

```objc
- (void) didApplyConstraints;
```

## Mentions

- [Responding to Frame-Cycle Events](../responding-to-frame-cycle-events.md)

## Discussion

Do not call this method directly; it is called exactly once per frame, so long as the scene is presented in a view and is not paused. By default, this method does nothing. Your scene subclass should override this method and perform any necessary updates to the scene.

## See Also

### Responding to Frame-Cycle Events
- [Responding to Frame-Cycle Events](../responding-to-frame-cycle-events.md)
  Implement per-frame app logic, such as the scene’s update function that’s called every frame.
- [func update(TimeInterval)](./update%28_%29.md)
  Tells your app to perform any app-specific logic to update your scene.
- [func didEvaluateActions()](./didevaluateactions%28%29.md)
  Tells your app to peform any necessary logic after scene actions are evaluated.
- [func didSimulatePhysics()](./didsimulatephysics%28%29.md)
  Tells your app to peform any necessary logic after physics simulations are performed.
- [func didFinishUpdate()](./didfinishupdate%28%29.md)
  Tells your app to peform any necessary logic after the scene has finished all of the steps required to process animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/didapplyconstraints())*