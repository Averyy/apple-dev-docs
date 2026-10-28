# textureType

**Framework**: Compositor Services  
**Kind**: property  
**Role**: Instance Property

The texture type value that specifies how the underlying texture organizes its views.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var textureType: MTLTextureType { get }
```

```c
MTLTextureType cp_texture_topology_get_texture_type(cp_texture_topology_t texture_topology);
```

## Discussion

A texture might store the content of one view or multiple views. For example, a single texture might store one or both views for the left and right eyes of a head-mounted display. The texture type indicates this content organization strategy.

## See Also

### Getting the layer’s texture topology
- [var arrayLength: UInt64](./arraylength.md)
  The number of items in the texture array.
- [cp_layer_renderer_properties_get_texture_topology_count](../cp_layer_renderer_properties_get_texture_topology_count.md)
  Returns the number of texture topologies available for you to inspect.
- [cp_layer_renderer_properties_get_texture_topology](../cp_layer_renderer_properties_get_texture_topology.md)
  Retrieves the texture topology at the specified index in the layer’s properties.
- [cp_texture_topology_t](../cp_texture_topology_t.md)
  A type that specifies the organization of one of the drawable’s textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/texturetopology/texturetype)*