# fillMode

**Framework**: RealityKit  
**Kind**: property

An option that determines which data displays outside of the normal duration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
var fillMode: AnimationFillMode { get set }
```

#### Discussion

This property determines what to display when the framework samples the animation outside of the range defined by its underlying duration. The animation applies this property when:

- Playback progresses toward, but hasn’t yet reached, a nonzero [`offset`](animationdefinition/offset.md). - A range determined by [`trimStart`](animationdefinition/trimstart.md), [`trimEnd`](animationdefinition/trimend.md), or [`trimDuration`](animationdefinition/trimduration.md) exceeds the animation’s underlying duration.

## See Also

- [var repeatMode: AnimationRepeatMode](fromtobyanimation/repeatmode.md)
  An option that determines how the animation repeats.
- [func repeated(count: TimeInterval) -> Self](fromtobyanimation/repeated(count:)-4f0eh.md)
  Repeats an animation the number of times specified by an irrational number.
- [func repeated(count: Int) -> Self](fromtobyanimation/repeated(count:)-1ykci.md)
  Repeats an animation the number of times specified by a whole number.
- [func repeatingForever() -> Self](fromtobyanimation/repeatingforever.md)
  Repeats the animation infinitely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyanimation/fillmode)*