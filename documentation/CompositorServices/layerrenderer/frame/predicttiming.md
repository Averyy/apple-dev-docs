# predictTiming()

**Framework**: Compositor Services  
**Kind**: method

Computes and returns the predicted timing information for the frame.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
func predictTiming() -> LayerRenderer.Frame.Timing?
```

## Mentions

- [Drawing fully immersive content using Metal](drawing-fully-immersive-content-using-metal.md)

#### Return Value

The predicted timing information for the specified frame, or `nil` if the layer is in the `Layer.State.paused` or `Layer.State.invalidated` state.

#### Discussion

The returned timing information contains the frame-related deadlines to meet during the rendering process. For example, wait until the time in `optimalInputTime` to start the submission phase of your frame update. This function updates the frame-specific timing information with the latest data from Compositor Services before it returns it.

Don’t call this function after you call [`queryDrawable()`](layerrenderer/frame/querydrawable().md) for the specified frame. After you retrieve the frame’s [`LayerRenderer.Drawable`](layerrenderer/drawable.md) type, get the timing information from the drawable’s [`frameTiming`](layerrenderer/drawable/frametiming.md) property instead.

## See Also

- [LayerRenderer.Frame.Timing](layerrenderer/frame/timing.md)
  A type that stores information about a frame’s encoding, rendering, and presentation deadlines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/frame/predicttiming())*