# cp_frame_predict_timing

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Computes and returns the predicted timing information for the frame.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
cp_frame_timing_tcp_frame_predict_timing(cp_frame_t frame);
```

## Mentions

- [Drawing fully immersive content using Metal](./drawing-fully-immersive-content-using-metal.md)

## Return Value

The predicted timing information for the specified frame, or `nil` if the layer is in the [`LayerRenderer.State.paused`](./layerrenderer/state-swift.enum/paused.md) or [`LayerRenderer.State.invalidated`](./layerrenderer/state-swift.enum/invalidated.md) state.

## Discussion

The returned type contains the timing information for the specified frame. Use related functions to retrieve specific values. For example, use the [`cp_frame_timing_get_optimal_input_time`](./cp_frame_timing_get_optimal_input_time.md) function to determine when to start the submission phase of your frame update. This function updates the frame-specific timing information with the latest data from Compositor Services before it returns it.

Don’t call this function after you call [`cp_frame_query_drawable`](./cp_frame_query_drawable.md) for the specified frame. After you retrieve the frame’s [`cp_drawable_t`](./cp_drawable_t.md) type, get the timing information from the drawable’s [`frameTiming`](./layerrenderer/drawable/frametiming.md) function instead.

## Parameters

- `frame`: The frame you’re preparing to draw.

## See Also

### Getting timing information
- [cp_frame_timing_get_optimal_input_time](./cp_frame_timing_get_optimal_input_time.md)
  Returns the optimal time to start the frame submission process.
- [cp_frame_timing_get_rendering_deadline](./cp_frame_timing_get_rendering_deadline.md)
  Returns the time at which you must finish all work for the specified frame.
- [cp_frame_timing_get_presentation_time](./cp_frame_timing_get_presentation_time.md)
  Returns the time at which the system displays the frame.
- [cp_frame_timing_t](./cp_frame_timing_t.md)
  A type that stores information about a frame’s encoding, rendering, and presentation deadlines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_frame_predict_timing)*