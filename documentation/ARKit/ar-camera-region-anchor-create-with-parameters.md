# ar_camera_region_anchor_create_with_parameters

**Framework**: ARKit  
**Kind**: func

Create a camera region anchor using a transform from the anchor to the origin coordinate system, a specified size, and a camera enhancement.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
extern ar_camera_region_anchor_t ar_camera_region_anchor_create_with_parameters(simd_float4x4 origin_from_anchor_transform, float width, float height, ar_camera_region_camera_enhancement_t camera_enhancement);
```

#### Return Value

An instance of `ar_camera_region_anchor_t`.

#### Discussion

> **Note**: This type supports ARC. In non-ARC files, use `ar_retain()` and `ar_release()` to retain and release the object.

## Parameters

- `origin_from_anchor_transform`: The origin from anchor transform.
- `width`: The width of the anchor (along the X-axis), in meters.
- `height`: The height of the anchor (along the Y-axis), in meters.
- `camera_enhancement`: The desired camera enhancement.

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
- [ar_camera_region_anchor_get_camera_enhancement](ar_camera_region_anchor_get_camera_enhancement.md)
  Get the camera enhancement type for a given anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_camera_region_anchor_create_with_parameters)*