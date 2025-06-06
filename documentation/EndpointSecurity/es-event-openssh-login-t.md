# es_event_openssh_login_t

**Framework**: Endpoint Security  
**Kind**: struct

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_openssh_login_t
```

## Topics

### Initializers
- [init()](es_event_openssh_login_t/init.md)
- [init(success: Bool, result_type: es_openssh_login_result_type_t, source_address_type: es_address_type_t, source_address: es_string_token_t, username: es_string_token_t, has_uid: Bool, uid: es_event_openssh_login_t.__Unnamed_union_uid)](es_event_openssh_login_t/init(success:result_type:source_address_type:source_address:username:has_uid:uid:).md)
### Instance Properties
- [var has_uid: Bool](es_event_openssh_login_t/has_uid.md)
- [var result_type: es_openssh_login_result_type_t](es_event_openssh_login_t/result_type.md)
- [var source_address: es_string_token_t](es_event_openssh_login_t/source_address.md)
- [var source_address_type: es_address_type_t](es_event_openssh_login_t/source_address_type.md)
- [var success: Bool](es_event_openssh_login_t/success.md)
- [var uid: es_event_openssh_login_t.__Unnamed_union_uid](es_event_openssh_login_t/uid.md)
- [var username: es_string_token_t](es_event_openssh_login_t/username.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_openssh_login_t)*