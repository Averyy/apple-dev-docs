# cp_layer_renderer_capabilities_supports_foveation

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether the layer supports variable rasterization rates.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
bool cp_layer_renderer_capabilities_supports_foveation(cp_layer_renderer_capabilities_t layer_capabilities);
```

#### Return Value

`true` if the layer supports variable rasterization rates or `false` if you must render the entire layer at the same resolution.

#### Discussion

Foveation support lets you reduce the amount of high-resolution drawing you do. When foveation support is available, the system provides a variable rasterization rate map that defines the content resolution in different parts of the texture. This map allows you to render content in someone’s peripheral vision at a lower resolution than content in the center of their vision.

## Parameters

- `layer_capabilities`: The layer capabilities to query.

## See Also

### Getting the supported features
- [cp_layer_renderer_capabilities_supported_minimum_near_plane_distance](./cp_layer_renderer_capabilities_supported_minimum_near_plane_distance.md)
  Returns the minimum distance in meters to the layer’s near projection plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_capabilities_supports_foveation)*