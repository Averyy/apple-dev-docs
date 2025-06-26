# drawableRenderContextSupportedStencilFormats

**Framework**: Compositor Services  
**Kind**: property

An array of stencil formats that the layer supports with its drawable render context.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var drawableRenderContextSupportedStencilFormats: [MTLPixelFormat] { get }
```

#### Discussion

The pixel formats in this property tell you which pixel arrangements and characteristics the layer supports for its stencil textures with the `LayerRenderer.Drawable.RenderContext`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/capabilities/drawablerendercontextsupportedstencilformats)*