# cp_frame_timing_t

**Framework**: Compositor Services  
**Kind**: typealias  
**Role**: Type Alias

A type that stores information about a frame’s encoding, rendering, and presentation deadlines.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
typedef struct cp_frame_timing * cp_frame_timing_t;
```

#### Discussion

Before you start drawing your frame’s content, retrieve the frame’s timing information using [`cp_frame_predict_timing`](./cp_frame_predict_timing.md). That function returns the latest predicted values for you to use during planning. After you retrieve the [`cp_drawable_t`](./cp_drawable_t.md) type for the frame, get the timing information from the drawable instead using [`frameTiming`](./layerrenderer/drawable/frametiming.md).

## See Also

### Getting timing information
- [cp_frame_predict_timing](./cp_frame_predict_timing.md)
  Computes and returns the predicted timing information for the frame.
- [cp_frame_timing_get_optimal_input_time](./cp_frame_timing_get_optimal_input_time.md)
  Returns the optimal time to start the frame submission process.
- [cp_frame_timing_get_rendering_deadline](./cp_frame_timing_get_rendering_deadline.md)
  Returns the time at which you must finish all work for the specified frame.
- [cp_frame_timing_get_presentation_time](./cp_frame_timing_get_presentation_time.md)
  Returns the time at which the system displays the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_frame_timing_t)*