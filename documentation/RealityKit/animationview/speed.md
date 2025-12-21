# speed

**Framework**: RealityKit  
**Kind**: property

A factor that increases or decreases the animation’s rate of playback.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var speed: Float { get set }
```

#### Discussion

The default value is `1.0`, which doesn’t alter the animation’s duration. A value of `2.0` indicates that the duration is half the underlying setting. A value of `0.5` indicates that the duration is twice the underlying setting. Negative values play the animation in reverse.

This property doesn’t affect the animation’s [`delay`](animationview/delay.md).

## See Also

- [var delay: TimeInterval](animationview/delay.md)
  An amount of time that lapses before the animation plays.
- [var duration: TimeInterval](animationview/duration.md)
  The total playback time of the animation.
- [var offset: TimeInterval](animationview/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var trimDuration: TimeInterval?](animationview/trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimStart: TimeInterval?](animationview/trimstart.md)
  The time, in seconds, at which the source animation plays.
- [var trimEnd: TimeInterval?](animationview/trimend.md)
  The time, in seconds, at which the source animation stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationview/speed)*