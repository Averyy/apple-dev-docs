# maxRenderQuality

**Framework**: Compositor Services  
**Kind**: property

The max render quality the layer can use when drawing to the drawables.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var maxRenderQuality: LayerRenderer.RenderQuality { get set }
```

## Mentions

- [Defining layer renderer quality](defining-layer-renderer-quality.md)

#### Discussion

The max render quality is a value between [0, 1]. This determines the max render quality at which drawing can happen.

Setting a higher max render quality will impact the resolution that is allocated for the drawable textures. This memory will count against the app’s memory limit so should only be specified as high as renderer can reasonably achieve frame rate at. During runtime, the render quality can be changed on the layer renderer but will not impact memory usage, see `LayerRenderer.renderQuality`.

## See Also

- [var renderQuality: LayerRenderer.RenderQuality](layerrenderer/renderquality-swift.property.md)
  Get the render quality to be used by the drawables.
- [var defaultRenderQuality: LayerRenderer.RenderQuality](layerrenderer/capabilities/defaultrenderquality.md)
  The default render quality used on this platform.
- [Defining layer renderer quality](defining-layer-renderer-quality.md)
  Declare the render quality of your textures to enable high-quality rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/configuration-swift.struct/maxrenderquality)*