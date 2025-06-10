# trimEnd

**Framework**: RealityKit  
**Kind**: property

The optional time, in seconds, at which the animation stops.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var trimEnd: TimeInterval? { get set }
```

#### Discussion

This property is `nil` by default, which plays the animation until `time` = [`duration`](animationgroup/duration.md). If you set a value, the animation edits the duration according to the specified ending time.

## See Also

- [var speed: Float](orbitanimation/speed.md)
  A factor that changes the animation’s rate of playback.
- [var delay: TimeInterval](orbitanimation/delay.md)
  An amount of time that lapses before the animation plays.
- [var duration: TimeInterval](orbitanimation/duration.md)
  The elapsed time for one complete rotation.
- [var offset: TimeInterval](orbitanimation/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var trimDuration: TimeInterval?](orbitanimation/trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimStart: TimeInterval?](orbitanimation/trimstart.md)
  The optional time, in seconds, at which the animation plays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/orbitanimation/trimend)*