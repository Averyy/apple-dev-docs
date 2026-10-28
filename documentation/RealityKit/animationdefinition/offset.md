# offset

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The time, in seconds, at which the animation begins within the duration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
var offset: TimeInterval { get set }
```

## Discussion

The default value is `0`, which indicates that the animation plays with no offset. Setting a value for this property moves the animation data along the timeline and doesn’t change timing. If you set a [`fillMode`](../sampledanimation/fillmode.md) other than [`none`](../animationfillmode/none.md), the animation fills the vacant area created by the offset according to the characteristics of the specified fill mode.

## See Also

### Timing the animation
- [var speed: Float](./speed.md)
  A factor that increases or decreases the animation’s rate of playback.
- [var delay: TimeInterval](./delay.md)
  An amount of time that elapses before the animation plays.
- [var duration: TimeInterval](./duration.md)
  The total playback time of the animation.
- [var trimDuration: TimeInterval?](./trimduration.md)
  An optional duration that overrides the source animation’s duration.
- [var trimStart: TimeInterval?](./trimstart.md)
  The time, in seconds, at which the animation plays.
- [var trimEnd: TimeInterval?](./trimend.md)
  The time, in seconds, at which the source animation stops.
- [func trimmed(start: TimeInterval?, end: TimeInterval?, duration: TimeInterval?) -> Self](./trimmed%28start,end,duration%29.md)
  Edits the animation duration according to the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationdefinition/offset)*