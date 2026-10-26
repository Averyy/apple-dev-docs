# cp_frame_query_drawables

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the drawable array type you use to retrieve the drawables for drawing environment for the frame.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
cp_drawable_array_tcp_frame_query_drawables(cp_frame_t frame);
```

#### Return Value

The drawable array type, if the layer is in the `cp_layer_renderer/cp_layer_renderer_state_paused` or `cp_layer_renderer/cp_layer_renderer_state_invalidated` states the array will have a count of 0 and frame is invalid.

#### Discussion

Call this function when you’re ready to encode the drawing commands for the frame. The [`cp_drawable_t`](./cp_drawable_t.md) type contains the textures and other information you need to set up your render descriptor in Metal. See [`target`](./layerrenderer/drawable/target-swift.property.md) for how each drawable will be used.

If array count is 0, the frame has been cancelled as there are no drawables to draw to and the frame should be discarded and is invalid to access.

Note: This function isn’t safe to be called concurrently. Always ensure a single thread call this function at a time.

## Parameters

- `frame`: The frame to query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_frame_query_drawables)*