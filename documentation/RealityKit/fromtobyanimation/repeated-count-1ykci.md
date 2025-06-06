# repeated(count:)

**Framework**: RealityKit  
**Kind**: method

Repeats an animation the number of times specified by a whole number.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
func repeated(count: Int) -> Self
```

#### Return Value

A version of the calling animation repeated the given number of times.

## Parameters

- `count`: The number of times the animation repeats before stopping.

## See Also

- [var repeatMode: AnimationRepeatMode](fromtobyanimation/repeatmode.md)
  An option that determines how the animation repeats.
- [var fillMode: AnimationFillMode](fromtobyanimation/fillmode.md)
  An option that determines which data displays outside of the normal duration.
- [func repeated(count: TimeInterval) -> Self](fromtobyanimation/repeated(count:)-4f0eh.md)
  Repeats an animation the number of times specified by an irrational number.
- [func repeatingForever() -> Self](fromtobyanimation/repeatingforever.md)
  Repeats the animation infinitely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyanimation/repeated(count:)-1ykci)*