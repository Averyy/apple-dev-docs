# cp_frame_t

**Framework**: Compositor Services  
**Kind**: typealias  
**Role**: Type Alias

A type that provides access to the timing information and data types you need to render a single frame of content.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
typedef struct cp_frame * cp_frame_t;
```

## Discussion

A frame represents a snapshot of your app’s content at a single moment in time. In your rendering loop, you render your content into static images many times a second to create the illusion of animation. A [`cp_frame_t`](./cp_frame_t.md) provides the Metal textures and information you need to render one of those images.

During each iteration of your app’s rendering loop, call `cp_layer_query_next_frame` to retrieve the next frame to render The system manages a finite number of frames and recycles them to maximize efficiency. You typically draw only one frame at a time, starting work on each new frame only after completing the previous frame.

Separate the work you do for each frame into two phases: the update phase and the encode phase. Use the update phase to perform tasks that don’t depend on the current device pose. For example, you might update your app’s data structures to reflect recent interactions with your content. Use the submission phase to retrieve the current pose and render the frame’s content using that information. Each frame provides a [`cp_drawable_t`](./cp_drawable_t.md) type with access to the specific textures and rendering details for that frame.

## Topics

### Getting timing information
- [cp_frame_predict_timing](./cp_frame_predict_timing.md)
  Computes and returns the predicted timing information for the frame.
- [cp_frame_timing_t](./cp_frame_timing_t.md)
  A type that stores information about a frame’s encoding, rendering, and presentation deadlines.
### Reporting frame update times
- [func startUpdate()](./layerrenderer/frame/startupdate%28%29.md)
  Notifies Compositor Services that you started updating the app-specific content for the frame.
- [func endUpdate()](./layerrenderer/frame/endupdate%28%29.md)
  Notifies Compositor Services that you finished updating the app-specific content you need to render the frame.
### Getting the drawable environment
- [cp_frame_query_drawable](./cp_frame_query_drawable.md)
  Returns the drawable type you use to retrieve the textures and drawing environment for the frame.
### Reporting frame submission times
- [func startSubmission()](./layerrenderer/frame/startsubmission%28%29.md)
  Notifies Compositor Services that you’re ready to generate the Metal commands to render the specified frame.
- [func endSubmission()](./layerrenderer/frame/endsubmission%28%29.md)
  Notifies Compositor Services that you finished generating the GPU commands to render the specified frame.
### Getting frame-related details
- [var frameIndex: LayerFrameIndex](./layerrenderer/frame/frameindex.md)
  The sequential index number of a frame.

## See Also

### Getting frame-related details
- [var frameIndex: LayerFrameIndex](./layerrenderer/frame/frameindex.md)
  The sequential index number of a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_frame_t)*