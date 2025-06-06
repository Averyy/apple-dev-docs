# both

**Framework**: RealityKit  
**Kind**: property

An option that displays the animation’s initial frame or final frame when playback occurs outside of the normal duration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
static let both: AnimationFillMode
```

#### Discussion

For example, if you extend a hand-waving animation’s duration by one second in both directions by setting [`trimStart`](sampledanimation/trimstart.md) to `-1.0`, and [`trimEnd`](sampledanimation/trimend.md) to [`duration`](sampledanimation/duration.md) + `1.0`, a [`fillMode`](sampledanimation/fillmode.md) of `both` determines that the hand holds its initial appearance for one second before continuing to wave. Then, the animation freezes on its final hand-waving frame for one second before disappearing.

## See Also

- [static let none: AnimationFillMode](animationfillmode/none.md)
  An option that indicates an animation doesn’t display frame data outside of its normal duration.
- [static let forwards: AnimationFillMode](animationfillmode/forwards.md)
  An option that freezes the last frame of the animation until it stops.
- [static let backwards: AnimationFillMode](animationfillmode/backwards.md)
  An option that shows the first animation frame while playback progresses to the beginning position.
- [let rawValue: Int8](animationfillmode/rawvalue-swift.property.md)
  The corresponding value of the raw type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationfillmode/both)*