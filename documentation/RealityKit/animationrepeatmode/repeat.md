# AnimationRepeatMode.repeat

**Framework**: RealityKit  
**Kind**: case

A mode that restarts the animation after it completes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
case `repeat`
```

#### Discussion

This mode restores the animated property to its initial value each time it restarts. For example, a [`FromToByAnimation`](fromtobyanimation.md) with [`fromValue`](fromtobyanimation/fromvalue-umpp.md) `=` `1.0`, [`toValue`](fromtobyanimation/tovalue-4m4pm.md) `=` `2.0` and [`repeatMode`](fromtobyanimation/repeatmode.md) set to this property repeats as, `1.0`, `2.0`, `1.0`, `2.0`, `1.0`, `2.0` and so on.

## See Also

- [AnimationRepeatMode.cumulative](animationrepeatmode/cumulative.md)
  A mode that repeats indefinitely and begins each repetition by setting the animated property to the ending value of the previous repetition.
- [AnimationRepeatMode.autoReverse](animationrepeatmode/autoreverse.md)
  A mode that reverses the animation after reaching the end or the beginning.
- [AnimationRepeatMode.none](animationrepeatmode/none.md)
  An option that determines the animation doesn’t repeat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationrepeatmode/repeat)*