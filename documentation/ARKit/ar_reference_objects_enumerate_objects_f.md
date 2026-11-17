# ar_reference_objects_enumerate_objects_f

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Enumerates a collection of reference objects using a function.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern void ar_reference_objects_enumerate_objects_f(ar_reference_objects_t reference_objects, void *context, ar_reference_objects_enumerator_function_t reference_objects_enumerator_function);
```

## Parameters

- `reference_objects`: The collection of reference objects.
- `context`: The application-defined context parameter to pass to the function.
- `reference_objects_enumerator_function`: The enumerator function.

## See Also

### Object tracking
- [ar_object_tracking_provider_create](./ar_object_tracking_provider_create.md)
  Create an object tracking provider.
- [ar_object_tracking_provider_copy_all_object_anchors](./ar_object_tracking_provider_copy_all_object_anchors.md)
  Copy all object anchors.
- [ar_object_tracking_provider_get_required_authorization_type](./ar_object_tracking_provider_get_required_authorization_type.md)
  Get the authorization type required by the object tracking provider.
- [ar_object_tracking_provider_is_supported](./ar_object_tracking_provider_is_supported.md)
  Determine whether this device supports the object tracking provider.
- [ar_object_tracking_provider_set_update_handler](./ar_object_tracking_provider_set_update_handler.md)
  Set the handler for receiving object tracking updates.
- [ar_object_tracking_provider_set_update_handler_f](./ar_object_tracking_provider_set_update_handler_f.md)
  Set the handler for receiving object tracking updates.
- [ar_object_tracking_error_code_t](./ar_object_tracking_error_code_t.md)
  Error codes that describe object tracking failures.
- [ar_reference_object_configuration_create](./ar_reference_object_configuration_create.md)
  Create a reference object configuration.
- [ar_reference_object_configuration_enable_high_frame_rate_tracking](./ar_reference_object_configuration_enable_high_frame_rate_tracking.md)
  Sets whether high-frame-rate tracking is enabled on this configuration.
- [ar_reference_object_configuration_is_equal_to_reference_object_configuration](./ar_reference_object_configuration_is_equal_to_reference_object_configuration.md)
  Returns a bool value that indicates whether the two reference object configurations are equal.
- [ar_reference_object_configuration_is_high_frame_rate_tracking_enabled](./ar_reference_object_configuration_is_high_frame_rate_tracking_enabled.md)
  Checks whether high-frame-rate tracking is enabled on this configuration.
- [ar_reference_object_load_from_url_with_configuration](./ar_reference_object_load_from_url_with_configuration.md)
  Load a reference object from a URL.
- [ar_reference_object_load_from_url_with_configuration_f](./ar_reference_object_load_from_url_with_configuration_f.md)
  Load a reference object from a URL.
- [ar_reference_object_load_with_name_and_configuration](./ar_reference_object_load_with_name_and_configuration.md)
  Load a reference object from a bundle.
- [ar_reference_object_load_with_name_and_configuration_f](./ar_reference_object_load_with_name_and_configuration_f.md)
  Load a reference object from a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_reference_objects_enumerate_objects_f)*