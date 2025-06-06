# frameTiming

**Framework**: Compositor Services  
**Kind**: property

The timing information for the drawable’s frame.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var frameTiming: LayerRenderer.Frame.Timing { get }
```

## Mentions

- [Drawing fully immersive content using Metal](drawing-fully-immersive-content-using-metal.md)

#### Discussion

This retrieves a frame’s timing information from a drawable instance that represents that frame. For Swift, it’s an alternative to calling a frame’s [`predictTiming()`](layerrenderer/frame/predicttiming().md) method. For ObjectiveC, it’s an alternative to calling the [`cp_frame_predict_timing`](cp_frame_predict_timing.md) function.

In ObjectiveC, you can determine when to start updating your data structures by passing a [`cp_frame_timing_t`](cp_frame_timing_t.md) instance to the [`cp_frame_timing_get_optimal_input_time`](cp_frame_timing_get_optimal_input_time.md) function.

## See Also

- [var presentationFrameIndex: CompositorFrameIndex](layerrenderer/drawable/presentationframeindex.md)
  The sequential index of a drawable’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/frametiming)*