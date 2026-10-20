# frameInterval

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The duration within the animation timeline for each frame in the frames array.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
var frameInterval: Float { get set }
```

## See Also

### Timing the animation
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
- [var trimDuration: TimeInterval?](./trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimStart: TimeInterval?](./trimstart.md)
  The optional time, in seconds, at which the animation plays.
- [var trimEnd: TimeInterval?](./trimend.md)
  The optional time, in seconds, at which the animation stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/frameinterval)*