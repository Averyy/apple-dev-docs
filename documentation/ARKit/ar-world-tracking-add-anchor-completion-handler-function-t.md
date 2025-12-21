# ar_world_tracking_add_anchor_completion_handler_function_t

**Framework**: ARKit  
**Kind**: typealias

**Availability**:
- visionOS 1.0+

## Declaration

```swift
typedef void (*)(void *, NSObject<OS_ar_world_anchor> *, _Bool, NSObject<OS_ar_error> *) ar_world_tracking_add_anchor_completion_handler_function_t;
```

## See Also

- [ar_world_anchor_create_with_origin_from_anchor_transform](ar_world_anchor_create_with_origin_from_anchor_transform.md)
  Creates a world anchor from a position and orientation in world space.
- [ar_world_anchor_is_shared_with_nearby_participants](ar_world_anchor_is_shared_with_nearby_participants.md)
  Check if a world anchor is marked to be shared with nearby participants.
- [ar_world_anchor_shared_with_nearby_participants_create](ar_world_anchor_shared_with_nearby_participants_create.md)
  Initialize a world anchor that should be shared with nearby participants.
- [ar_world_anchor_sharing_availability_update_handler_function_t](ar_world_anchor_sharing_availability_update_handler_function_t.md)
  Function pointer called when there is a change in world anchor sharing availability.
- [ar_world_anchor_sharing_availability_update_handler_t](ar_world_anchor_sharing_availability_update_handler_t.md)
  Handler called when there is a change in world anchor sharing availability.
- [ar_world_tracking_add_anchor_completion_handler_t](ar_world_tracking_add_anchor_completion_handler_t.md)
  A handler to call upon completion of a request to add a world anchor.
- [ar_world_tracking_remove_anchor_completion_handler_t](ar_world_tracking_remove_anchor_completion_handler_t.md)
  A handler to call upon completion of a request to remove a world anchor.
- [ar_world_tracking_remove_all_anchors_completion_handler_function_t](ar_world_tracking_remove_all_anchors_completion_handler_function_t.md)
  Function called when a request to remove all known world anchors has completed (successfully or not).
- [ar_world_tracking_remove_all_anchors_completion_handler_t](ar_world_tracking_remove_all_anchors_completion_handler_t.md)
  Function called when a request to remove all known world anchors has completed (successfully or not).
- [ar_world_tracking_anchor_update_handler_t](ar_world_tracking_anchor_update_handler_t.md)
  A handler for receiving updates to world anchors.
- [ar_world_tracking_configuration_create](ar_world_tracking_configuration_create.md)
  Creates a world tracking configuration.
- [ar_world_anchors_enumerate_anchors](ar_world_anchors_enumerate_anchors.md)
  Enumerates a collection of world anchors.
- [ar_world_anchors_enumerate_anchors_f](ar_world_anchors_enumerate_anchors_f.md)
  Enumerates a collection of world anchors.
- [ar_world_anchors_get_count](ar_world_anchors_get_count.md)
  Gets the number of world anchors in the collection.
- [ar_world_tracking_provider_create](ar_world_tracking_provider_create.md)
  Creates a world tracking provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_world_tracking_add_anchor_completion_handler_function_t)*