# delay

**Framework**: RealityKit  
**Kind**: property

An amount of time that elapses before the animation plays.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var delay: TimeInterval { get set }
```

#### Discussion

The default value is `0`, which indicates that the animation plays with no delay. If you set a value for this property, the animation plays from its start time after the specified delay lapses.

During the delayed time, the animation doesn’t update. However, to fill the delayed time with some portion of animation, set a negative [`trimStart`](sampledanimation/trimstart.md) instead and choose a [`fillMode`](sampledanimation/fillmode.md) that displays the desired portion of animation.

## See Also

- [var frameInterval: Float](sampledanimation/frameinterval.md)
  The duration within the animation timeline for each frame in the frames array.
- [var start: TimeInterval](sampledanimation/start.md)
  An integer multiple of the frame interval at which the animation plays.
- [var end: TimeInterval](sampledanimation/end.md)
  An integer multiple of the frame interval at which the animation stops.
- [var speed: Float](sampledanimation/speed.md)
  A factor that changes the animation’s rate of playback.
- [var duration: TimeInterval](sampledanimation/duration.md)
  The total playback time of the animation.
- [var offset: TimeInterval](sampledanimation/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var trimDuration: TimeInterval?](sampledanimation/trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimStart: TimeInterval?](sampledanimation/trimstart.md)
  The optional time, in seconds, at which the animation plays.
- [var trimEnd: TimeInterval?](sampledanimation/trimend.md)
  The optional time, in seconds, at which the animation stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/delay)*