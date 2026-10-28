# compositionRenderer()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the renderer object associated with the composition parameter view.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func compositionRenderer() -> (any QCCompositionRenderer)!
```

```objc
- (id<QCCompositionRenderer>) compositionRenderer;
```

## Return Value

A renderer object or `nil`, if the composition parameter view is not set to a renderer object.

## See Also

### Getting and Setting the Renderer
- [func setCompositionRenderer((any QCCompositionRenderer)!)](./setcompositionrenderer%28_%29.md)
  Sets the composition parameter view for editing the input parameters of the provided renderer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionparameterview/compositionrenderer())*