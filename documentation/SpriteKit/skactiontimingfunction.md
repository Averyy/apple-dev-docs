# SKActionTimingFunction

**Framework**: SpriteKit  
**Kind**: typealias

The signature for the custom timing block.

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
typealias SKActionTimingFunction = (Float) -> Float
```

#### Discussion

The block parameters are defined as follows:

The input value will be a value between `0.0` and `1.0`, inclusive. The block must also return a value between `0.0` and `1.0`. When the input time is `0.0`, the output value should be `0.0`. When the input time is `1.0`, the output value should also be `1.0`.

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
- [var speed: CGFloat](skaction/speed.md)
  A speed factor that modifies how fast an action runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skactiontimingfunction)*