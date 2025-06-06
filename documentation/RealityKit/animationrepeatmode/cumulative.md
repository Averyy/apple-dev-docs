# AnimationRepeatMode.cumulative

**Framework**: RealityKit  
**Kind**: case

A mode that repeats indefinitely and begins each repetition by setting the animated property to the ending value of the previous repetition.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
case cumulative
```

#### Discussion

A [`FromToByAnimation`](fromtobyanimation.md) with a [`fromValue`](fromtobyanimation/fromvalue-umpp.md) of `1.0` and an [`toValue`](fromtobyanimation/tovalue-4m4pm.md) of `2.0` and [`repeatMode`](fromtobyanimation/repeatmode.md) set to this property repeats as, `1.0`, `2.0`, 3`.0`, 4`.0`, `5.0`, and so on.

## See Also

- [AnimationRepeatMode.repeat](animationrepeatmode/repeat.md)
  A mode that restarts the animation after it completes.
- [AnimationRepeatMode.autoReverse](animationrepeatmode/autoreverse.md)
  A mode that reverses the animation after reaching the end or the beginning.
- [AnimationRepeatMode.none](animationrepeatmode/none.md)
  An option that determines the animation doesn’t repeat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationrepeatmode/cumulative)*