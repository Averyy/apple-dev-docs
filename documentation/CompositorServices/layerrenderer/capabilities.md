# LayerRenderer.Capabilities

**Framework**: Compositor Services  
**Kind**: struct

The color formats, depth formats, and features that you can use to configure your rendering engine.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct Capabilities
```

#### Overview

A [`LayerRenderer.Capabilities`](layerrenderer/capabilities.md) type provides information about the capabilities of the current device. Simulator and devices support different sets of options. Use the information in this type to specify the configuration details for your layer.

## Topics

### Getting the supported formats
- [var supportedColorFormats: [MTLPixelFormat]](layerrenderer/capabilities/supportedcolorformats.md)
  An array of color formats that the layer supports for its textures.
- [var supportedDepthFormats: [MTLPixelFormat]](layerrenderer/capabilities/supporteddepthformats.md)
  The list of depth formats that the layer supports
### Getting the supported layouts
- [func supportedLayouts(options: LayerRenderer.Capabilities.SupportedLayoutsOptions) -> [LayerRenderer.Layout]](layerrenderer/capabilities/supportedlayouts(options:).md)
  Returns an array of texture layouts that the layer supports.
- [LayerRenderer.Capabilities.SupportedLayoutsOptions](layerrenderer/capabilities/supportedlayoutsoptions.md)
  Options you can use to filter the supported layouts for a layer.
### Getting the supported layer features
- [var supportsFoveation: Bool](layerrenderer/capabilities/supportsfoveation.md)
  A Boolean value that indicates whether the layer supports variable rasterization rates.
### Getting the minimum near plane distance
- [var supportedMinimumNearPlaneDistance: Float](layerrenderer/capabilities/supportedminimumnearplanedistance.md)
  The minimum distance in meters to the layer’s near projection plane.
### Determining supported stencil formats
- [var drawableRenderContextSupportedStencilFormats: [MTLPixelFormat]](layerrenderer/capabilities/drawablerendercontextsupportedstencilformats.md)
  An array of metal pixel formats the layer renderer drawable supports with its render context.
### Getting render quality
- [var defaultRenderQuality: LayerRenderer.RenderQuality](layerrenderer/capabilities/defaultrenderquality.md)
  The default render quality used on this platform.
### Structures
- [LayerRenderer.Capabilities.SupportedColorFormatsOptions](layerrenderer/capabilities/supportedcolorformatsoptions.md)
  Options you can use to filter the supported color formats for a layer textures.
### Instance Properties
- [var supportedTrackingAreasFormats: [MTLPixelFormat]](layerrenderer/capabilities/supportedtrackingareasformats.md)
  An array of tracking areas formats that the layer supports for its textures.
### Instance Methods
- [func supportedColorFormats(options: LayerRenderer.Capabilities.SupportedColorFormatsOptions) -> [MTLPixelFormat]](layerrenderer/capabilities/supportedcolorformats(options:).md)
  Returns an array of formats that the layer supports for its color textures

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)

## See Also

- [var configuration: LayerRenderer.Configuration](layerrenderer/configuration-swift.property.md)
  The configuration details for the specified layer.
- [LayerRenderer.Configuration](layerrenderer/configuration-swift.struct.md)
  A type that stores the texture formats, layout information, and other details you use to configure your rendering loop code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/capabilities)*