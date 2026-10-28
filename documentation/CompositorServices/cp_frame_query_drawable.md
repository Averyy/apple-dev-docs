# cp_frame_query_drawable

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the drawable type you use to retrieve the textures and drawing environment for the frame.

**Availability**:
- visionOS 1.0+ - Deprecated in 26.0

## Declaration

```c
cp_drawable_tcp_frame_query_drawable(cp_frame_t frame);
```

## Return Value

The drawable type, or `nil` if the layer is in the [`LayerRenderer.State.paused`](./layerrenderer/state-swift.enum/paused.md) or [`LayerRenderer.State.invalidated`](./layerrenderer/state-swift.enum/invalidated.md) state.

## Discussion

Fetch the drawable when you’re ready to encode the drawing commands for the frame. The [`cp_drawable_t`](./cp_drawable_t.md) type contains the textures and other information you need to set up your render descriptor in Metal.

## Parameters

- `frame`: The frame to query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_frame_query_drawable)*