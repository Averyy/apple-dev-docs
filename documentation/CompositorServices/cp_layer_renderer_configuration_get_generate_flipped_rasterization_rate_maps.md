# cp_layer_renderer_configuration_get_generate_flipped_rasterization_rate_maps

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether the layer renderer provides rasterization rate maps flipped around the y-axis.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
bool cp_layer_renderer_configuration_get_generate_flipped_rasterization_rate_maps(cp_layer_renderer_configuration_t configuration);
```

#### Return Value

`true` if the layer renderer generates both flipped and nonflipped rasterization rate maps, or `false` if it generates only nonflipped rasterization rate maps.

#### Discussion

If foveation is disabled, the layer renderer doesn’t generate any rasterization rate maps, regardless of this function’s return value.

## Parameters

- `configuration`: The layer configuration details.

## See Also

### Configuring the foveation setting
- [cp_layer_renderer_configuration_get_foveation_enabled](./cp_layer_renderer_configuration_get_foveation_enabled.md)
  Returns a Boolean value that indicates whether the layer supports variable rasterization rates.
- [cp_layer_renderer_configuration_set_foveation_enabled](./cp_layer_renderer_configuration_set_foveation_enabled.md)
  Changes the setting that indicates whether the layer supports variable rasterization rates.
- [cp_layer_renderer_configuration_set_generate_flipped_rasterization_rate_maps](./cp_layer_renderer_configuration_set_generate_flipped_rasterization_rate_maps.md)
  Changes the layer renderer setting that provides rasterization rate maps flipped around the y-axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_configuration_get_generate_flipped_rasterization_rate_maps)*