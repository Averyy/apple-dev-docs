# time

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The animation’s location within the timeline.

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
@preconcurrency var time: TimeInterval { get set }
```

## See Also

### Timing animation playback
- [var duration: TimeInterval](./duration.md)
  The length of time the animation spans, in seconds.
- [var speed: Float](./speed.md)
  The animation’s rate of playback.
- [var clock: CMClockOrTimebase](./clock.md)
  A reference clock to synchronize the animation with other events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller/time)*