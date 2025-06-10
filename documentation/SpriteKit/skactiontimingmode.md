# SKActionTimingMode

**Framework**: SpriteKit  
**Kind**: enum

The modes that an action can use to adjust the apparent timing of the action.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum SKActionTimingMode
```

## Mentions

- [Configuring Action Timing](configuring-action-timing.md)

## Topics

### Constants
- [SKActionTimingMode.linear](skactiontimingmode/linear.md)
  Specifies linear pacing. Linear pacing causes an animation to occur evenly over its duration.
- [SKActionTimingMode.easeIn](skactiontimingmode/easein.md)
  Specifies ease-in pacing. Ease-in pacing causes the animation to begin slowly and then speed up as it progresses.
- [SKActionTimingMode.easeOut](skactiontimingmode/easeout.md)
  Specifies ease-out pacing. Ease-out pacing causes the animation to begin quickly and then slow as it completes.
- [SKActionTimingMode.easeInEaseOut](skactiontimingmode/easeineaseout.md)
  Specifies ease-in ease-out pacing. An ease-in ease-out animation begins slowly, accelerates through the middle of its duration, and then slows again before completing.
### Initializers
- [init?(rawValue: Int)](skactiontimingmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Configuring Action Timing](configuring-action-timing.md)
  Time an action in a scene, by adding or modifying timing properties, or cancel an action.
- [var duration: TimeInterval](skaction/duration.md)
  The duration required to complete an action.
- [var timingMode: SKActionTimingMode](skaction/timingmode.md)
  A setting that controls the speed curve of an animation.
- [var timingFunction: SKActionTimingFunction](skaction/timingfunction.md)
  A block used to customize the timing function.
- [typealias SKActionTimingFunction](skactiontimingfunction.md)
  The signature for the custom timing block.
- [var speed: CGFloat](skaction/speed.md)
  A speed factor that modifies how fast an action runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skactiontimingmode)*