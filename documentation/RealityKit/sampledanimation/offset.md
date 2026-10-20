# offset

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The time, in seconds, at which the animation begins within the duration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
var offset: TimeInterval { get set }
```

#### Discussion

The default value is `0`, which indicates that the animation plays with no offset. Setting a value for this property moves the animation data along the timeline and doesn’t change timing. If you set a [`fillMode`](./fillmode.md) other than [`none`](../animationfillmode/none.md), the animation fills the vacant area created by the offset according to the characteristics of the specified fill mode.

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
- [var trimDuration: TimeInterval?](./trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimStart: TimeInterval?](./trimstart.md)
  The optional time, in seconds, at which the animation plays.
- [var trimEnd: TimeInterval?](./trimend.md)
  The optional time, in seconds, at which the animation stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/offset)*