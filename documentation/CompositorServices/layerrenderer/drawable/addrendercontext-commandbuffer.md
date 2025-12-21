# addRenderContext(commandBuffer:)

**Framework**: Compositor Services  
**Kind**: method

Adds and returns a render context to a `LayerRenderer.Drawable` providing a metal command buffer.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func addRenderContext(commandBuffer cmd_buffer: any MTLCommandBuffer) -> LayerRenderer.Drawable.RenderContext
```

#### Discussion

This object draws any content that the compositor needs to render in the app. The [`LayerRenderer.Drawable.RenderContext`](layerrenderer/drawable/rendercontext.md) can only be used when the layer renderer is using layered layout or on platforms that only render one view, such as the Simulator. The `RenderContext` makes use of the [`deviceAnchor`](layerrenderer/drawable/deviceanchor.md) set in [`cp_drawable_set_device_anchor`](cp_drawable_set_device_anchor.md). Only use the `deviceAnchor` in the layer renderer drawable before calling [`addRenderContext(commandBuffer:)`](layerrenderer/drawable/addrendercontext(commandbuffer:).md).

## See Also

- [LayerRenderer.Drawable.RenderContext](layerrenderer/drawable/rendercontext.md)
  An object the compositer uses for rendering all effects associated with a layer renderer drawable.
- [func addRenderContext() -> LayerRenderer.Drawable.RenderContext](layerrenderer/drawable/addrendercontext.md)
  Adds and returns a render context to a `LayerRenderer.Drawable` that draws any content required by the compositor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/addrendercontext(commandbuffer:))*