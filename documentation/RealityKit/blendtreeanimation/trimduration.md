# trimDuration

**Framework**: RealityKit  
**Kind**: property

An optional duration that overrides the calculated duration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
var trimDuration: TimeInterval? { get set }
```

#### Discussion

The framework calculates [`duration`](fromtobyanimation/duration.md), but you can set this property to override it. This property is `nil` by default, which indicates that the animation stops after one play that spans [`duration`](blendtreeanimation/duration.md).

If you set a value for this property and both [`trimStart`](blendtreeanimation/trimstart.md) and [`trimEnd`](blendtreeanimation/trimend.md) are `nil`, the animation observes this property as an edited duration.

A value greater than [`duration`](blendtreeanimation/duration.md) causes the animation to repeat, applying the characteristics defined by [`repeatMode`](blendtreeanimation/repeatmode.md). Assign this property [`greatestFiniteMagnitude`](https://developer.apple.com/documentation/Swift/Double/greatestFiniteMagnitude) to repeat indefinitely.

## See Also

- [var speed: Float](blendtreeanimation/speed.md)
  A factor that increases or decreases the animation’s rate of playback.
- [var delay: TimeInterval](blendtreeanimation/delay.md)
  An amount of time that lapses before the animation plays.
- [var duration: TimeInterval](blendtreeanimation/duration.md)
  The total playback time of the animation.
- [var offset: TimeInterval](blendtreeanimation/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var trimStart: TimeInterval?](blendtreeanimation/trimstart.md)
  The optional time, in seconds, at which the source animation plays.
- [var trimEnd: TimeInterval?](blendtreeanimation/trimend.md)
  The optional time, in seconds, at which the source animation stops.
- [func trimmed(start: TimeInterval?, end: TimeInterval?, duration: TimeInterval?) -> Self](blendtreeanimation/trimmed(start:end:duration:).md)
  Edits the animation duration according to the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendtreeanimation/trimduration)*