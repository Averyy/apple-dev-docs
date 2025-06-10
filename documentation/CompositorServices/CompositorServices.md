# Compositor Services

**Framework**: Compositor Services  
**Kind**: module

Take control of the drawing environment and render your own content using Metal.

**Availability**:
- visionOS 1.0+

#### Overview

Compositor Services lets you draw directly to the device’s displays using Metal and your own rendering engine. Use this framework to create a fully immersive scene in your app that doesn’t require integration with the person’s surroundings.

When you present an immersive space with [`CompositorLayer`](compositorlayer.md) content from your app, you receive a [`LayerRenderer`](layerrenderer.md) with the information you need to set up your Metal drawing environment. Use the layer to start your rendering loop and deliver successive frames of content. The layer provides the timing information you need to deliver frames at the refresh rate of the display. It also provides the Metal textures and other information that you need to draw content on the device displays.

For more information about how to draw your app’s content using Metal, see [`Metal`](https://developer.apple.com/documentation/Metal).

## Topics

### App integration
- [Drawing fully immersive content using Metal](drawing-fully-immersive-content-using-metal.md)
  Create a fully immersive experience in visionOS using a custom Metal-based rendering engine.
- [Interacting with virtual content blended with passthrough](interacting-with-virtual-content-blended-with-passthrough.md)
  Present a mixed immersion style space to draw content in a person’s surroundings, and choose how upper limbs appear with respect to rendered content.
- [Rendering hover effects in Metal immersive apps](rendering_hover_effects_in_metal_immersive_apps.md)
  Change the appearance of a rendered onscreen element when a player gazes at it.
- [struct CompositorLayer](compositorlayer.md)
  A type that you use with an immersive space to display fully immersive content using Metal.
- [protocol CompositorLayerConfiguration](compositorlayerconfiguration.md)
  An interface for specifying the texture configurations and rendering behaviors to use with your Metal rendering engine.
- [struct DefaultCompositorLayerConfiguration](defaultcompositorlayerconfiguration.md)
  A type that configures the layer with the default texture configurations and rendering behaviors for the current device.
### Render-loop setup
- [class LayerRenderer](layerrenderer.md)
  A type that provides the Metal types and timing information you need to draw your content.
- [LayerRenderer.Frame](layerrenderer/frame.md)
  A type that provides access to the timing information and data types you need to render a single frame of content.
### Drawing environment
- [LayerRenderer.Drawable](layerrenderer/drawable.md)
  A type that provides the textures and information you need to draw a frame of content.
- [LayerRenderer.Drawable.View](layerrenderer/drawable/view.md)
  A type that provides information on how to render content into the frame’s textures.
### Errors
- [enum LayerRendererConfigurationError](layerrendererconfigurationerror.md)
  Errors that can occur during layer configuration.
### Articles
- [CompositorServices Functions](compositorservices-functions.md)
### Structures
- [struct TextureTopology](texturetopology.md)
  A type that specifies the organization of one of the drawable’s textures.
### Type Aliases
- [typealias cp_drawable_array_t](cp_drawable_array_t.md)
  An opaque type that contains the drawable types and other information you need to set up your render pipeline.
- [typealias cp_hover_effect_t](cp_hover_effect_t.md)
  An opaque type that describes a hover effect of the tracking area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CompositorServices)*