# defaultRenderQuality

**Framework**: Compositor Services  
**Kind**: property  
**Role**: Instance Property

The default render quality used on this platform.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var defaultRenderQuality: LayerRenderer.RenderQuality { get }
```

## Mentions

- [Defining layer renderer quality](../../defining-layer-renderer-quality.md)

#### Discussion

This should be used as the base render quality value for the platform.

Use it to decide your maximum render quality, see `LayerRenderer.Configuration.maxRenderQuality`.

## See Also

### Defining quality level
- [var renderQuality: LayerRenderer.RenderQuality](../renderquality-swift.property.md)
  Get the render quality to be used by the drawables.
- [var maxRenderQuality: LayerRenderer.RenderQuality](../configuration-swift.struct/maxrenderquality.md)
  The max render quality the layer can use when drawing to the drawables.
- [Defining layer renderer quality](../../defining-layer-renderer-quality.md)
  Declare the render quality of your textures to enable high-quality rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/capabilities/defaultrenderquality)*