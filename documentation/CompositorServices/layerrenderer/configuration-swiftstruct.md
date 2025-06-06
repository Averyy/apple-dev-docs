# LayerRenderer.Configuration

**Framework**: Compositor Services  
**Kind**: struct

A type that stores the texture formats, layout information, and other details you use to configure your rendering loop code.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct Configuration
```

#### Overview

A [`LayerRenderer.Configuration`](layerrenderer/configuration-swift.struct.md) type stores the configuration options for your app’s [`LayerRenderer`](layerrenderer.md) object. When configuring your app’s [`CompositorLayer`](compositorlayer.md) type, use this type to specify information about the texture layouts, pixel formats, and rendering options you want. The system uses the provided information to initialize the [`LayerRenderer`](layerrenderer.md) object. It also uses the information to create the Metal textures and other data structures that you use for each frame of content.

You don’t create this type directly. When implementing the [`makeConfiguration(capabilities:configuration:)`](compositorlayerconfiguration/makeconfiguration(capabilities:configuration:).md) method of your [`CompositorLayerConfiguration`](compositorlayerconfiguration.md) type, the system passes a set of default configuration values for you to modify.

## Topics

### Configuring the color textures
- [var colorFormat: MTLPixelFormat](layerrenderer/configuration-swift.struct/colorformat.md)
  The pixel format to use for color textures.
- [var colorUsage: MTLTextureUsage](layerrenderer/configuration-swift.struct/colorusage.md)
  The texture usage value to apply to the layer’s color textures.
### Configuring the depth information
- [var depthFormat: MTLPixelFormat](layerrenderer/configuration-swift.struct/depthformat.md)
  The pixel format to use for the layer’s depth textures.
- [var depthUsage: MTLTextureUsage](layerrenderer/configuration-swift.struct/depthusage.md)
  The texture usage value to apply to the layer’s depth textures.
- [var defaultDepthRange: SIMD2<Float>](layerrenderer/configuration-swift.struct/defaultdepthrange.md)
  The distances to the far and near clipping planes that define the bounds of your content.
### Configuring the texture layout
- [var layout: LayerRenderer.Layout](layerrenderer/configuration-swift.struct/layout.md)
  The layout being used by the layer.
- [LayerRenderer.Layout](layerrenderer/layout.md)
  Constants that specify the organization of the textures you use for drawing.
### Configuring the foveation setting
- [var isFoveationEnabled: Bool](layerrenderer/configuration-swift.struct/isfoveationenabled.md)
  A value that indicates if the layer is using variable rasterization rates.
- [var generateFlippedRasterizationRateMaps: Bool](layerrenderer/configuration-swift.struct/generateflippedrasterizationratemaps.md)
  A Boolean value that indicates whether the layer renderer provides rasterization rate maps flipped around the y-axis.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)

## See Also

- [var configuration: LayerRenderer.Configuration](layerrenderer/configuration-swift.property.md)
  The configuration details for the specified layer.
- [LayerRenderer.Capabilities](layerrenderer/capabilities.md)
  The color formats, depth formats, and features that you can use to configure your rendering engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/configuration-swift.struct)*