# drawableRenderContextSupportedStencilFormats

**Framework**: Compositor Services  
**Kind**: property  
**Role**: Instance Property

An array of metal pixel formats the layer renderer drawable supports with its render context.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var drawableRenderContextSupportedStencilFormats: [MTLPixelFormat] { get }
```

## Discussion

The pixel formats in this property tell you which [`MTLPixelFormat`](../../../Metal/mtlpixelformat.md) pixel arrangements and characteristics the layer supports for its stencil textures with the `RenderContext`.

> **Note**: Pixel formats are further detailed in [Metal Feature Set Tables](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf).


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/capabilities/drawablerendercontextsupportedstencilformats)*