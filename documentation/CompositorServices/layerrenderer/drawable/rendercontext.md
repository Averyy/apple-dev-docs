# LayerRenderer.Drawable.RenderContext

**Framework**: Compositor Services  
**Kind**: struct

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct RenderContext
```

## Topics

### Initializers
- [init()](layerrenderer/drawable/rendercontext/init.md)
### Instance Methods
- [func drawMaskOnStencilAttachment(commandEncoder: any MTLRenderCommandEncoder, value: UInt8)](layerrenderer/drawable/rendercontext/drawmaskonstencilattachment(commandencoder:value:)-65i67.md)
  Store the `value` parameter in the stencil texture in the pixels that Compositor will display on the screen.
- [func drawMaskOnStencilAttachment(commandEncoder: any MTL4RenderCommandEncoder, value: UInt8)](layerrenderer/drawable/rendercontext/drawmaskonstencilattachment(commandencoder:value:)-7npim.md)
  Store the `value` parameter in the stencil texture in the pixels that Compositor will display on the screen.
- [func endEncoding(commandEncoder: any MTL4RenderCommandEncoder)](layerrenderer/drawable/rendercontext/endencoding(commandencoder:)-2l6lk.md)
  Finish encoding the render context.
- [func endEncoding(commandEncoder: any MTLRenderCommandEncoder)](layerrenderer/drawable/rendercontext/endencoding(commandencoder:)-4hx0m.md)
  Finish encoding the render context.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/rendercontext)*