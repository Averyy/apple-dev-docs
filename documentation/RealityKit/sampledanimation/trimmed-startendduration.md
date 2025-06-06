# trimmed(start:end:duration:)

**Framework**: RealityKit  
**Kind**: method

Edits the animation duration according to the specified time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
func trimmed(start: TimeInterval? = nil, end: TimeInterval? = nil, duration: TimeInterval? = nil) -> Self
```

#### Return Value

A version of the animation shortened or lengthened according to the specified times.

#### Discussion

If an argument property lies outside the underlying [`duration`](animationdefinition/duration.md), the animation plays back according to the characteristics of its [`repeatMode`](animationdefinition/repeatmode.md).

## Parameters

- `start`: The time within the underlying duration to begin playback.
- `end`: The time within the underlying duration to end playback.
- `duration`: The amount of time that overrides the underlying duration.

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
- [var trimDuration: TimeInterval?](sampledanimation/trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimStart: TimeInterval?](sampledanimation/trimstart.md)
  The optional time, in seconds, at which the animation plays.
- [var trimEnd: TimeInterval?](sampledanimation/trimend.md)
  The optional time, in seconds, at which the animation stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/trimmed(start:end:duration:))*