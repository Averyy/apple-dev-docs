# cp_layer_renderer_configuration_error_code_unsupported_tracking_areas_usage

**Framework**: Compositor Services  
**Kind**: case  
**Role**: Enumeration Case

An error that indicates the layer doesn’t support the current texture usage for tracking areas textures.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
cp_layer_renderer_configuration_error_code_unsupported_tracking_areas_usage
```

#### Discussion

Compare the value the [`cp_layer_renderer_configuration_get_tracking_areas_usage`](../cp_layer_renderer_configuration_get_tracking_areas_usage.md) function returns and make sure it has at least `MTLTextureUsageShaderRead` and does not contain `MTLTextureUsageShaderAtomic`


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_configuration_error_code/cp_layer_renderer_configuration_error_code_unsupported_tracking_areas_usage)*