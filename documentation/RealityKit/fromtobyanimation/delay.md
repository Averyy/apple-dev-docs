# delay

**Framework**: RealityKit  
**Kind**: property

An amount of time that elapses before the animation plays.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var delay: TimeInterval { get set }
```

#### Discussion

The default value is `0`, which indicates that the animation plays with no delay. If you set a value for this property, the animation plays from its start time after the specified delay lapses.

During the delayed time, the animation doesn’t update. However, to fill the delayed time with some portion of animation, set a negative [`trimStart`](fromtobyanimation/trimstart.md) instead and choose a [`fillMode`](fromtobyanimation/fillmode.md) that displays the desired portion of animation.

## See Also

- [var speed: Float](fromtobyanimation/speed.md)
  A factor that increases or decreases the animation’s rate of playback.
- [var duration: TimeInterval](fromtobyanimation/duration.md)
  The total playback time of the animation.
- [var offset: TimeInterval](fromtobyanimation/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var timing: AnimationTimingFunction](fromtobyanimation/timing.md)
  An option that determines the animation’s pace over time.
- [var trimDuration: TimeInterval?](fromtobyanimation/trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimStart: TimeInterval?](fromtobyanimation/trimstart.md)
  The time, in seconds, at which the animation plays.
- [var trimEnd: TimeInterval?](fromtobyanimation/trimend.md)
  The time, in seconds, at which the animation stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyanimation/delay)*