# ar_environment_light_estimation_update_handler_t

**Framework**: ARKit  
**Kind**: typealias  
**Role**: Type Alias

Handler triggered when there are updates to environment probe anchors.

**Availability**:
- visionOS 2.0+

## Declaration

```c
typedef void (^)(NSObject<OS_ar_environment_probe_anchors> *, NSObject<OS_ar_environment_probe_anchors> *, NSObject<OS_ar_environment_probe_anchors> *) ar_environment_light_estimation_update_handler_t;
```

## Parameters

- `added_anchors`: Collection of anchors that are added.
- `updated_anchors`: Collection of anchors that are updated.
- `removed_anchors`: Collection of anchors that are removed.

## See Also

### Environment light estimation data types
- [ar_environment_light_estimation_configuration_t](./ar_environment_light_estimation_configuration_t.md)
  Configuration for environment light estimation.
- [ar_environment_light_estimation_provider_t](./ar_environment_light_estimation_provider_t.md)
  A data provider for environment light estimation.
- [ar_environment_light_estimation_update_handler_function_t](./ar_environment_light_estimation_update_handler_function_t.md)
  Function to be called when there are updates to environment probe anchors.
- [ar_environment_probe_anchor_t](./ar_environment_probe_anchor_t.md)
  An anchor providing environment lighting information for realistic rendering.
- [ar_environment_probe_anchors_enumerator_function_t](./ar_environment_probe_anchors_enumerator_function_t.md)
  Function for enumerating a collection of environment probe anchors.
- [ar_environment_probe_anchors_enumerator_t](./ar_environment_probe_anchors_enumerator_t.md)
  Handler for enumerating a collection of environment probe anchors.
- [ar_environment_probe_anchors_t](./ar_environment_probe_anchors_t.md)
  A collection of environment probe anchors.
- [ar_environment_probe_anchor_get_camera_scale_reference](./ar_environment_probe_anchor_get_camera_scale_reference.md)
  Get the camera scale reference of an environment probe anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_environment_light_estimation_update_handler_t)*