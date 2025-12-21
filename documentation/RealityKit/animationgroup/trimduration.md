# trimDuration

**Framework**: RealityKit  
**Kind**: property

An optional duration that overrides the calculated duration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var trimDuration: TimeInterval? { get set }
```

#### Discussion

The framework calculates [`duration`](fromtobyanimation/duration.md), but you can set this property to override it. This property is `nil` by default, which indicates that the animation stops after one play that spans [`duration`](animationgroup/duration.md).

If you set a non-zero value for this property and both [`trimStart`](animationgroup/trimstart.md) and [`trimEnd`](animationgroup/trimend.md) are `nil`, the animation observes this property as an edited duration.

When you set [`repeatMode`](animationgroup/repeatmode.md) to make the animation repeat:

- If this property is `nil`, the animation repeats forever.
- If set to a value greater than [`duration`](animationgroup/duration.md), the animation repeats for the specified duration.

## See Also

- [var speed: Float](animationgroup/speed.md)
  A factor that increases or decreases the animation’s rate of playback.
- [var delay: TimeInterval](animationgroup/delay.md)
  An amount of time that lapses before the animation plays.
- [var duration: TimeInterval](animationgroup/duration.md)
  The total playback time of the animation.
- [var offset: TimeInterval](animationgroup/offset.md)
  The time, in seconds, at which the animations begin within the duration.
- [var trimStart: TimeInterval?](animationgroup/trimstart.md)
  The time, in seconds, at which the animations play.
- [var trimEnd: TimeInterval?](animationgroup/trimend.md)
  The time, in seconds, at which the animations stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgroup/trimduration)*