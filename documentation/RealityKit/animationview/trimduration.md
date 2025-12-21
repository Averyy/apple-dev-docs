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

The framework calculates [`duration`](animationview/duration.md), but you can set this property to override it. This property is `nil` by default, which indicates that the animation stops after one play that spans [`duration`](animationview/duration.md).

If you set a non-zero value for this property and both [`trimStart`](animationview/trimstart.md) and [`trimEnd`](animationview/trimend.md) are `nil`, the animation observes this property as an edited duration.

When you set [`repeatMode`](animationview/repeatmode.md) to make the animation repeat:

- If this property is `nil`, the animation repeats forever.
- If set to a value greater than [`duration`](animationview/duration.md), the animation repeats for the specified duration.

## See Also

- [var speed: Float](animationview/speed.md)
  A factor that increases or decreases the animation’s rate of playback.
- [var delay: TimeInterval](animationview/delay.md)
  An amount of time that lapses before the animation plays.
- [var duration: TimeInterval](animationview/duration.md)
  The total playback time of the animation.
- [var offset: TimeInterval](animationview/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var trimStart: TimeInterval?](animationview/trimstart.md)
  The time, in seconds, at which the source animation plays.
- [var trimEnd: TimeInterval?](animationview/trimend.md)
  The time, in seconds, at which the source animation stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationview/trimduration)*