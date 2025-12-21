# ar_camera_region_provider_set_update_handler_for_anchor_with_identifier_f

**Framework**: ARKit  
**Kind**: func

Set the function for receiving camera region updates for a specific anchor identifier.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
extern void ar_camera_region_provider_set_update_handler_for_anchor_with_identifier_f(ar_camera_region_provider_t camera_region_provider, uuid_t camera_region_anchor_identifier, dispatch_queue_t camera_region_anchor_updates_queue, void * context, ar_camera_region_anchor_update_handler_function_t camera_region_anchor_update_handler_function);
```

#### Discussion

> **Note**: Setting this function will override the handler set using `ar_camera_region_provider_set_update_handler_for_anchor_with_identifier`.

## Parameters

- `camera_region_provider`: The camera region provider.
- `camera_region_anchor_identifier`: The camera region anchor identifier to get updates for.
- `camera_region_anchor_updates_queue`: The queue on which the function will be called. Passing NULL will default to the main queue.
- `context`: The application-defined context parameter to pass to the function.
- `camera_region_anchor_update_handler_function`: The function to be called when new camera region anchor data arrives.

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

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_camera_region_provider_set_update_handler_for_anchor_with_identifier_f)*