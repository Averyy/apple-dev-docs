# trimStart

**Framework**: RealityKit  
**Kind**: property

The optional time, in seconds, at which the animation plays.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var trimStart: TimeInterval? { get set }
```

#### Discussion

This property is `nil` by default, which plays the animation from the starting frame defined by [`start`](sampledanimation/start.md).

If you set a value for this property, the animation visually begins from an additional seconds offset from the starting frame and decreases the duration by that amount.

If you set a negative value for this property, the duration increases and the additional animation data fills in based on the [`fillMode`](sampledanimation/fillmode.md) you choose.

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
- [var trimEnd: TimeInterval?](sampledanimation/trimend.md)
  The optional time, in seconds, at which the animation stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/trimstart)*