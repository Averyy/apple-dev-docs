# clock

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

A reference clock to synchronize the animation with other events.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency var clock: CMClockOrTimebase { get set }
```

## See Also

### Timing animation playback
- [var duration: TimeInterval](./duration.md)
  The length of time the animation spans, in seconds.
- [var speed: Float](./speed.md)
  The animation’s rate of playback.
- [var time: TimeInterval](./time.md)
  The animation’s location within the timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller/clock)*