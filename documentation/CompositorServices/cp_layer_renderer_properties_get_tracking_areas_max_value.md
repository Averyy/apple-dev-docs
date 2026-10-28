# cp_layer_renderer_properties_get_tracking_areas_max_value

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the max render value for tracking areas’ render values.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
cp_tracking_area_render_value cp_layer_renderer_properties_get_tracking_areas_max_value(cp_layer_renderer_properties_t properties);
```

## Return Value

The max render value for the tracking areas render values.

## Discussion

The layer’s configuration determines the total number of available tracking areas. This will be the max render value available, based on [`cp_layer_renderer_configuration_get_tracking_areas_format`](./cp_layer_renderer_configuration_get_tracking_areas_format.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_properties_get_tracking_areas_max_value)*