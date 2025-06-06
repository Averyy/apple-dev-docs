# startAnimation(_:)

**Framework**: Quartz  
**Kind**: method

Starts animating the composition in the composition picker view.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func startAnimation(_ sender: Any!)
```

## Parameters

- `sender`: The object initiating the animation.

## See Also

- [func stopAnimation(Any!)](qccompositionpickerview/stopanimation(_:).md)
  Stops animating the composition that is currently animating in the composition picker view.
- [func isAnimating() -> Bool](qccompositionpickerview/isanimating.md)
  Returns whether or not the composition picker view is currently animating its composition.
- [func setMaxAnimationFrameRate(Float)](qccompositionpickerview/setmaxanimationframerate(_:).md)
  Sets the maximum frame rate for animating compositions.
- [func maxAnimationFrameRate() -> Float](qccompositionpickerview/maxanimationframerate.md)
  Retrieves the maximum frame rate for animating compositions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionpickerview/startanimation(_:))*