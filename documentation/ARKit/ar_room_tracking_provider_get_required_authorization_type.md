# ar_room_tracking_provider_get_required_authorization_type

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Get the authorization type required by the room tracking provider.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern ar_authorization_type_t ar_room_tracking_provider_get_required_authorization_type();
```

## Return Value

The required authorization type.

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
- [ar_room_tracking_provider_is_supported](./ar_room_tracking_provider_is_supported.md)
  Determine whether this device supports the room tracking provider.
- [ar_room_tracking_provider_set_update_handler](./ar_room_tracking_provider_set_update_handler.md)
  Set the handler for receiving room tracking updates.
- [ar_room_tracking_provider_set_update_handler_f](./ar_room_tracking_provider_set_update_handler_f.md)
  Set the function for receiving room tracking updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_room_tracking_provider_get_required_authorization_type)*