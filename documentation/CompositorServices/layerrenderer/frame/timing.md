# LayerRenderer.Frame.Timing

**Framework**: Compositor Services  
**Kind**: struct  
**Role**: Structure

A type that stores information about a frame’s encoding, rendering, and presentation deadlines.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct Timing
```

#### Overview

Before you start drawing your frame’s content, call [`predictTiming()`](./predicttiming%28%29.md) to retrieve the frame’s timing information. That function returns the latest predicted values for you to use during planning. After you retrieve the [`LayerRenderer.Drawable`](../drawable.md) type for the frame, get the timing information from the drawable instead using [`frameTiming`](../drawable/frametiming.md).

## Topics

### Updating the frame contents
- [var optimalInputTime: LayerRenderer.Clock.Instant](./timing/optimalinputtime.md)
  The optimal time to start the frame submission process.
### Rendering the frame
- [var renderingDeadline: LayerRenderer.Clock.Instant](./timing/renderingdeadline.md)
  The time at which you must finish all work for the specified frame.
### Displaying the frame
- [var presentationTime: LayerRenderer.Clock.Instant](./timing/presentationtime.md)
  The time at which the system displays the frame onscreen.
### Creating the timing details
- [init()](./timing/init%28%29.md)
### Instance Properties
- [var trackableAnchorTime: LayerRenderer.Clock.Instant](./timing/trackableanchortime.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)

## See Also

### Getting timing information
- [func predictTiming() -> LayerRenderer.Frame.Timing?](./predicttiming%28%29.md)
  Computes and returns the predicted timing information for the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/frame/timing)*