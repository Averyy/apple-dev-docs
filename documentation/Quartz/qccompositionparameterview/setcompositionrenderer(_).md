# setCompositionRenderer(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Sets the composition parameter view for editing the input parameters of the provided renderer object.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func setCompositionRenderer(_ renderer: (any QCCompositionRenderer)!)
```

```objc
- (void) setCompositionRenderer:(id<QCCompositionRenderer>) renderer;
```

## Discussion

If the renderer is a [`QCView`](../qcview.md) object, the view track the composition.

## Parameters

- `renderer`: A `QCCompositionRenderer` object, either [`QCView`](../qcview.md), [`QCRenderer`](../qcrenderer.md), or [`QCCompositionLayer`](../qccompositionlayer.md). Pass `nil` to unset this renderer.

## See Also

### Getting and Setting the Renderer
- [func compositionRenderer() -> (any QCCompositionRenderer)!](./compositionrenderer%28%29.md)
  Returns the renderer object associated with the composition parameter view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionparameterview/setcompositionrenderer(_:))*