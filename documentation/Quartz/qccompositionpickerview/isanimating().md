# isAnimating()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns whether or not the composition picker view is currently animating its composition.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func isAnimating() -> Bool
```

```objc
- (BOOL) isAnimating;
```

## Return Value

[`true`](../../Swift/true.md) if a composition is animating in the composition picker view; [`false`](../../Swift/false.md) otherwise.

## See Also

### Managing Animation
- [func startAnimation(Any!)](./startanimation%28_%29.md)
  Starts animating the composition in the composition picker view.
- [func stopAnimation(Any!)](./stopanimation%28_%29.md)
  Stops animating the composition that is currently animating in the composition picker view.
- [func setMaxAnimationFrameRate(Float)](./setmaxanimationframerate%28_%29.md)
  Sets the maximum frame rate for animating compositions.
- [func maxAnimationFrameRate() -> Float](./maxanimationframerate%28%29.md)
  Retrieves the maximum frame rate for animating compositions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionpickerview/isanimating())*