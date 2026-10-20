# maxAnimationFrameRate()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Retrieves the maximum frame rate for animating compositions.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func maxAnimationFrameRate() -> Float
```

```objc
- (float) maxAnimationFrameRate;
```

#### Return Value

The maximum frame rate.

## See Also

### Managing Animation
- [func startAnimation(Any!)](./startanimation%28_%29.md)
  Starts animating the composition in the composition picker view.
- [func stopAnimation(Any!)](./stopanimation%28_%29.md)
  Stops animating the composition that is currently animating in the composition picker view.
- [func isAnimating() -> Bool](./isanimating%28%29.md)
  Returns whether or not the composition picker view is currently animating its composition.
- [func setMaxAnimationFrameRate(Float)](./setmaxanimationframerate%28_%29.md)
  Sets the maximum frame rate for animating compositions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionpickerview/maxanimationframerate())*