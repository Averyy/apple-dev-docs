# LayerRenderer.Frame.Timing

**Framework**: Compositor Services  
**Kind**: struct

A type that stores information about a frame’s encoding, rendering, and presentation deadlines.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct Timing
```

#### Overview

Before you start drawing your frame’s content, call [`predictTiming()`](layerrenderer/frame/predicttiming().md) to retrieve the frame’s timing information. That function returns the latest predicted values for you to use during planning. After you retrieve the [`LayerRenderer.Drawable`](layerrenderer/drawable.md) type for the frame, get the timing information from the drawable instead using [`frameTiming`](layerrenderer/drawable/frametiming.md).

## Topics

### Updating the frame contents
- [var optimalInputTime: LayerRenderer.Clock.Instant](layerrenderer/frame/timing/optimalinputtime.md)
  The optimal time to start the frame submission process.
### Rendering the frame
- [var renderingDeadline: LayerRenderer.Clock.Instant](layerrenderer/frame/timing/renderingdeadline.md)
  The time at which you must finish all work for the specified frame.
### Displaying the frame
- [var presentationTime: LayerRenderer.Clock.Instant](layerrenderer/frame/timing/presentationtime.md)
  The time at which the system displays the frame onscreen.
### Creating the timing details
- [init()](layerrenderer/frame/timing/init.md)
### Instance Properties
- [var trackableAnchorTime: LayerRenderer.Clock.Instant](layerrenderer/frame/timing/trackableanchortime.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [func predictTiming() -> LayerRenderer.Frame.Timing?](layerrenderer/frame/predicttiming.md)
  Computes and returns the predicted timing information for the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/frame/timing)*