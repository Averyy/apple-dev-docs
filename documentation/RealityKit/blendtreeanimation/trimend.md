# trimEnd

**Framework**: RealityKit  
**Kind**: property

The optional time, in seconds, at which the source animation stops.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var trimEnd: TimeInterval? { get set }
```

#### Discussion

This property is `nil` by default, which plays the animation until `time` = [`duration`](blendtreeanimation/duration.md). If you set a value, the animation edits the duration according to the specified ending time.

## See Also

- [var speed: Float](blendtreeanimation/speed.md)
  A factor that increases or decreases the animation’s rate of playback.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendtreeanimation/trimend)*