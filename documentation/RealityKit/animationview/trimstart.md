# trimStart

**Framework**: RealityKit  
**Kind**: property

The time, in seconds, at which the source animation plays.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var trimStart: TimeInterval? { get set }
```

#### Discussion

This property is `nil` by default, which plays the animation with `time` = `0`. If you set a value, the animation edits the duration according to the specified beginning time.

If you set a negative value for this property, the duration increases and the additional animation data fills in based on the [`fillMode`](animationview/fillmode.md) you choose.

## See Also

- [var speed: Float](animationview/speed.md)
  A factor that increases or decreases the animation’s rate of playback.
- [var delay: TimeInterval](animationview/delay.md)
  An amount of time that lapses before the animation plays.
- [var duration: TimeInterval](animationview/duration.md)
  The total playback time of the animation.
- [var offset: TimeInterval](animationview/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var trimDuration: TimeInterval?](animationview/trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimEnd: TimeInterval?](animationview/trimend.md)
  The time, in seconds, at which the source animation stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationview/trimstart)*