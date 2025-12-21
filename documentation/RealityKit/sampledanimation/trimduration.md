# trimDuration

**Framework**: RealityKit  
**Kind**: property

An optional duration that overrides the calculated duration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var trimDuration: TimeInterval? { get set }
```

#### Discussion

This property is `nil` by default, which indicates that the animation stops after one play that spans [`duration`](sampledanimation/duration.md).

If you set a non-zero value for this property and both [`trimStart`](sampledanimation/trimstart.md) and [`trimEnd`](sampledanimation/trimend.md) are `nil`, the animation observes this property as an edited duration.

When you set [`repeatMode`](sampledanimation/repeatmode.md) to make the animation repeat:

- If this property is `nil`, the animation repeats forever.
- If set to a value greater than [`duration`](sampledanimation/duration.md), the animation repeats for the specified duration.

## See Also

- [var frameInterval: Float](sampledanimation/frameinterval.md)
  The duration within the animation timeline for each frame in the frames array.
- [var start: TimeInterval](sampledanimation/start.md)
  An integer multiple of the frame interval at which the animation plays.
- [var end: TimeInterval](sampledanimation/end.md)
  An integer multiple of the frame interval at which the animation stops.
- [var speed: Float](sampledanimation/speed.md)
  A factor that changes the animation’s rate of playback.
- [var delay: TimeInterval](sampledanimation/delay.md)
  An amount of time that elapses before the animation plays.
- [var duration: TimeInterval](sampledanimation/duration.md)
  The total playback time of the animation.
- [var offset: TimeInterval](sampledanimation/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var trimStart: TimeInterval?](sampledanimation/trimstart.md)
  The optional time, in seconds, at which the animation plays.
- [var trimEnd: TimeInterval?](sampledanimation/trimend.md)
  The optional time, in seconds, at which the animation stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/trimduration)*