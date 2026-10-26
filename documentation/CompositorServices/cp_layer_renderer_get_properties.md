# cp_layer_renderer_get_properties

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the configured properties of the specified layer.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
cp_layer_renderer_properties_tcp_layer_renderer_get_properties(cp_layer_renderer_t layer_renderer);
```

#### Return Value

An opaque type you use to retrieve the property details.

#### Discussion

The layer properties include details about the layer’s textures, such as their organization and the location of drawable views in those textures.

## Parameters

- `layer_renderer`: The layer to query.

## See Also

### Getting a layer’s properties
- [cp_layer_renderer_properties_t](./cp_layer_renderer_properties_t.md)
  A type that describes the organization of the layer’s textures and the relationships between those textures and the views you use for drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_get_properties)*