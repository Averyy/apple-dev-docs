# duration

**Framework**: RealityKit  
**Kind**: property  
**Required**: Yes

The total playback time of the animation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var duration: TimeInterval { get }
```

#### Discussion

The framework sets a value for this property depending on the underlying animation data and the specified [`speed`](animationdefinition/speed.md).

You can override the default duration by defining [`trimStart`](animationdefinition/trimstart.md), [`trimEnd`](animationdefinition/trimend.md), or [`trimDuration`](animationdefinition/trimduration.md).

## See Also

- [var speed: Float](animationdefinition/speed.md)
  A factor that increases or decreases the animation’s rate of playback.
- [var delay: TimeInterval](animationdefinition/delay.md)
  An amount of time that elapses before the animation plays.
- [var offset: TimeInterval](animationdefinition/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var trimDuration: TimeInterval?](animationdefinition/trimduration.md)
  An optional duration that overrides the source animation’s duration.
- [var trimStart: TimeInterval?](animationdefinition/trimstart.md)
  The time, in seconds, at which the animation plays.
- [var trimEnd: TimeInterval?](animationdefinition/trimend.md)
  The time, in seconds, at which the source animation stops.
- [func trimmed(start: TimeInterval?, end: TimeInterval?, duration: TimeInterval?) -> Self](animationdefinition/trimmed(start:end:duration:).md)
  Edits the animation duration according to the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationdefinition/duration)*