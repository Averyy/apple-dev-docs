# duration

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The duration required to complete an action.

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
var duration: TimeInterval { get set }
```

```objc
@property (nonatomic) NSTimeInterval duration;
```

## Mentions

- [Getting Started with Actions](../getting-started-with-actions.md)

#### Discussion

This is the expected duration of an action’s animation. The actual time an action takes to complete is modified by the [`speed`](./speed.md) property of the action and the [`speed`](../sknode/speed.md) property of the node on which it executes.

## See Also

### Controlling Action Timing
- [Configuring Action Timing](../configuring-action-timing.md)
  Time an action in a scene, by adding or modifying timing properties, or cancel an action.
- [var timingMode: SKActionTimingMode](./timingmode.md)
  A setting that controls the speed curve of an animation.
- [enum SKActionTimingMode](../skactiontimingmode.md)
  The modes that an action can use to adjust the apparent timing of the action.
- [var timingFunction: SKActionTimingFunction](./timingfunction.md)
  A block used to customize the timing function.
- [typealias SKActionTimingFunction](../skactiontimingfunction.md)
  The signature for the custom timing block.
- [var speed: CGFloat](./speed.md)
  A speed factor that modifies how fast an action runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/duration)*