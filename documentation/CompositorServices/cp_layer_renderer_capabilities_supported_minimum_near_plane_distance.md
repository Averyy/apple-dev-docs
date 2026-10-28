# cp_layer_renderer_capabilities_supported_minimum_near_plane_distance

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the minimum distance in meters to the layer’s near projection plane.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
float cp_layer_renderer_capabilities_supported_minimum_near_plane_distance(cp_layer_renderer_capabilities_t layer_capabilities);
```

## Return Value

The minimum allowed distance in meters from the camera origin to the near projection plane.

## Discussion

Compositor Services uses the near and far projection planes to compute the perspective projection matrix and to clip content that’s too close to the camera, or too far from it. Use this method to retrieve the minimum distance to the near plane that the layer allows. When you configure your layer, you can specify a different near-plane distance, but that value must be greater than or equal to the minimum distance.

## Parameters

- `layer_capabilities`: The layer capabilities to query.

## See Also

### Getting the supported features
- [cp_layer_renderer_capabilities_supports_foveation](./cp_layer_renderer_capabilities_supports_foveation.md)
  Returns a Boolean value that indicates whether the layer supports variable rasterization rates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_capabilities_supported_minimum_near_plane_distance)*