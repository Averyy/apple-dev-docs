# addRenderContext()

**Framework**: Compositor Services  
**Kind**: method  
**Role**: Instance Method

Adds and returns a render context to a `LayerRenderer.Drawable` that draws any content required by the compositor.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func addRenderContext() -> LayerRenderer.Drawable.RenderContext
```

```c
cp_drawable_render_context_tcp_drawable_add_mtl4_render_context(cp_drawable_t drawable);
```

## Discussion

Call `renderContext.drawMaskOnStencilAttachment(self:commandEncoder:value:)` on the returned [`LayerRenderer.Drawable.RenderContext`](./rendercontext.md) to render only the necessary pixels. You can only use the [`LayerRenderer.Drawable.RenderContext`](./rendercontext.md) API in the context of layered layout rendering or on platforms that only render one view, such as the Simulator. The `RenderContext` uses the [`deviceAnchor`](./deviceanchor.md) set in [`cp_drawable_set_device_anchor`](../../cp_drawable_set_device_anchor.md). Set the `deviceAnchor` in the layer renderer drawable before calling [`addRenderContext(commandBuffer:)`](./addrendercontext%28commandbuffer%29.md).

## See Also

### Adding a render context
- [LayerRenderer.Drawable.RenderContext](./rendercontext.md)
  An object the compositer uses for rendering all effects associated with a layer renderer drawable.
- [func addRenderContext(commandBuffer: any MTLCommandBuffer) -> LayerRenderer.Drawable.RenderContext](./addrendercontext%28commandbuffer%29.md)
  Adds and returns a render context to a `LayerRenderer.Drawable` providing a metal command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/addrendercontext())*