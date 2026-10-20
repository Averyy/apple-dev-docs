# forwards

**Framework**: RealityKit  
**Kind**: property  
**Role**: Type Property

An option that freezes the last frame of the animation until it stops.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
static let forwards: AnimationFillMode
```

#### Discussion

For example, if you increase a hand-waving animation’s duration one second by setting [`trimEnd`](../sampledanimation/trimend.md) to [`duration`](../sampledanimation/duration.md) + `1.0`, a [`fillMode`](../sampledanimation/fillmode.md) of `forwards` determines that the hand waves and then freezes on its final animation frame for one second before disappearing.

## See Also

### Choosing a fill mode
- [static let none: AnimationFillMode](./none.md)
  An option that indicates an animation doesn’t display frame data outside of its normal duration.
- [static let backwards: AnimationFillMode](./backwards.md)
  An option that shows the first animation frame while playback progresses to the beginning position.
- [static let both: AnimationFillMode](./both.md)
  An option that displays the animation’s initial frame or final frame when playback occurs outside of the normal duration.
- [init(rawValue: Int8)](./init%28rawvalue%29.md)
  Creates a fill mode from its backing data type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationfillmode/forwards)*