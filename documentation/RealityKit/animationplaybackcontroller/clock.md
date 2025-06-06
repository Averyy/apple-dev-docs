# clock

**Framework**: RealityKit  
**Kind**: property

A reference clock to synchronize the animation with other events.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var clock: CMClockOrTimebase { get set }
```

## See Also

- [var duration: TimeInterval](animationplaybackcontroller/duration.md)
  The length of time the animation spans, in seconds.
- [var speed: Float](animationplaybackcontroller/speed.md)
  The animation’s rate of playback.
- [var time: TimeInterval](animationplaybackcontroller/time.md)
  The animation’s location within the timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller/clock)*