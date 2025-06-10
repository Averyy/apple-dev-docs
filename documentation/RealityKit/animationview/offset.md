# offset

**Framework**: RealityKit  
**Kind**: property

The time, in seconds, at which the animation begins within the duration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var offset: TimeInterval { get set }
```

#### Discussion

The default value is `0`, which indicates that the animation plays with no offset. Setting a value for this property moves the animation data along the timeline and doesn’t change timing. If you set a [`fillMode`](sampledanimation/fillmode.md) other than [`none`](animationfillmode/none.md), the animation fills the vacant area created by the offset according to the characteristics of the specified fill mode.

## See Also

- [var speed: Float](animationview/speed.md)
  A factor that increases or decreases the animation’s rate of playback.
- [var delay: TimeInterval](animationview/delay.md)
  An amount of time that lapses before the animation plays.
- [var duration: TimeInterval](animationview/duration.md)
  The total playback time of the animation.
- [var trimDuration: TimeInterval?](animationview/trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimStart: TimeInterval?](animationview/trimstart.md)
  The time, in seconds, at which the source animation plays.
- [var trimEnd: TimeInterval?](animationview/trimend.md)
  The time, in seconds, at which the source animation stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationview/offset)*