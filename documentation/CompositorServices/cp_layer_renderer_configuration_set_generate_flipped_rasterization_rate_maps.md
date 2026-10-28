# cp_layer_renderer_configuration_set_generate_flipped_rasterization_rate_maps

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Changes the layer renderer setting that provides rasterization rate maps flipped around the y-axis.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
void cp_layer_renderer_configuration_set_generate_flipped_rasterization_rate_maps(cp_layer_renderer_configuration_t configuration, bool generate_flipped_rasterization_rate_maps);
```

## Discussion

If foveation is disabled, the layer renderer doesn’t generate any rasterization rate maps, regardless of the value you pass to this function.

To generate flipped rasterization rate maps, the system must perform extra computational work during your app’s render loop. Enable this support only if your drawing engine requires these extra rate maps and you can afford the extra cost.

## Parameters

- `configuration`: The layer configuration details.
- `generate_flipped_rasterization_rate_maps`: `true` if you want the layer renderer to generate nonflipped rasterization rate maps. Specify `false` to generate only nonflipped rasterization rate maps.

## See Also

### Configuring the foveation setting
- [cp_layer_renderer_configuration_get_foveation_enabled](./cp_layer_renderer_configuration_get_foveation_enabled.md)
  Returns a Boolean value that indicates whether the layer supports variable rasterization rates.
- [cp_layer_renderer_configuration_set_foveation_enabled](./cp_layer_renderer_configuration_set_foveation_enabled.md)
  Changes the setting that indicates whether the layer supports variable rasterization rates.
- [cp_layer_renderer_configuration_get_generate_flipped_rasterization_rate_maps](./cp_layer_renderer_configuration_get_generate_flipped_rasterization_rate_maps.md)
  Returns a Boolean value that indicates whether the layer renderer provides rasterization rate maps flipped around the y-axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_configuration_set_generate_flipped_rasterization_rate_maps)*