# ar_shared_coordinate_space_connected_participants_update_handler_t

**Framework**: ARKit  
**Kind**: typealias

Handler called when there is an update to shared coordinate space connected participants.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
typedef void (^)(NSObject<OS_ar_identifiers> *) ar_shared_coordinate_space_connected_participants_update_handler_t;
```

## Parameters

- `connected_participant_identifiers`: List of all participant identifiers that have established a shared coordinate space.

## See Also

- [ar_shared_coordinate_space_configuration_t](ar_shared_coordinate_space_configuration_t.md)
- [ar_shared_coordinate_space_connected_participants_update_handler_function_t](ar_shared_coordinate_space_connected_participants_update_handler_function_t.md)
  Function called when there are updates to shared coordinate space participant status.
- [ar_shared_coordinate_space_provider_t](ar_shared_coordinate_space_provider_t.md)
- [ar_shared_coordinate_space_sharing_status_update_handler_function_t](ar_shared_coordinate_space_sharing_status_update_handler_function_t.md)
  Function called when there is an update to shared coordinate space sharing status.
- [ar_shared_coordinate_space_sharing_status_update_handler_t](ar_shared_coordinate_space_sharing_status_update_handler_t.md)
  Handler called when there is an update to shared coordinate space sharing status.
- [ar_shared_coordinate_provider_set_connected_participants_update_handler_f](ar_shared_coordinate_provider_set_connected_participants_update_handler_f.md)
  Set the function for receiving shared coordinate space connected participants updates.
- [ar_shared_coordinate_space_configuration_create](ar_shared_coordinate_space_configuration_create.md)
  Create a shared coordinate space configuration.
- [ar_shared_coordinate_space_provider_copy_next_coordinate_space_data](ar_shared_coordinate_space_provider_copy_next_coordinate_space_data.md)
  Copy the next collaboration data.
- [ar_shared_coordinate_space_provider_create](ar_shared_coordinate_space_provider_create.md)
  Create a shared coordinate space provider.
- [ar_shared_coordinate_space_provider_get_participant_identifier](ar_shared_coordinate_space_provider_get_participant_identifier.md)
  Get the identifier used to identify the participant in the shared coordinate space.
- [ar_shared_coordinate_space_provider_get_required_authorization_type](ar_shared_coordinate_space_provider_get_required_authorization_type.md)
  Get the authorization type required by the shared coordinate space provider.
- [ar_shared_coordinate_space_provider_is_supported](ar_shared_coordinate_space_provider_is_supported.md)
  Determines whether this device supports the shared coordinate space provider.
- [ar_shared_coordinate_space_provider_push_data](ar_shared_coordinate_space_provider_push_data.md)
  Push data to shared coordinate space.
- [ar_shared_coordinate_space_provider_set_connected_participants_update_handler](ar_shared_coordinate_space_provider_set_connected_participants_update_handler.md)
  Set the handler for receiving shared coordinate space connected participants updates.
- [ar_shared_coordinate_space_provider_set_sharing_status_update_handler](ar_shared_coordinate_space_provider_set_sharing_status_update_handler.md)
  Set the handler for receiving sharing status updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_shared_coordinate_space_connected_participants_update_handler_t)*