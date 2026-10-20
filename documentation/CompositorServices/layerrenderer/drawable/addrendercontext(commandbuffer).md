# addRenderContext(commandBuffer:)

**Framework**: Compositor Services  
**Kind**: method  
**Role**: Instance Method

Adds and returns a render context to a `LayerRenderer.Drawable` providing a metal command buffer.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func addRenderContext(commandBuffer cmd_buffer: any MTLCommandBuffer) -> LayerRenderer.Drawable.RenderContext
```

```c
cp_drawable_render_context_tcp_drawable_add_render_context(cp_drawable_t drawable, id<MTLCommandBuffer>cmd_buffer);
```

#### Discussion

This object draws any content that the compositor needs to render in the app. The [`LayerRenderer.Drawable.RenderContext`](./rendercontext.md) can only be used when the layer renderer is using layered layout or on platforms that only render one view, such as the Simulator. The `RenderContext` makes use of the [`deviceAnchor`](./deviceanchor.md) set in [`cp_drawable_set_device_anchor`](../../cp_drawable_set_device_anchor.md). Only use the `deviceAnchor` in the layer renderer drawable before calling [`addRenderContext(commandBuffer:)`](./addrendercontext%28commandbuffer%29.md).

## See Also

### Adding a render context
- [LayerRenderer.Drawable.RenderContext](./rendercontext.md)
  An object the compositer uses for rendering all effects associated with a layer renderer drawable.
- [func addRenderContext() -> LayerRenderer.Drawable.RenderContext](./addrendercontext%28%29.md)
  Adds and returns a render context to a `LayerRenderer.Drawable` that draws any content required by the compositor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/addrendercontext(commandbuffer:))*