# trimDuration

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

An optional duration that overrides the calculated duration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
var trimDuration: TimeInterval? { get set }
```

#### Discussion

This property is `nil` by default, which indicates that the animation stops after one play that spans [`duration`](./duration.md).

If you set a non-zero value for this property and both [`trimStart`](./trimstart.md) and [`trimEnd`](./trimend.md) are `nil`, the animation observes this property as an edited duration.

When you set [`repeatMode`](./repeatmode.md) to make the animation repeat:

- If this property is `nil`, the animation repeats forever.
- If set to a value greater than [`duration`](./duration.md), the animation repeats for the specified duration.

## See Also

### Timing the animation
- [var frameInterval: Float](./frameinterval.md)
  The duration within the animation timeline for each frame in the frames array.
- [var start: TimeInterval](./start.md)
  An integer multiple of the frame interval at which the animation plays.
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
- [var trimStart: TimeInterval?](./trimstart.md)
  The optional time, in seconds, at which the animation plays.
- [var trimEnd: TimeInterval?](./trimend.md)
  The optional time, in seconds, at which the animation stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/trimduration)*