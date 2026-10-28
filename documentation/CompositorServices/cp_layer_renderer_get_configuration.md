# cp_layer_renderer_get_configuration

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the configuration details for the specified layer.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
cp_layer_renderer_configuration_tcp_layer_renderer_get_configuration(cp_layer_renderer_t layer_renderer);
```

## Return Value

An opaque type you use to retrieve details about the layer’s configuration.

## Discussion

Use the returned information to set up your rendering loop. The layer ignores any modifications you make to the specified configuration data. To properly configure the layer, specify those details in the initializer for your immersive space’s content.

## Parameters

- `layer_renderer`: The layer that contains the configuration details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_get_configuration)*