# ar_world_tracking_provider_query_device_anchor_at_timestamp

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Queries the predicted pose of the current device at a given time.

**Availability**:
- visionOS 1.0+

## Declaration

```c
extern ar_device_anchor_query_status_t ar_world_tracking_provider_query_device_anchor_at_timestamp(ar_world_tracking_provider_t world_tracking_provider, CFTimeInterval timestamp, ar_device_anchor_t device_anchor);
```

## Return Value

An `ar_device_anchor_query_status_t` value indicating whether the device anchor was successfully retrieved at the given timestamp or not.

## Discussion

The origin is a right-handed coordinate system and is defined such that X points to the right, Y points up, and Z points backward.

Example usage:

```
auto timing_info = cp_drawable_get_frame_timing(drawable);
auto time = cp_time_to_cf_time_interval(cp_frame_timing_get_presentation_time(timing_info));
const ar_device_anchor_query_status_t status = ar_world_tracking_provider_query_device_anchor_at_timestamp(_provider, time, &device_anchor);
```

> **Note**: This API is not thread safe.

## Parameters

- `world_tracking_provider`: The world tracking provider.
- `timestamp`: The timestamp to get the device anchor at. The timestamp should be provided as mach absolute time in seconds.
- `device_anchor`: The output device anchor.

## See Also

### World tracking
- [ar_world_anchor_create_with_origin_from_anchor_transform](./ar_world_anchor_create_with_origin_from_anchor_transform.md)
  Creates a world anchor from a position and orientation in world space.
- [ar_world_anchor_is_shared_with_nearby_participants](./ar_world_anchor_is_shared_with_nearby_participants.md)
  Check if a world anchor is marked to be shared with nearby participants.
- [ar_world_anchor_shared_with_nearby_participants_create](./ar_world_anchor_shared_with_nearby_participants_create.md)
  Initialize a world anchor that should be shared with nearby participants.
- [ar_world_anchor_sharing_availability_update_handler_function_t](./ar_world_anchor_sharing_availability_update_handler_function_t.md)
  Function pointer called when there is a change in world anchor sharing availability.
- [ar_world_anchor_sharing_availability_update_handler_t](./ar_world_anchor_sharing_availability_update_handler_t.md)
  A handler that the provider calls when there is a change in world anchor sharing availability.
- [ar_world_tracking_add_anchor_completion_handler_t](./ar_world_tracking_add_anchor_completion_handler_t.md)
  A handler to call upon completion of a request to add a world anchor.
- [ar_world_tracking_remove_anchor_completion_handler_t](./ar_world_tracking_remove_anchor_completion_handler_t.md)
  A handler to call upon completion of a request to remove a world anchor.
- [ar_world_tracking_remove_all_anchors_completion_handler_function_t](./ar_world_tracking_remove_all_anchors_completion_handler_function_t.md)
  Function called when a request to remove all known world anchors has completed (successfully or not).
- [ar_world_tracking_remove_all_anchors_completion_handler_t](./ar_world_tracking_remove_all_anchors_completion_handler_t.md)
  Function called when a request to remove all known world anchors has completed (successfully or not).
- [ar_world_tracking_anchor_update_handler_t](./ar_world_tracking_anchor_update_handler_t.md)
  A handler for receiving updates to world anchors.
- [ar_world_tracking_configuration_create](./ar_world_tracking_configuration_create.md)
  Creates a world tracking configuration.
- [ar_world_anchors_enumerate_anchors](./ar_world_anchors_enumerate_anchors.md)
  Enumerates a collection of world anchors.
- [ar_world_anchors_enumerate_anchors_f](./ar_world_anchors_enumerate_anchors_f.md)
  Enumerates a collection of world anchors using a function.
- [ar_world_anchors_get_count](./ar_world_anchors_get_count.md)
  Gets the number of world anchors in the collection.
- [ar_world_tracking_provider_create](./ar_world_tracking_provider_create.md)
  Creates a world tracking provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_world_tracking_provider_query_device_anchor_at_timestamp)*