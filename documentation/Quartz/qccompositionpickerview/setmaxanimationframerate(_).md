# setMaxAnimationFrameRate(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Sets the maximum frame rate for animating compositions.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func setMaxAnimationFrameRate(_ maxFPS: Float)
```

```objc
- (void) setMaxAnimationFrameRate:(float) maxFPS;
```

## Parameters

- `maxFPS`: A frame rate in frames per second. Pass `0.0` to specify no limit to the maximum value.

## See Also

### Managing Animation
- [func startAnimation(Any!)](./startanimation%28_%29.md)
  Starts animating the composition in the composition picker view.
- [func stopAnimation(Any!)](./stopanimation%28_%29.md)
  Stops animating the composition that is currently animating in the composition picker view.
- [func isAnimating() -> Bool](./isanimating%28%29.md)
  Returns whether or not the composition picker view is currently animating its composition.
- [func maxAnimationFrameRate() -> Float](./maxanimationframerate%28%29.md)
  Retrieves the maximum frame rate for animating compositions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionpickerview/setmaxanimationframerate(_:))*