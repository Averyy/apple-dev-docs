# drawableRenderContextStencilFormat

**Framework**: Compositor Services  
**Kind**: property  
**Role**: Instance Property

The metal pixel format matching that of the stencil texture used in the layer renderer drawable’s render context.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var drawableRenderContextStencilFormat: MTLPixelFormat { get set }
```

## Discussion

This value corresponds to the pixel format of the stencil texture you attach to your Metal pipeline.

> **Note**: For more information, see [`MTLRenderPassAttachmentDescriptor`](../../../Metal/mtlrenderpassattachmentdescriptor.md).

## See Also

### Configurating the render context
- [var drawableRenderContextRasterSampleCount: Int](./drawablerendercontextrastersamplecount.md)
  The multisample antialiasing sample count used for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/configuration-swift.struct/drawablerendercontextstencilformat)*