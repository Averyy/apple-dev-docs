# cp_texture_topology_t

**Framework**: Compositor Services  
**Kind**: typealias  
**Role**: Type Alias

A type that specifies the organization of one of the drawable’s textures.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
typedef struct cp_texture_topology * cp_texture_topology_t;
```

## Discussion

Metal supports multiple organizations for the textures you use for drawing. Use this type to identify one of the organizations available to use in your app.

## Topics

### Getting the topology type
- [var textureType: MTLTextureType](./texturetopology/texturetype.md)
  The texture type value that specifies how the underlying texture organizes its views.
### Getting the array length
- [var arrayLength: UInt64](./texturetopology/arraylength.md)
  The number of items in the texture array.

## See Also

### Getting the layer’s texture topology
- [cp_layer_renderer_properties_get_texture_topology_count](./cp_layer_renderer_properties_get_texture_topology_count.md)
  Returns the number of texture topologies available for you to inspect.
- [cp_layer_renderer_properties_get_texture_topology](./cp_layer_renderer_properties_get_texture_topology.md)
  Retrieves the texture topology at the specified index in the layer’s properties.
- [var arrayLength: UInt64](./texturetopology/arraylength.md)
  The number of items in the texture array.
- [var textureType: MTLTextureType](./texturetopology/texturetype.md)
  The texture type value that specifies how the underlying texture organizes its views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_texture_topology_t)*