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

- Playback progresses toward, but hasn’t yet reached, a nonzero [`offset`](animationview/offset.md). - A range determined by [`trimStart`](animationview/trimstart.md), [`trimEnd`](animationview/trimend.md), or [`trimDuration`](animationview/trimduration.md) exceeds the animation’s underlying duration.

## See Also

- [var repeatMode: AnimationRepeatMode](animationview/repeatmode.md)
  An option that determines how the animation repeats.
- [func repeated(count: TimeInterval) -> Self](animationview/repeated(count:)-353j4.md)
  Repeats an animation the number of times specified by an irrational number.
- [func repeated(count: Int) -> Self](animationview/repeated(count:)-87qbq.md)
  Repeats an animation the number of times specified by a whole number.
- [func repeatingForever() -> Self](animationview/repeatingforever.md)
  Repeats the animation infinitely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationview/fillmode)*