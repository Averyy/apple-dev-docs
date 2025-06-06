# es_event_authentication_touchid_t

**Framework**: Endpoint Security  
**Kind**: struct

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_authentication_touchid_t
```

## Topics

### Initializers
- [init()](es_event_authentication_touchid_t/init.md)
- [init(instigator: UnsafeMutablePointer<es_process_t>?, touchid_mode: es_touchid_mode_t, has_uid: Bool, uid: es_event_authentication_touchid_t.__Unnamed_union_uid, instigator_token: audit_token_t)](es_event_authentication_touchid_t/init(instigator:touchid_mode:has_uid:uid:instigator_token:).md)
### Instance Properties
- [var has_uid: Bool](es_event_authentication_touchid_t/has_uid.md)
- [var instigator: UnsafeMutablePointer<es_process_t>?](es_event_authentication_touchid_t/instigator.md)
- [var instigator_token: audit_token_t](es_event_authentication_touchid_t/instigator_token.md)
- [var touchid_mode: es_touchid_mode_t](es_event_authentication_touchid_t/touchid_mode.md)
- [var uid: es_event_authentication_touchid_t.__Unnamed_union_uid](es_event_authentication_touchid_t/uid.md)

## See Also

- [struct es_authorization_result_t](es_authorization_result_t.md)
- [struct es_btm_launch_item_t](es_btm_launch_item_t.md)
- [struct es_event_authentication_auto_unlock_t](es_event_authentication_auto_unlock_t.md)
- [struct es_event_authentication_od_t](es_event_authentication_od_t.md)
- [struct es_event_authentication_t](es_event_authentication_t.md)
- [struct es_event_authentication_token_t](es_event_authentication_token_t.md)
- [struct es_event_authorization_judgement_t](es_event_authorization_judgement_t.md)
- [struct es_event_authorization_petition_t](es_event_authorization_petition_t.md)
- [struct es_event_btm_launch_item_add_t](es_event_btm_launch_item_add_t.md)
- [struct es_event_btm_launch_item_remove_t](es_event_btm_launch_item_remove_t.md)
- [struct es_event_gatekeeper_user_override_t](es_event_gatekeeper_user_override_t.md)
- [struct es_event_login_login_t](es_event_login_login_t.md)
- [struct es_event_login_logout_t](es_event_login_logout_t.md)
- [struct es_event_lw_session_lock_t](es_event_lw_session_lock_t.md)
- [struct es_event_lw_session_login_t](es_event_lw_session_login_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_authentication_touchid_t)*