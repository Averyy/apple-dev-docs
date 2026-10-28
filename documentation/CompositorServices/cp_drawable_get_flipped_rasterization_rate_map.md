# cp_drawable_get_flipped_rasterization_rate_map

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the flipped rasterization rate map at the specified index in the drawable.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
id<MTLRasterizationRateMap>cp_drawable_get_flipped_rasterization_rate_map(cp_drawable_t drawable, size_t index);
```

## Return Value

The flipped rasterization rate map at the specified index.

## Discussion

Use this function to retrieve a rasterization rate map flipped around the y-axis. Apply a flipped rasterization rate map to your render descriptor when you set up your drawing environment. Rasterization rate maps define how the GPU scales different parts of the texture to fill the display. You use them to save time and render less important parts of your scene at lower resolutions. For example, the drawable includes a rasterization rate map to render the portions of the texture in someone’s peripheral vision at a lower resolution. Flipped rasterization rate maps are available only when foveation is enabled and the [`cp_layer_renderer_configuration_get_generate_flipped_rasterization_rate_maps`](./cp_layer_renderer_configuration_get_generate_flipped_rasterization_rate_maps.md) function of your layer configuration returns `true`.

## Parameters

- `drawable`: The drawable for a frame.
- `index`: The index of the flipped rasterization rate map you want. The index must be greater than or equal to `0` and less than the value that [`cp_drawable_get_rasterization_rate_map_count`](./cp_drawable_get_rasterization_rate_map_count.md) returns.

## See Also

### Getting the rasterization rate map
- [cp_drawable_get_rasterization_rate_map_count](./cp_drawable_get_rasterization_rate_map_count.md)
  Returns the number of rasterization rate maps associated with the drawable.
- [cp_drawable_get_rasterization_rate_map](./cp_drawable_get_rasterization_rate_map.md)
  Returns the rasterization rate map at the specified index in the drawable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_drawable_get_flipped_rasterization_rate_map)*