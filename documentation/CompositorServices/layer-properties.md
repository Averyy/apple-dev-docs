# Layer properties

**Framework**: Compositor Services  
**Role**: API Collection

Information about the textures and views that the system created for your drawing code.

## Overview

At layer-creation time, the system constructs the textures you use for drawing and stores information about those textures in the layer’s properties. Use that information to configure your render pipeline and set up any app-specific data structures. For example, use the information to get the size and type of the textures. If you want to set up your app’s render pipeline before the layer is available, create a `cp_layer_properties_t` type from the same configuration details you use to construct the layer.

## Topics

### Getting view port information
- [var viewport: MTLViewport](./layerrenderer/drawable/view/texturemap-swift.struct/viewport.md)
  The portion of the texture that the view uses to draw its content.
- [cp_layer_renderer_properties_get_view_count](./cp_layer_renderer_properties_get_view_count.md)
  Returns the number of views that you must fill with content.
### Getting the layer’s texture topology
- [var arrayLength: UInt64](./texturetopology/arraylength.md)
  The number of items in the texture array.
- [var textureType: MTLTextureType](./texturetopology/texturetype.md)
  The texture type value that specifies how the underlying texture organizes its views.
- [cp_layer_renderer_properties_get_texture_topology_count](./cp_layer_renderer_properties_get_texture_topology_count.md)
  Returns the number of texture topologies available for you to inspect.
- [cp_layer_renderer_properties_get_texture_topology](./cp_layer_renderer_properties_get_texture_topology.md)
  Retrieves the texture topology at the specified index in the layer’s properties.
- [cp_texture_topology_t](./cp_texture_topology_t.md)
  A type that specifies the organization of one of the drawable’s textures.
### Getting a layer’s properties
- [cp_layer_renderer_get_properties](./cp_layer_renderer_get_properties.md)
  Returns the configured properties of the specified layer.
- [cp_layer_renderer_properties_t](./cp_layer_renderer_properties_t.md)
  A type that describes the organization of the layer’s textures and the relationships between those textures and the views you use for drawing.
### Creating new layer properties
- [cp_layer_renderer_properties_create_using_configuration](./cp_layer_renderer_properties_create_using_configuration.md)
  Creates a new opaque type to store layer-related properties.

## See Also

### Configuring the layer
- [Layer capabilities](./layer-capabilities.md)
  The color formats, depth formats, and features that you can use to configure your rendering engine.
- [Layer configuration](./layer-configuration.md)
  The pixel formats, depth mask, texture layout, and other drawing-related settings you use to configure your drawing code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layer-properties)*