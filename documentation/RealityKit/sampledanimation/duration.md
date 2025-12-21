# duration

**Framework**: RealityKit  
**Kind**: property

The total playback time of the animation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var duration: TimeInterval { get set }
```

#### Discussion

The framework sets a value for this property depending on the underlying animation data and the specified [`speed`](sampledanimation/speed.md).

You can override the default duration by defining [`trimStart`](sampledanimation/trimstart.md), [`trimEnd`](sampledanimation/trimend.md), or [`trimDuration`](sampledanimation/trimduration.md).

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
- [var offset: TimeInterval](sampledanimation/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var trimDuration: TimeInterval?](sampledanimation/trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimStart: TimeInterval?](sampledanimation/trimstart.md)
  The optional time, in seconds, at which the animation plays.
- [var trimEnd: TimeInterval?](sampledanimation/trimend.md)
  The optional time, in seconds, at which the animation stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/duration)*