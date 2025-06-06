# none

**Framework**: RealityKit  
**Kind**: property

An option that indicates an animation doesn’t display frame data outside of its normal duration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
static let none: AnimationFillMode
```

#### Discussion

For example, if you rewind an animation of a hand waving for one second by setting [`trimStart`](sampledanimation/trimstart.md) to `-1.0`, a [`fillMode`](sampledanimation/fillmode.md) of `none` determines that the hand is invisible for one second before appearing and waving.

## See Also

- [static let forwards: AnimationFillMode](animationfillmode/forwards.md)
  An option that freezes the last frame of the animation until it stops.
- [static let backwards: AnimationFillMode](animationfillmode/backwards.md)
  An option that shows the first animation frame while playback progresses to the beginning position.
- [static let both: AnimationFillMode](animationfillmode/both.md)
  An option that displays the animation’s initial frame or final frame when playback occurs outside of the normal duration.
- [let rawValue: Int8](animationfillmode/rawvalue-swift.property.md)
  The corresponding value of the raw type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationfillmode/none)*