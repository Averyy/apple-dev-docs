# drawableRenderContextRasterSampleCount

**Framework**: Compositor Services  
**Kind**: property  
**Role**: Instance Property

The multisample antialiasing sample count used for rendering.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var drawableRenderContextRasterSampleCount: Int { get set }
```

## Mentions

- [Controlling Metal rendering immersion level](../../controlling-metal-rendering-immersion-level.md)

## Discussion

If you’re using multisample antialiasing, set the same value you attach to your Metal pipeline. [`LayerRenderer`](../../layerrenderer.md) sets the value to 1 by default.

> **Note**: For more information, see [Improving edge-rendering quality with multisample antialiasing (MSAA)](../../../Metal/improving-edge-rendering-quality-with-multisample-antialiasing-msaa.md).

## See Also

### Configurating the render context
- [var drawableRenderContextStencilFormat: MTLPixelFormat](./drawablerendercontextstencilformat.md)
  The metal pixel format matching that of the stencil texture used in the layer renderer drawable’s render context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/configuration-swift.struct/drawablerendercontextrastersamplecount)*