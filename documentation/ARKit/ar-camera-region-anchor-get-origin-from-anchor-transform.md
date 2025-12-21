# ar_camera_region_anchor_get_origin_from_anchor_transform

**Framework**: ARKit  
**Kind**: func

Get the transform from an anchor to the origin coordinate system.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
extern simd_float4x4 ar_camera_region_anchor_get_origin_from_anchor_transform(ar_camera_region_anchor_t camera_region_anchor);
```

#### Return Value

The transform of the anchor.

## Parameters

- `camera_region_anchor`: The anchor.

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

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_camera_region_anchor_get_origin_from_anchor_transform)*