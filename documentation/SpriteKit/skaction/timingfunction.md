# timingFunction

**Framework**: SpriteKit  
**Kind**: property

A block used to customize the timing function.

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
var timingFunction: SKActionTimingFunction { get set }
```

## Mentions

- [Getting Started with Actions](getting-started-with-actions.md)
- [Configuring Action Timing](configuring-action-timing.md)

#### Discussion

If a timing function is provided, after the normal timing mode is applied, the result is sent to the timing function. The return [`SKActionTimingFunction`](skactiontimingfunction.md) value of the timing function determines the actual time used to perform the animation.

The following code shows how you can create a custom timing function using [`simd_smoothstep(_:_:_:)`](https://developer.apple.com/documentation/simd/simd_smoothstep(_:_:_:)-5839l) interpolation:

```swift
import simd
let horizontalAction = SKAction.moveTo(x: end.x, duration: 2.0)
horizontalAction.timingFunction = {
    time in
    return simd_smoothstep(0, 1, time)
}
```

If the above code is combined with a vertical linear move action, the path taken by a node running this action describes the curve illustrated below:

![Smoothstep based motion path](https://docs-assets.developer.apple.com/published/abd62c141bd21009f0f394fcd2d3ea57/media-2759776%402x.png)

## See Also

- [Configuring Action Timing](configuring-action-timing.md)
  Time an action in a scene, by adding or modifying timing properties, or cancel an action.
- [var duration: TimeInterval](skaction/duration.md)
  The duration required to complete an action.
- [var timingMode: SKActionTimingMode](skaction/timingmode.md)
  A setting that controls the speed curve of an animation.
- [enum SKActionTimingMode](skactiontimingmode.md)
  The modes that an action can use to adjust the apparent timing of the action.
- [typealias SKActionTimingFunction](skactiontimingfunction.md)
  The signature for the custom timing block.
- [var speed: CGFloat](skaction/speed.md)
  A speed factor that modifies how fast an action runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/timingfunction)*