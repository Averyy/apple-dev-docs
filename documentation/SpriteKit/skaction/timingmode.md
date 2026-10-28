# timingMode

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A setting that controls the speed curve of an animation.

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
var timingMode: SKActionTimingMode { get set }
```

```objc
@property (nonatomic) SKActionTimingMode timingMode;
```

## Mentions

- [Configuring Action Timing](../configuring-action-timing.md)
- [Getting Started with Actions](../getting-started-with-actions.md)

## Discussion

The possible values for this property are listed in [`SKActionTimingMode`](../skactiontimingmode.md). The default value is [`SKActionTimingMode.linear`](../skactiontimingmode/linear.md).

## See Also

### Controlling Action Timing
- [Configuring Action Timing](../configuring-action-timing.md)
  Time an action in a scene, by adding or modifying timing properties, or cancel an action.
- [var duration: TimeInterval](./duration.md)
  The duration required to complete an action.
- [enum SKActionTimingMode](../skactiontimingmode.md)
  The modes that an action can use to adjust the apparent timing of the action.
- [var timingFunction: SKActionTimingFunction](./timingfunction.md)
  A block used to customize the timing function.
- [typealias SKActionTimingFunction](../skactiontimingfunction.md)
  The signature for the custom timing block.
- [var speed: CGFloat](./speed.md)
  A speed factor that modifies how fast an action runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/timingmode)*