# ar_environment_probe_anchor_get_camera_scale_reference

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Get the camera scale reference of an environment probe anchor.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern float ar_environment_probe_anchor_get_camera_scale_reference(ar_environment_probe_anchor_t environment_probe);
```

## Return Value

Returns the camera scale reference of a pixel with rgb value [1,1,1] in the environment texture.

## Discussion

The environment texture stores floating point linear high-dynamic range rgb values in P3 color space. In order to have a consistent brightness between texture updates, the cameraScaleReference allows you to translate the local brightness from the current environment texture to the absolute brightness range from the camera.

## Parameters

- `environment_probe`: An environment probe anchor.

## See Also

### Environment light estimation data types
- [ar_environment_light_estimation_configuration_t](./ar_environment_light_estimation_configuration_t.md)
  Configuration for environment light estimation.
- [ar_environment_light_estimation_provider_t](./ar_environment_light_estimation_provider_t.md)
  A data provider for environment light estimation.
- [ar_environment_light_estimation_update_handler_function_t](./ar_environment_light_estimation_update_handler_function_t.md)
  Function to be called when there are updates to environment probe anchors.
- [ar_environment_light_estimation_update_handler_t](./ar_environment_light_estimation_update_handler_t.md)
  Handler triggered when there are updates to environment probe anchors.
- [ar_environment_probe_anchor_t](./ar_environment_probe_anchor_t.md)
  An anchor providing environment lighting information for realistic rendering.
- [ar_environment_probe_anchors_enumerator_function_t](./ar_environment_probe_anchors_enumerator_function_t.md)
  Function for enumerating a collection of environment probe anchors.
- [ar_environment_probe_anchors_enumerator_t](./ar_environment_probe_anchors_enumerator_t.md)
  Handler for enumerating a collection of environment probe anchors.
- [ar_environment_probe_anchors_t](./ar_environment_probe_anchors_t.md)
  A collection of environment probe anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_environment_probe_anchor_get_camera_scale_reference)*