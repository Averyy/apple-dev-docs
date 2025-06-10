# duration

**Framework**: RealityKit  
**Kind**: property

The elapsed time for one complete rotation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var duration: TimeInterval { get set }
```

#### Discussion

The framework sets a value for this property depending on the underlying animation data and the specified [`speed`](orbitanimation/speed.md).

You can override the default duration by defining [`trimStart`](orbitanimation/trimstart.md), [`trimEnd`](orbitanimation/trimend.md), or [`trimDuration`](orbitanimation/trimduration.md).

## See Also

- [var speed: Float](orbitanimation/speed.md)
  A factor that changes the animation’s rate of playback.
- [var delay: TimeInterval](orbitanimation/delay.md)
  An amount of time that lapses before the animation plays.
- [var offset: TimeInterval](orbitanimation/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var trimDuration: TimeInterval?](orbitanimation/trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimStart: TimeInterval?](orbitanimation/trimstart.md)
  The optional time, in seconds, at which the animation plays.
- [var trimEnd: TimeInterval?](orbitanimation/trimend.md)
  The optional time, in seconds, at which the animation stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/orbitanimation/duration)*