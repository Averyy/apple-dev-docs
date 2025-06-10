# trimEnd

**Framework**: RealityKit  
**Kind**: property

The time, in seconds, at which the source animation stops.

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

This property is `nil` by default, which plays the animation until `time` = [`duration`](animationview/duration.md). If you set a value, the animation edits the duration according to the specified ending time.

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
- [var trimStart: TimeInterval?](animationview/trimstart.md)
  The time, in seconds, at which the source animation plays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationview/trimend)*