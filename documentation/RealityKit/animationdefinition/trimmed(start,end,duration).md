# trimmed(start:end:duration:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Edits the animation duration according to the specified time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
func trimmed(start: TimeInterval? = nil, end: TimeInterval? = nil, duration: TimeInterval? = nil) -> Self
```

#### Return Value

A version of the animation shortened or lengthened according to the specified times.

#### Discussion

If an argument property lies outside the underlying [`duration`](./duration.md), the animation plays back according to the characteristics of its [`repeatMode`](./repeatmode.md).

## Parameters

- `start`: The time within the underlying duration to begin playback.
- `end`: The time within the underlying duration to end playback.
- `duration`: The amount of time that overrides the underlying duration.

## See Also

### Timing the animation
- [var speed: Float](./speed.md)
  A factor that increases or decreases the animation’s rate of playback.
- [var delay: TimeInterval](./delay.md)
  An amount of time that elapses before the animation plays.
- [var duration: TimeInterval](./duration.md)
  The total playback time of the animation.
- [var offset: TimeInterval](./offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var trimDuration: TimeInterval?](./trimduration.md)
  An optional duration that overrides the source animation’s duration.
- [var trimStart: TimeInterval?](./trimstart.md)
  The time, in seconds, at which the animation plays.
- [var trimEnd: TimeInterval?](./trimend.md)
  The time, in seconds, at which the source animation stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationdefinition/trimmed(start:end:duration:))*