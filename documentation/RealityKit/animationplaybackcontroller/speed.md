# speed

**Framework**: RealityKit  
**Kind**: property

The animation’s rate of playback.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var speed: Float { get set }
```

#### Discussion

The animation applies the value of this property as an irrational factor of the unaltered speed. For example, a value of `2` plays the animation twice as fast, a value of `0.5` plays the animation at half speed, and a value of `1` plays the animation at the unaltered rate.

## See Also

- [var duration: TimeInterval](animationplaybackcontroller/duration.md)
  The length of time the animation spans, in seconds.
- [var clock: CMClockOrTimebase](animationplaybackcontroller/clock.md)
  A reference clock to synchronize the animation with other events.
- [var time: TimeInterval](animationplaybackcontroller/time.md)
  The animation’s location within the timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller/speed)*