# trimmed(start:end:duration:)

**Framework**: RealityKit  
**Kind**: method

Edits the animation duration according to the specified time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
func trimmed(start: TimeInterval? = nil, end: TimeInterval? = nil, duration: TimeInterval? = nil) -> Self
```

#### Return Value

A version of the animation shortened or lengthened according to the specified times.

#### Discussion

If an argument property lies outside the underlying [`duration`](animationdefinition/duration.md), the animation plays back according to the characteristics of its [`repeatMode`](animationdefinition/repeatmode.md).

## Parameters

- `start`: The time within the underlying duration to begin playback.
- `end`: The time within the underlying duration to end playback.
- `duration`: The amount of time that overrides the underlying duration.

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
- [var trimEnd: TimeInterval?](blendtreeanimation/trimend.md)
  The optional time, in seconds, at which the source animation stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendtreeanimation/trimmed(start:end:duration:))*