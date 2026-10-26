# cp_layer_renderer_properties_get_texture_topology_count

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the number of texture topologies available for you to inspect.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
size_t cp_layer_renderer_properties_get_texture_topology_count(cp_layer_renderer_properties_t layer_properties);
```

#### Return Value

The number of texture topologies the layer supports.

#### Discussion

The layer’s configuration determines the total number of available topologies, and each topology contains details about one texture you use for rendering. Fetch the topology details using the [`cp_layer_renderer_properties_get_texture_topology`](./cp_layer_renderer_properties_get_texture_topology.md) function.

## Parameters

- `layer_properties`: The layer properties to query.

## See Also

### Getting the layer’s texture topology
- [cp_layer_renderer_properties_get_texture_topology](./cp_layer_renderer_properties_get_texture_topology.md)
  Retrieves the texture topology at the specified index in the layer’s properties.
- [var arrayLength: UInt64](./texturetopology/arraylength.md)
  The number of items in the texture array.
- [var textureType: MTLTextureType](./texturetopology/texturetype.md)
  The texture type value that specifies how the underlying texture organizes its views.
- [cp_texture_topology_t](./cp_texture_topology_t.md)
  A type that specifies the organization of one of the drawable’s textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_properties_get_texture_topology_count)*