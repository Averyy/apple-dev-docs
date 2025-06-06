# trimDuration

**Framework**: RealityKit  
**Kind**: property  
**Required**: Yes

An optional duration that overrides the source animation’s duration.

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

The framework calculates [`duration`](fromtobyanimation/duration.md), but you can set this property to override it. This property is `nil` by default, which indicates that the animation stops after one play that spans [`duration`](animationdefinition/duration.md).

If you set a value for this property and both [`trimStart`](animationdefinition/trimstart.md) and [`trimEnd`](animationdefinition/trimend.md) are `nil`, the animation observes this property as an edited duration.

A value greater than [`duration`](animationdefinition/duration.md) causes the animation to repeat, applying the characteristics defined by [`repeatMode`](animationdefinition/repeatmode.md). Assign this property [`greatestFiniteMagnitude`](https://developer.apple.com/documentation/Swift/Double/greatestFiniteMagnitude) to repeat indefinitely.

## See Also

- [var speed: Float](animationdefinition/speed.md)
  A factor that increases or decreases the animation’s rate of playback.
- [var delay: TimeInterval](animationdefinition/delay.md)
  An amount of time that elapses before the animation plays.
- [var duration: TimeInterval](animationdefinition/duration.md)
  The total playback time of the animation.
- [var offset: TimeInterval](animationdefinition/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var trimStart: TimeInterval?](animationdefinition/trimstart.md)
  The time, in seconds, at which the animation plays.
- [var trimEnd: TimeInterval?](animationdefinition/trimend.md)
  The time, in seconds, at which the source animation stops.
- [func trimmed(start: TimeInterval?, end: TimeInterval?, duration: TimeInterval?) -> Self](animationdefinition/trimmed(start:end:duration:).md)
  Edits the animation duration according to the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationdefinition/trimduration)*