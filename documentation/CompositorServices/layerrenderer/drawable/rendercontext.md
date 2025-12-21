# LayerRenderer.Drawable.RenderContext

**Framework**: Compositor Services  
**Kind**: struct

An object the compositer uses for rendering all effects associated with a layer renderer drawable.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct RenderContext
```

#### Overview

A `RenderContext` is required for apps to render using the progressive immersion style.

## Topics

### Rendering with Metal 4
- [func drawMaskOnStencilAttachment(commandEncoder: any MTL4RenderCommandEncoder, value: UInt8)](layerrenderer/drawable/rendercontext/drawmaskonstencilattachment(commandencoder:value:)-7npim.md)
  Store the value parameter in the stencil texture in the pixels that the Compositor displays onscreen.
- [func endEncoding(commandEncoder: any MTL4RenderCommandEncoder)](layerrenderer/drawable/rendercontext/endencoding(commandencoder:)-2l6lk.md)
  Finish encoding the render context.
### Rendering with Metal
- [func drawMaskOnStencilAttachment(commandEncoder: any MTLRenderCommandEncoder, value: UInt8)](layerrenderer/drawable/rendercontext/drawmaskonstencilattachment(commandencoder:value:)-65i67.md)
  Store the value parameter in the stencil texture in the pixels that the compositor will display onscreen.
- [func endEncoding(commandEncoder: any MTLRenderCommandEncoder)](layerrenderer/drawable/rendercontext/endencoding(commandencoder:)-4hx0m.md)
  Finish encoding the render context.
### Initializers
- [init()](layerrenderer/drawable/rendercontext/init.md)
  Creates a new render context.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [func addRenderContext(commandBuffer: any MTLCommandBuffer) -> LayerRenderer.Drawable.RenderContext](layerrenderer/drawable/addrendercontext(commandbuffer:).md)
  Adds and returns a render context to a `LayerRenderer.Drawable` providing a metal command buffer.
- [func addRenderContext() -> LayerRenderer.Drawable.RenderContext](layerrenderer/drawable/addrendercontext.md)
  Adds and returns a render context to a `LayerRenderer.Drawable` that draws any content required by the compositor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/rendercontext)*