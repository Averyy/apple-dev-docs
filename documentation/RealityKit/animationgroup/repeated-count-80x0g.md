# repeated(count:)

**Framework**: RealityKit  
**Kind**: method

Repeats an animation the number of times specified by an irrational number.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
func repeated(count: TimeInterval) -> Self
```

#### Return Value

A version of the calling animation repeated the given number of times.

## Parameters

- `count`: The number of times the animation repeats before stopping.

## See Also

- [var repeatMode: AnimationRepeatMode](animationgroup/repeatmode.md)
  An option that determines how the animations repeat.
- [var fillMode: AnimationFillMode](animationgroup/fillmode.md)
  An option that determines which data displays outside of the normal duration.
- [func repeated(count: Int) -> Self](animationgroup/repeated(count:)-3445q.md)
  Repeats an animation the number of times specified by a whole number.
- [func repeatingForever() -> Self](animationgroup/repeatingforever.md)
  Repeats the animation infinitely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgroup/repeated(count:)-80x0g)*