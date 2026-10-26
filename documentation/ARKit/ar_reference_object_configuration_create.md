# ar_reference_object_configuration_create

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Create a reference object configuration.

**Availability**:
- visionOS 27.0+

## Declaration

```c
extern ar_reference_object_configuration_tar_reference_object_configuration_create();
```

#### Return Value

An instance of `ar_reference_object_configuration_t`.

#### Discussion

> **Note**: Default values are set as follows: - `is_high_frame_rate_tracking_enabled`: `false`

> **Note**: This type supports ARC. In non-ARC files, use `ar_retain()` and `ar_release()` to retain and release the object.

## See Also

### Object tracking
- [ar_object_tracking_provider_create](./ar_object_tracking_provider_create.md)
- [ar_object_tracking_provider_copy_all_object_anchors](./ar_object_tracking_provider_copy_all_object_anchors.md)
- [ar_object_tracking_provider_get_required_authorization_type](./ar_object_tracking_provider_get_required_authorization_type.md)
- [ar_object_tracking_provider_is_supported](./ar_object_tracking_provider_is_supported.md)
- [ar_object_tracking_provider_set_update_handler](./ar_object_tracking_provider_set_update_handler.md)
- [ar_object_tracking_provider_set_update_handler_f](./ar_object_tracking_provider_set_update_handler_f.md)
- [ar_object_tracking_error_code_t](./ar_object_tracking_error_code_t.md)
  An enumeration that describes object tracking errors.
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
- [ar_reference_object_load_from_url](./ar_reference_object_load_from_url.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_reference_object_configuration_create)*