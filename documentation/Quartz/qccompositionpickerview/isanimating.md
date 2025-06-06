# isAnimating()

**Framework**: Quartz  
**Kind**: method

Returns whether or not the composition picker view is currently animating its composition.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func isAnimating() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if a composition is animating in the composition picker view; [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

## See Also

- [func startAnimation(Any!)](qccompositionpickerview/startanimation(_:).md)
  Starts animating the composition in the composition picker view.
- [func stopAnimation(Any!)](qccompositionpickerview/stopanimation(_:).md)
  Stops animating the composition that is currently animating in the composition picker view.
- [func setMaxAnimationFrameRate(Float)](qccompositionpickerview/setmaxanimationframerate(_:).md)
  Sets the maximum frame rate for animating compositions.
- [func maxAnimationFrameRate() -> Float](qccompositionpickerview/maxanimationframerate.md)
  Retrieves the maximum frame rate for animating compositions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionpickerview/isanimating())*