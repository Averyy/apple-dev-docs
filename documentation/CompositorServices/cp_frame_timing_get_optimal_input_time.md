# cp_frame_timing_get_optimal_input_time

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the optimal time to start the frame submission process.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
cp_time_t cp_frame_timing_get_optimal_input_time(cp_frame_timing_t frame_timing);
```

#### Return Value

The Mach absolute time at which to query the input for your frame.

#### Discussion

The optimal input time is the time at which to call the [`startSubmission()`](./layerrenderer/frame/startsubmission%28%29.md) function. Use the time before the input time to update your app’s data structures and prepare for rendering. Call [`cp_time_wait_until`](./cp_time_wait_until.md) to suspend your app until the optimal time arrives. When it does, fetch the current device pose and finish rendering and the frame and commit your Metal command buffers.

## Parameters

- `frame_timing`: The frame’s timing information. Fetch this information using the [`cp_frame_predict_timing`](./cp_frame_predict_timing.md) function. After you retrieve the frame’s drawable type, get the information using [`frameTiming`](./layerrenderer/drawable/frametiming.md) instead.

## See Also

### Getting timing information
- [cp_frame_predict_timing](./cp_frame_predict_timing.md)
  Computes and returns the predicted timing information for the frame.
- [cp_frame_timing_get_rendering_deadline](./cp_frame_timing_get_rendering_deadline.md)
  Returns the time at which you must finish all work for the specified frame.
- [cp_frame_timing_get_presentation_time](./cp_frame_timing_get_presentation_time.md)
  Returns the time at which the system displays the frame.
- [cp_frame_timing_t](./cp_frame_timing_t.md)
  A type that stores information about a frame’s encoding, rendering, and presentation deadlines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_frame_timing_get_optimal_input_time)*