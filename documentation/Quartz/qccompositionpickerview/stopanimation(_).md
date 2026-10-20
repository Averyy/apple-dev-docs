# stopAnimation(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Stops animating the composition that is currently animating in the composition picker view.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func stopAnimation(_ sender: Any!)
```

```objc
- (void) stopAnimation:(id) sender;
```

## Parameters

- `sender`: The object stopping the animation.

## See Also

### Managing Animation
- [func startAnimation(Any!)](./startanimation%28_%29.md)
  Starts animating the composition in the composition picker view.
- [func isAnimating() -> Bool](./isanimating%28%29.md)
  Returns whether or not the composition picker view is currently animating its composition.
- [func setMaxAnimationFrameRate(Float)](./setmaxanimationframerate%28_%29.md)
  Sets the maximum frame rate for animating compositions.
- [func maxAnimationFrameRate() -> Float](./maxanimationframerate%28%29.md)
  Retrieves the maximum frame rate for animating compositions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionpickerview/stopanimation(_:))*