# setMaxRenderingFrameRate(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Sets the maximum rendering frame rate.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func setMaxRenderingFrameRate(_ maxFPS: Float)
```

```objc
- (void) setMaxRenderingFrameRate:(float) maxFPS;
```

## Parameters

- `maxFPS`: The frame rate to set. Pass `0.0` to specify that there is no limit.

## See Also

### Setting and Getting the Maximum Frame Rate
- [func maxRenderingFrameRate() -> Float](./maxrenderingframerate%28%29.md)
  Returns the maximum frame rate for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/setmaxrenderingframerate(_:))*