# trimEnd

**Framework**: RealityKit  
**Kind**: property  
**Required**: Yes

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

This property is `nil` by default, which plays the animation until `time` = [`duration`](animationdefinition/duration.md). If you set a value, the animation edits the duration according to the specified ending time.

## See Also

- [var speed: Float](animationdefinition/speed.md)
  A factor that increases or decreases the animation’s rate of playback.
- [var delay: TimeInterval](animationdefinition/delay.md)
  An amount of time that elapses before the animation plays.
- [var duration: TimeInterval](animationdefinition/duration.md)
  The total playback time of the animation.
- [var offset: TimeInterval](animationdefinition/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var trimDuration: TimeInterval?](animationdefinition/trimduration.md)
  An optional duration that overrides the source animation’s duration.
- [var trimStart: TimeInterval?](animationdefinition/trimstart.md)
  The time, in seconds, at which the animation plays.
- [func trimmed(start: TimeInterval?, end: TimeInterval?, duration: TimeInterval?) -> Self](animationdefinition/trimmed(start:end:duration:).md)
  Edits the animation duration according to the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationdefinition/trimend)*