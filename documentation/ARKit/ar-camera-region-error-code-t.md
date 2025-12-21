# ar_camera_region_error_code_t

**Framework**: ARKit  
**Kind**: enum

Error codes specific to the camera region provider.

## Declaration

```swift
typedef enum { ... } ar_camera_region_error_code_t;
```

## Topics

### Enumeration Cases
- [ar_camera_region_error_code_add_anchor_failed](ar_camera_region_error_code_t/ar_camera_region_error_code_add_anchor_failed.md)
  Error code indicating that a camera region anchor failed to be added.
- [ar_camera_region_error_code_anchor_max_limit_reached](ar_camera_region_error_code_t/ar_camera_region_error_code_anchor_max_limit_reached.md)
  Error code indicating that the maximum amount of camera region anchors for its respective camera enhancement have been added.
- [ar_camera_region_error_code_remove_anchor_failed](ar_camera_region_error_code_t/ar_camera_region_error_code_remove_anchor_failed.md)
  Error code indicating that a camera region anchor failed to be removed.

## See Also

- [ar_camera_region_add_anchor_completion_handler_function_t](ar_camera_region_add_anchor_completion_handler_function_t.md)
  Function called when a request to add a camera region anchor has completed (successfully or not).
- [ar_camera_region_add_anchor_completion_handler_t](ar_camera_region_add_anchor_completion_handler_t.md)
  Handler called when a request to add a camera region anchor has completed (successfully or not).
- [ar_camera_region_anchor_t](ar_camera_region_anchor_t.md)
- [ar_camera_region_anchor_update_handler_function_t](ar_camera_region_anchor_update_handler_function_t.md)
  Function called when there are updates to a specific camera region anchor.
- [ar_camera_region_anchor_update_handler_t](ar_camera_region_anchor_update_handler_t.md)
  Handler called when there are updates to a specific camera region anchor.
- [ar_camera_region_anchors_enumerator_function_t](ar_camera_region_anchors_enumerator_function_t.md)
  Function for enumerating a collection of camera region anchors.
- [ar_camera_region_anchors_enumerator_t](ar_camera_region_anchors_enumerator_t.md)
  Handler for enumerating a collection of camera region anchors.
- [ar_camera_region_anchors_t](ar_camera_region_anchors_t.md)
- [ar_camera_region_configuration_t](ar_camera_region_configuration_t.md)
- [ar_camera_region_provider_t](ar_camera_region_provider_t.md)
- [ar_camera_region_remove_anchor_completion_handler_function_t](ar_camera_region_remove_anchor_completion_handler_function_t.md)
  Function called when a request to remove a camera region anchor has completed (successfully or not).
- [ar_camera_region_remove_anchor_completion_handler_t](ar_camera_region_remove_anchor_completion_handler_t.md)
  Handler called when a request to remove a camera region anchor has completed (successfully or not).
- [ar_camera_region_remove_anchor_with_identifier_completion_handler_function_t](ar_camera_region_remove_anchor_with_identifier_completion_handler_function_t.md)
  Function called when a request to remove a camera region anchor by its identifier has completed (successfully or not).
- [ar_camera_region_remove_anchor_with_identifier_completion_handler_t](ar_camera_region_remove_anchor_with_identifier_completion_handler_t.md)
  Handler called when a request to remove a camera region anchor by its identifier has completed (successfully or not).
- [ar_camera_region_anchor_create_with_parameters](ar_camera_region_anchor_create_with_parameters.md)
  Create a camera region anchor using a transform from the anchor to the origin coordinate system, a specified size, and a camera enhancement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_camera_region_error_code_t)*