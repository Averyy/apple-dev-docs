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
- [ar_world_tracking_add_anchor_completion_handler_t](ar_world_tracking_add_anchor_completion_handler_t.md)
  A handler to call upon completion of a request to add a world anchor.
- [ar_world_tracking_remove_anchor_completion_handler_t](ar_world_tracking_remove_anchor_completion_handler_t.md)
  A handler to call upon completion of a request to remove a world anchor.
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
- [ar_world_tracking_provider_is_supported](ar_world_tracking_provider_is_supported.md)
  Returns a Boolean value that indicates whether the current runtime environment supports world tracking providers.
- [ar_world_tracking_provider_query_device_anchor_at_timestamp](ar_world_tracking_provider_query_device_anchor_at_timestamp.md)
  Queries the predicted pose of the current device at a given time.
- [ar_world_tracking_provider_add_anchor](ar_world_tracking_provider_add_anchor.md)
  Adds a world anchor you supply to the set of currently tracked anchors.
- [ar_world_tracking_provider_add_anchor_f](ar_world_tracking_provider_add_anchor_f.md)
  Adds a world anchor you supply to the set of currently tracked anchors.
- [ar_world_tracking_provider_get_required_authorization_type](ar_world_tracking_provider_get_required_authorization_type.md)
  Gets the types of authorizations required to track world anchors.
- [ar_world_tracking_provider_set_anchor_update_handler](ar_world_tracking_provider_set_anchor_update_handler.md)
  Sets the handler for receiving world tracking updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_world_tracking_add_anchor_completion_handler_function_t)*