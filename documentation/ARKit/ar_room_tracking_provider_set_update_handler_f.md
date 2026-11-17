# ar_room_tracking_provider_set_update_handler_f

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Set the function for receiving room tracking updates.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern void ar_room_tracking_provider_set_update_handler_f(ar_room_tracking_provider_t room_tracking_provider, dispatch_queue_t room_tracking_updates_queue, void *context, ar_room_tracking_update_handler_function_t room_tracking_update_handler_function);
```

## Discussion

> **Note**: Setting this function will override the handler set using `ar_room_tracking_provider_set_update_handler`.

## Parameters

- `room_tracking_provider`: The room tracking provider.
- `room_tracking_updates_queue`: The room tracking update queue. Passing `NULL` will default to the main queue.
- `context`: The application-defined context parameter to pass to the function.
- `room_tracking_update_handler_function`: The room tracking update handler function.

## See Also

### Room tracking functions
- [ar_room_tracking_configuration_create](./ar_room_tracking_configuration_create.md)
  Create a room tracking configuration.
- [ar_room_tracking_provider_copy_all_room_anchors](./ar_room_tracking_provider_copy_all_room_anchors.md)
  Copy all room anchors.
- [ar_room_tracking_provider_copy_current_room_anchor](./ar_room_tracking_provider_copy_current_room_anchor.md)
  Copy the room anchor that the person is currently inside.
- [ar_room_tracking_provider_create](./ar_room_tracking_provider_create.md)
  Create a room tracking provider.
- [ar_room_tracking_provider_get_required_authorization_type](./ar_room_tracking_provider_get_required_authorization_type.md)
  Get the authorization type required by the room tracking provider.
- [ar_room_tracking_provider_is_supported](./ar_room_tracking_provider_is_supported.md)
  Determine whether this device supports the room tracking provider.
- [ar_room_tracking_provider_set_update_handler](./ar_room_tracking_provider_set_update_handler.md)
  Set the handler for receiving room tracking updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_room_tracking_provider_set_update_handler_f)*