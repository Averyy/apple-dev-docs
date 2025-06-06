# speed

**Framework**: RealityKit  
**Kind**: property

A factor that increases or decreases the animation’s rate of playback.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
var speed: Float { get set }
```

#### Discussion

The default value is `1.0`, which doesn’t alter the animation’s rate of playback. A value of `2.0` plays the animation at twice the normal rate, and a speed of `0.5` makes the animation finish after twice the normal time. A negative value plays the animation in reverse.

This property doesn’t affect the animation’s [`delay`](fromtobyanimation/delay.md).

## See Also

- [var delay: TimeInterval](blendtreeanimation/delay.md)
  An amount of time that lapses before the animation plays.
- [var duration: TimeInterval](blendtreeanimation/duration.md)
  The total playback time of the animation.
- [var offset: TimeInterval](blendtreeanimation/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var trimDuration: TimeInterval?](blendtreeanimation/trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimStart: TimeInterval?](blendtreeanimation/trimstart.md)
  The optional time, in seconds, at which the source animation plays.
- [var trimEnd: TimeInterval?](blendtreeanimation/trimend.md)
  The optional time, in seconds, at which the source animation stops.
- [func trimmed(start: TimeInterval?, end: TimeInterval?, duration: TimeInterval?) -> Self](blendtreeanimation/trimmed(start:end:duration:).md)
  Edits the animation duration according to the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendtreeanimation/speed)*