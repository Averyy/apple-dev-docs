# cp_layer_renderer_properties_create_using_configuration

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Creates a new opaque type to store layer-related properties.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
cp_layer_renderer_properties_tcp_layer_renderer_properties_create_using_configuration(cp_layer_renderer_configuration_t configuration, CFErrorRef*error);
```

#### Return Value

A new layer properties type with details about how the layer configures its topologies and texture maps. The function returns `nil` if an error occurs.

#### Discussion

Call this function to create a set of layer properties when you don’t yet have a [`LayerRenderer`](./layerrenderer.md) type. This function generates an equivalent set of properties for the configuration you provide. You can use those properties to configure other parts of your app before the layer becomes available. For example, you might use the information to configure portions of your app’s render pipeline.

## Parameters

- `configuration`: The configuration details for your layer. Compositor Services uses this information to configure the properties an equivalent layer would use.
- `error`: A pointer to an error object. On success, the function sets this value to `nil`. If an error occurs, the function sets the value of the pointer to an error object with details about what happened.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_properties_create_using_configuration)*