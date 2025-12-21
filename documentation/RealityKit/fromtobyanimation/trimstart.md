# trimStart

**Framework**: RealityKit  
**Kind**: property

The time, in seconds, at which the animation plays.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var trimStart: TimeInterval? { get set }
```

#### Discussion

This property is `nil` by default, which plays the animation with `time` = `0`. If you set a value, the animation edits the duration according to the specified beginning time.

If you set a negative value for this property, the duration increases and the additional animation data fills in based on the [`fillMode`](fromtobyanimation/fillmode.md) you choose.

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
- [var trimDuration: TimeInterval?](fromtobyanimation/trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimEnd: TimeInterval?](fromtobyanimation/trimend.md)
  The time, in seconds, at which the animation stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyanimation/trimstart)*