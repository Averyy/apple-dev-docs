# ar_object_tracking_provider_set_update_handler

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Set the handler for receiving object tracking updates.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern void ar_object_tracking_provider_set_update_handler(ar_object_tracking_provider_t object_tracking_provider, dispatch_queue_t object_tracking_updates_queue, ar_object_tracking_update_handler_t object_tracking_update_handler);
```

## Discussion

> **Note**: Setting this handler will override the function set using `ar_object_tracking_provider_set_update_handler_f`.

## Parameters

- `object_tracking_provider`: The object tracking provider.
- `object_tracking_updates_queue`: The queue on which the handler will be called. Passing `NULL` will default to the main queue.
- `object_tracking_update_handler`: The handler to be called when new object tracking data arrives.

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
- [ar_reference_object_load_from_url](./ar_reference_object_load_from_url.md)
  Load a reference object from a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_object_tracking_provider_set_update_handler)*