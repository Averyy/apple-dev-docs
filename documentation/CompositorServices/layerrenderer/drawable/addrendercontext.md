# addRenderContext()

**Framework**: Compositor Services  
**Kind**: method

Adds and returns a render context to a `LayerRenderer.Drawable` that draws any content required by the compositor.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func addRenderContext() -> LayerRenderer.Drawable.RenderContext
```

#### Discussion

Call `renderContext.drawMaskOnStencilAttachment(self:commandEncoder:value:)` on the returned [`LayerRenderer.Drawable.RenderContext`](layerrenderer/drawable/rendercontext.md) to render only the necessary pixels. You can only use the [`LayerRenderer.Drawable.RenderContext`](layerrenderer/drawable/rendercontext.md) API in the context of layered layout rendering or on platforms that only render one view, such as the Simulator. The `RenderContext` uses the [`deviceAnchor`](layerrenderer/drawable/deviceanchor.md) set in [`cp_drawable_set_device_anchor`](cp_drawable_set_device_anchor.md). Set the `deviceAnchor` in the layer renderer drawable before calling [`addRenderContext(commandBuffer:)`](layerrenderer/drawable/addrendercontext(commandbuffer:).md).

## See Also

- [LayerRenderer.Drawable.RenderContext](layerrenderer/drawable/rendercontext.md)
  An object the compositer uses for rendering all effects associated with a layer renderer drawable.
- [func addRenderContext(commandBuffer: any MTLCommandBuffer) -> LayerRenderer.Drawable.RenderContext](layerrenderer/drawable/addrendercontext(commandbuffer:).md)
  Adds and returns a render context to a `LayerRenderer.Drawable` providing a metal command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/addrendercontext())*