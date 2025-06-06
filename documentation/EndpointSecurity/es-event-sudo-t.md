# es_event_sudo_t

**Framework**: Endpoint Security  
**Kind**: struct

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_sudo_t
```

## Topics

### Initializers
- [init()](es_event_sudo_t/init.md)
- [init(success: Bool, reject_info: UnsafeMutablePointer<es_sudo_reject_info_t>?, has_from_uid: Bool, from_uid: es_event_sudo_t.__Unnamed_union_from_uid, from_username: es_string_token_t, has_to_uid: Bool, to_uid: es_event_sudo_t.__Unnamed_union_to_uid, to_username: es_string_token_t, command: es_string_token_t)](es_event_sudo_t/init(success:reject_info:has_from_uid:from_uid:from_username:has_to_uid:to_uid:to_username:command:).md)
### Instance Properties
- [var command: es_string_token_t](es_event_sudo_t/command.md)
- [var from_uid: es_event_sudo_t.__Unnamed_union_from_uid](es_event_sudo_t/from_uid.md)
- [var from_username: es_string_token_t](es_event_sudo_t/from_username.md)
- [var has_from_uid: Bool](es_event_sudo_t/has_from_uid.md)
- [var has_to_uid: Bool](es_event_sudo_t/has_to_uid.md)
- [var reject_info: UnsafeMutablePointer<es_sudo_reject_info_t>?](es_event_sudo_t/reject_info.md)
- [var success: Bool](es_event_sudo_t/success.md)
- [var to_uid: es_event_sudo_t.__Unnamed_union_to_uid](es_event_sudo_t/to_uid.md)
- [var to_username: es_string_token_t](es_event_sudo_t/to_username.md)

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
- [struct es_event_gatekeeper_user_override_t](es_event_gatekeeper_user_override_t.md)
- [struct es_event_login_login_t](es_event_login_login_t.md)
- [struct es_event_login_logout_t](es_event_login_logout_t.md)
- [struct es_event_lw_session_lock_t](es_event_lw_session_lock_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_sudo_t)*