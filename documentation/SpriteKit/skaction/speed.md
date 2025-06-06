# speed

**Framework**: SpriteKit  
**Kind**: property

A speed factor that modifies how fast an action runs.

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
var speed: CGFloat { get set }
```

## Mentions

- [Getting Started with Actions](getting-started-with-actions.md)

#### Discussion

The speed factor adjusts how fast an action’s animation runs. For example, a speed factor of `2.0` means the animation runs twice as fast.

## See Also

- [Configuring Action Timing](configuring-action-timing.md)
  Time an action in a scene, by adding or modifying timing properties, or cancel an action.
- [var duration: TimeInterval](skaction/duration.md)
  The duration required to complete an action.
- [var timingMode: SKActionTimingMode](skaction/timingmode.md)
  A setting that controls the speed curve of an animation.
- [enum SKActionTimingMode](skactiontimingmode.md)
  The modes that an action can use to adjust the apparent timing of the action.
- [var timingFunction: SKActionTimingFunction](skaction/timingfunction.md)
  A block used to customize the timing function.
- [typealias SKActionTimingFunction](skactiontimingfunction.md)
  The signature for the custom timing block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/speed)*