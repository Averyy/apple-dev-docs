# cp_frame_timing_get_rendering_deadline

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the time at which you must finish all work for the specified frame.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
cp_time_t cp_frame_timing_get_rendering_deadline(cp_frame_timing_t frame_timing);
```

#### Return Value

The Mach absolute time at which you must finish all work and commit your command buffers to the GPU.

#### Discussion

This value reflects the time you need to finish your work and deliver the frame to the system. Finish all CPU tasks, commit your Metal command buffers, and call [`endSubmission()`](./layerrenderer/frame/endsubmission%28%29.md) by the specified time. This time is before the actual presentation time of the frame, because it accounts for the Compositor Services overhead needed to render your frame and display it.

## Parameters

- `frame_timing`: The frame’s timing information. Fetch this information using the [`cp_frame_predict_timing`](./cp_frame_predict_timing.md) function. After you retrieve the frame’s drawable type, get the information using [`frameTiming`](./layerrenderer/drawable/frametiming.md) instead.

## See Also

### Getting timing information
- [cp_frame_predict_timing](./cp_frame_predict_timing.md)
  Computes and returns the predicted timing information for the frame.
- [cp_frame_timing_get_optimal_input_time](./cp_frame_timing_get_optimal_input_time.md)
  Returns the optimal time to start the frame submission process.
- [cp_frame_timing_get_presentation_time](./cp_frame_timing_get_presentation_time.md)
  Returns the time at which the system displays the frame.
- [cp_frame_timing_t](./cp_frame_timing_t.md)
  A type that stores information about a frame’s encoding, rendering, and presentation deadlines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_frame_timing_get_rendering_deadline)*