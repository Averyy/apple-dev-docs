# forwards

**Framework**: RealityKit  
**Kind**: property

An option that freezes the last frame of the animation until it stops.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
static let forwards: AnimationFillMode
```

#### Discussion

For example, if you increase a hand-waving animation’s duration one second by setting [`trimEnd`](sampledanimation/trimend.md) to [`duration`](sampledanimation/duration.md) + `1.0`, a [`fillMode`](sampledanimation/fillmode.md) of `forwards` determines that the hand waves and then freezes on its final animation frame for one second before disappearing.

## See Also

- [static let none: AnimationFillMode](animationfillmode/none.md)
  An option that indicates an animation doesn’t display frame data outside of its normal duration.
- [static let backwards: AnimationFillMode](animationfillmode/backwards.md)
  An option that shows the first animation frame while playback progresses to the beginning position.
- [static let both: AnimationFillMode](animationfillmode/both.md)
  An option that displays the animation’s initial frame or final frame when playback occurs outside of the normal duration.
- [let rawValue: Int8](animationfillmode/rawvalue-swift.property.md)
  The corresponding value of the raw type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationfillmode/forwards)*