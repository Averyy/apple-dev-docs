# trimEnd

**Framework**: RealityKit  
**Kind**: property

The time, in seconds, at which the animation stops.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var trimEnd: TimeInterval? { get set }
```

#### Discussion

This property is `nil` by default, which plays the animation until `time` = [`duration`](fromtobyanimation/duration.md). If you set a value, the animation edits the duration according to the specified ending time.

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
- [var trimStart: TimeInterval?](fromtobyanimation/trimstart.md)
  The time, in seconds, at which the animation plays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyanimation/trimend)*