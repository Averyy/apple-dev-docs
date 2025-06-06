# setMaxAnimationFrameRate(_:)

**Framework**: Quartz  
**Kind**: method

Sets the maximum frame rate for animating compositions.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setMaxAnimationFrameRate(_ maxFPS: Float)
```

## Parameters

- `maxFPS`: A frame rate in frames per second. Pass   to specify no limit to the maximum value.

## See Also

- [func startAnimation(Any!)](qccompositionpickerview/startanimation(_:).md)
  Starts animating the composition in the composition picker view.
- [func stopAnimation(Any!)](qccompositionpickerview/stopanimation(_:).md)
  Stops animating the composition that is currently animating in the composition picker view.
- [func isAnimating() -> Bool](qccompositionpickerview/isanimating.md)
  Returns whether or not the composition picker view is currently animating its composition.
- [func maxAnimationFrameRate() -> Float](qccompositionpickerview/maxanimationframerate.md)
  Retrieves the maximum frame rate for animating compositions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionpickerview/setmaxanimationframerate(_:))*