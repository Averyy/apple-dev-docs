# setCompositionRenderer(_:)

**Framework**: Quartz  
**Kind**: method

Sets the composition parameter view for editing the input parameters of the provided renderer object.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setCompositionRenderer(_ renderer: (any QCCompositionRenderer)!)
```

#### Discussion

If the renderer is a [`QCView`](qcview.md) object, the view track the composition.

## Parameters

- `renderer`: A   object, either  ,  , or  . Pass   to unset this renderer.

## See Also

- [func compositionRenderer() -> (any QCCompositionRenderer)!](qccompositionparameterview/compositionrenderer.md)
  Returns the renderer object associated with the composition parameter view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionparameterview/setcompositionrenderer(_:))*