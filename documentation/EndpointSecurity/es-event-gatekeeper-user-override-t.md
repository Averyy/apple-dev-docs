# es_event_gatekeeper_user_override_t

**Framework**: Endpoint Security  
**Kind**: struct

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_gatekeeper_user_override_t
```

## Topics

### Initializers
- [init()](es_event_gatekeeper_user_override_t/init.md)
- [init(file_type: es_gatekeeper_user_override_file_type_t, file: es_event_gatekeeper_user_override_t.__Unnamed_union_file, sha256: UnsafeMutablePointer<es_sha256_t>?, signing_info: UnsafeMutablePointer<es_signed_file_info_t>?)](es_event_gatekeeper_user_override_t/init(file_type:file:sha256:signing_info:).md)
### Instance Properties
- [var file: es_event_gatekeeper_user_override_t.__Unnamed_union_file](es_event_gatekeeper_user_override_t/file.md)
- [var file_type: es_gatekeeper_user_override_file_type_t](es_event_gatekeeper_user_override_t/file_type.md)
- [var sha256: UnsafeMutablePointer<es_sha256_t>?](es_event_gatekeeper_user_override_t/sha256.md)
- [var signing_info: UnsafeMutablePointer<es_signed_file_info_t>?](es_event_gatekeeper_user_override_t/signing_info.md)

## See Also

- [struct es_authorization_result_t](es_authorization_result_t.md)
- [struct es_btm_launch_item_t](es_btm_launch_item_t.md)
- [struct es_event_authentication_auto_unlock_t](es_event_authentication_auto_unlock_t.md)
- [struct es_event_authentication_od_t](es_event_authentication_od_t.md)
- [struct es_event_authentication_t](es_event_authentication_t.md)
- [struct es_event_authentication_token_t](es_event_authentication_token_t.md)
- [struct es_event_authentication_touchid_t](es_event_authentication_touchid_t.md)
- [struct es_event_authorization_judgement_t](es_event_authorization_judgement_t.md)
- [struct es_event_authorization_petition_t](es_event_authorization_petition_t.md)
- [struct es_event_btm_launch_item_add_t](es_event_btm_launch_item_add_t.md)
- [struct es_event_btm_launch_item_remove_t](es_event_btm_launch_item_remove_t.md)
- [struct es_event_login_login_t](es_event_login_login_t.md)
- [struct es_event_login_logout_t](es_event_login_logout_t.md)
- [struct es_event_lw_session_lock_t](es_event_lw_session_lock_t.md)
- [struct es_event_lw_session_login_t](es_event_lw_session_login_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_gatekeeper_user_override_t)*