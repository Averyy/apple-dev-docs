# trimDuration

**Framework**: RealityKit  
**Kind**: property

An optional duration that overrides the calculated duration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var trimDuration: TimeInterval? { get set }
```

#### Discussion

The framework calculates [`duration`](fromtobyanimation/duration.md), but you can set this property to override it. This property is `nil` by default, which indicates that the animation stops after one play that spans [`duration`](fromtobyanimation/duration.md).

If you set a value for this property and both [`trimStart`](fromtobyanimation/trimstart.md) and [`trimEnd`](fromtobyanimation/trimend.md) are `nil`, the animation observes this property as an edited duration.

A value greater than [`duration`](fromtobyanimation/duration.md) causes the animation to repeat, applying the characteristics defined by [`repeatMode`](fromtobyanimation/repeatmode.md). Assign this property [`greatestFiniteMagnitude`](https://developer.apple.com/documentation/Swift/Double/greatestFiniteMagnitude) to repeat indefinitely.

## See Also

- [var speed: Float](fromtobyanimation/speed.md)
  A factor that increases or decreases the animation’s rate of playback.
- [var delay: TimeInterval](fromtobyanimation/delay.md)
  An amount of time that elapses before the animation plays.
- [var duration: TimeInterval](fromtobyanimation/duration.md)
  The total playback time of the animation.
- [var offset: TimeInterval](fromtobyanimation/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var timing: AnimationTimingFunction](fromtobyanimation/timing.md)
  An option that determines the animation’s pace over time.
- [var trimStart: TimeInterval?](fromtobyanimation/trimstart.md)
  The time, in seconds, at which the animation plays.
- [var trimEnd: TimeInterval?](fromtobyanimation/trimend.md)
  The time, in seconds, at which the animation stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyanimation/trimduration)*