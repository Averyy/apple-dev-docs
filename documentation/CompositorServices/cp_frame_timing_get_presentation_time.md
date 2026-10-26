# cp_frame_timing_get_presentation_time

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the time at which the system displays the frame.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
cp_time_t cp_frame_timing_get_presentation_time(cp_frame_timing_t frame_timing);
```

#### Return Value

The Mach absolute time at which the layer presents the frame.

#### Discussion

You can use the presentation time as a synchronization point for other parts of your app. For example, if you play an audio clip when the frame appears, configure your code to start playing the clip at the specified time.

## Parameters

- `frame_timing`: The frame’s timing information. Fetch this information using the [`cp_frame_predict_timing`](./cp_frame_predict_timing.md) function. After you retrieve the frame’s drawable type, get the information using [`frameTiming`](./layerrenderer/drawable/frametiming.md) instead.

## See Also

### Getting timing information
- [cp_frame_predict_timing](./cp_frame_predict_timing.md)
  Computes and returns the predicted timing information for the frame.
- [cp_frame_timing_get_optimal_input_time](./cp_frame_timing_get_optimal_input_time.md)
  Returns the optimal time to start the frame submission process.
- [cp_frame_timing_get_rendering_deadline](./cp_frame_timing_get_rendering_deadline.md)
  Returns the time at which you must finish all work for the specified frame.
- [cp_frame_timing_t](./cp_frame_timing_t.md)
  A type that stores information about a frame’s encoding, rendering, and presentation deadlines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_frame_timing_get_presentation_time)*