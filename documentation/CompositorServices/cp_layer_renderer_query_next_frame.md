# cp_layer_renderer_query_next_frame

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the next frame to use for drawing.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
cp_frame_tcp_layer_renderer_query_next_frame(cp_layer_renderer_t layer_renderer);
```

## Return Value

A frame type to use for drawing operations. The function returns `nil` if the layer is paused, invalidated, or has too many frames already in use.

## Discussion

This function retrieves the next frame for you to use in your drawing operations. The system maintains a limited number of frames, so don’t try to render more than one frame in advance. If this function returns `nil`, wait a short time and try again. When the system finishes displaying a rendered frame onscreen, it returns that frame to the shared pool and makes it available for you to use again.

The index of each returned frame is always greater than the index of the previous frame. The system increments index values sequentially so you can differentiate frames you are currently drawing.

## Parameters

- `layer_renderer`: The layer that manages the drawing destination.

## See Also

### Drawing a frame of content
- [typealias LayerFrameIndex](./layerframeindex.md)
  A frame index in the layer’s timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_query_next_frame)*