# timing

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

An option that determines the animation’s pace over time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
var timing: AnimationTimingFunction { get set }
```

## Discussion

Depending on the option you pick, the animation’s progress moves at varying speeds along its duration.

## See Also

### Timing the animation
- [var speed: Float](./speed.md)
  A factor that increases or decreases the animation’s rate of playback.
- [var delay: TimeInterval](./delay.md)
  An amount of time that elapses before the animation plays.
- [var duration: TimeInterval](./duration.md)
  The total playback time of the animation.
- [var offset: TimeInterval](./offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var trimDuration: TimeInterval?](./trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimStart: TimeInterval?](./trimstart.md)
  The time, in seconds, at which the animation plays.
- [var trimEnd: TimeInterval?](./trimend.md)
  The time, in seconds, at which the animation stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyanimation/timing)*