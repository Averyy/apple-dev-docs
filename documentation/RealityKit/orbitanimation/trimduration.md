# trimDuration

**Framework**: RealityKit  
**Kind**: property

An optional duration that overrides the calculated duration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var trimDuration: TimeInterval? { get set }
```

#### Discussion

The framework calculates [`duration`](orbitanimation/duration.md), but you can set this property to override it. This property is `nil` by default, which indicates that the animation stops after one play that spans [`duration`](orbitanimation/duration.md).

If you set a non-zero value for this property and both [`trimStart`](orbitanimation/trimstart.md) and [`trimEnd`](orbitanimation/trimend.md) are `nil`, the animation observes this property as an edited duration.

When you set [`repeatMode`](orbitanimation/repeatmode.md) to make the animation repeat:

- If this property is `nil`, the animation repeats forever.
- If set to a value greater than [`duration`](orbitanimation/duration.md), the animation repeats for the specified duration.

## See Also

- [var speed: Float](orbitanimation/speed.md)
  A factor that changes the animation’s rate of playback.
- [var delay: TimeInterval](orbitanimation/delay.md)
  An amount of time that lapses before the animation plays.
- [var duration: TimeInterval](orbitanimation/duration.md)
  The elapsed time for one complete rotation.
- [var offset: TimeInterval](orbitanimation/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var trimStart: TimeInterval?](orbitanimation/trimstart.md)
  The optional time, in seconds, at which the animation plays.
- [var trimEnd: TimeInterval?](orbitanimation/trimend.md)
  The optional time, in seconds, at which the animation stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/orbitanimation/trimduration)*