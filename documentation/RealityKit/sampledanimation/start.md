# start

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

An integer multiple of the frame interval at which the animation plays.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
var start: TimeInterval { get set }
```

#### Discussion

When calculating the visual beginning of a sampled animation, the framework first evaluates this property, and then applies the optional [`trimStart`](./trimstart.md), in seconds.

The framework requires this property to contain an integer multiple of [`frameInterval`](./frameinterval.md). Note that the value of this property can be irrational because frame interval is of type [`TimeInterval`](../../Foundation/timeinterval.md).

## See Also

### Timing the animation
- [var frameInterval: Float](./frameinterval.md)
  The duration within the animation timeline for each frame in the frames array.
- [var end: TimeInterval](./end.md)
  An integer multiple of the frame interval at which the animation stops.
- [var speed: Float](./speed.md)
  A factor that changes the animation’s rate of playback.
- [var delay: TimeInterval](./delay.md)
  An amount of time that elapses before the animation plays.
- [var duration: TimeInterval](./duration.md)
  The total playback time of the animation.
- [var offset: TimeInterval](./offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var trimDuration: TimeInterval?](./trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimStart: TimeInterval?](./trimstart.md)
  The optional time, in seconds, at which the animation plays.
- [var trimEnd: TimeInterval?](./trimend.md)
  The optional time, in seconds, at which the animation stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/start)*