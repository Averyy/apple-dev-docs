# delay

**Framework**: RealityKit  
**Kind**: property

An amount of time that lapses before the animation plays.

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

During the delayed time, the animation doesn’t update. However, to fill the delayed time with some portion of animation, set a negative [`trimStart`](orbitanimation/trimstart.md) instead and choose a [`fillMode`](orbitanimation/fillmode.md) that displays the desired portion of animation.

## See Also

- [var speed: Float](orbitanimation/speed.md)
  A factor that changes the animation’s rate of playback.
- [var duration: TimeInterval](orbitanimation/duration.md)
  The elapsed time for one complete rotation.
- [var offset: TimeInterval](orbitanimation/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var trimDuration: TimeInterval?](orbitanimation/trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimStart: TimeInterval?](orbitanimation/trimstart.md)
  The optional time, in seconds, at which the animation plays.
- [var trimEnd: TimeInterval?](orbitanimation/trimend.md)
  The optional time, in seconds, at which the animation stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/orbitanimation/delay)*