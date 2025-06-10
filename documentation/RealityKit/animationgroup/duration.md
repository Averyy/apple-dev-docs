# duration

**Framework**: RealityKit  
**Kind**: property

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

The framework sets a value for this property depending on the underlying animation data and the specified [`speed`](animationgroup/speed.md).

You can override the default duration by defining [`trimStart`](animationgroup/trimstart.md), [`trimEnd`](animationgroup/trimend.md), or [`trimDuration`](animationgroup/trimduration.md).

## See Also

- [var speed: Float](animationgroup/speed.md)
  A factor that increases or decreases the animation’s rate of playback.
- [var delay: TimeInterval](animationgroup/delay.md)
  An amount of time that lapses before the animation plays.
- [var offset: TimeInterval](animationgroup/offset.md)
  The time, in seconds, at which the animations begin within the duration.
- [var trimDuration: TimeInterval?](animationgroup/trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimStart: TimeInterval?](animationgroup/trimstart.md)
  The time, in seconds, at which the animations play.
- [var trimEnd: TimeInterval?](animationgroup/trimend.md)
  The time, in seconds, at which the animations stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgroup/duration)*