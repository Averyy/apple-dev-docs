# startAnimation(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Starts animating the composition in the composition picker view.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func startAnimation(_ sender: Any!)
```

```objc
- (void) startAnimation:(id) sender;
```

## Parameters

- `sender`: The object initiating the animation.

## See Also

### Managing Animation
- [func stopAnimation(Any!)](./stopanimation%28_%29.md)
  Stops animating the composition that is currently animating in the composition picker view.
- [func isAnimating() -> Bool](./isanimating%28%29.md)
  Returns whether or not the composition picker view is currently animating its composition.
- [func setMaxAnimationFrameRate(Float)](./setmaxanimationframerate%28_%29.md)
  Sets the maximum frame rate for animating compositions.
- [func maxAnimationFrameRate() -> Float](./maxanimationframerate%28%29.md)
  Retrieves the maximum frame rate for animating compositions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionpickerview/startanimation(_:))*