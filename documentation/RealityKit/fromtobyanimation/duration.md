# duration

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The total playback time of the animation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
var duration: TimeInterval { get set }
```

## Discussion

The framework sets a value for this property depending on the underlying animation data and the specified [`speed`](../animationview/speed.md).

You can override the default duration by defining [`trimStart`](./trimstart.md), [`trimEnd`](./trimend.md), or [`trimDuration`](./trimduration.md).

## See Also

### Timing the animation
- [var speed: Float](./speed.md)
  A factor that increases or decreases the animation’s rate of playback.
- [var delay: TimeInterval](./delay.md)
  An amount of time that elapses before the animation plays.
- [var offset: TimeInterval](./offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var timing: AnimationTimingFunction](./timing.md)
  An option that determines the animation’s pace over time.
- [var trimDuration: TimeInterval?](./trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimStart: TimeInterval?](./trimstart.md)
  The time, in seconds, at which the animation plays.
- [var trimEnd: TimeInterval?](./trimend.md)
  The time, in seconds, at which the animation stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyanimation/duration)*