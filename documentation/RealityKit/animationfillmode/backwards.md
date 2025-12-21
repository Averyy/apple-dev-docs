# backwards

**Framework**: RealityKit  
**Kind**: property

An option that shows the first animation frame while playback progresses to the beginning position.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
static let backwards: AnimationFillMode
```

#### Discussion

For example, if you wind a hand-waving animation’s duration back one second by setting [`trimStart`](sampledanimation/trimstart.md) to `-1.0`, a [`fillMode`](sampledanimation/fillmode.md) of `backwards` determines that the hand holds its initial appearance for one second before waving.

## See Also

- [static let none: AnimationFillMode](animationfillmode/none.md)
  An option that indicates an animation doesn’t display frame data outside of its normal duration.
- [static let forwards: AnimationFillMode](animationfillmode/forwards.md)
  An option that freezes the last frame of the animation until it stops.
- [static let both: AnimationFillMode](animationfillmode/both.md)
  An option that displays the animation’s initial frame or final frame when playback occurs outside of the normal duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationfillmode/backwards)*