# es_event_od_delete_user_t

**Framework**: Endpoint Security  
**Kind**: struct

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_od_delete_user_t
```

## Topics

### Initializers
- [init()](es_event_od_delete_user_t/init.md)
- [init(instigator: UnsafeMutablePointer<es_process_t>?, error_code: Int32, user_name: es_string_token_t, node_name: es_string_token_t, db_path: es_string_token_t, instigator_token: audit_token_t)](es_event_od_delete_user_t/init(instigator:error_code:user_name:node_name:db_path:instigator_token:).md)
### Instance Properties
- [var db_path: es_string_token_t](es_event_od_delete_user_t/db_path.md)
- [var error_code: Int32](es_event_od_delete_user_t/error_code.md)
- [var instigator: UnsafeMutablePointer<es_process_t>?](es_event_od_delete_user_t/instigator.md)
- [var instigator_token: audit_token_t](es_event_od_delete_user_t/instigator_token.md)
- [var node_name: es_string_token_t](es_event_od_delete_user_t/node_name.md)
- [var user_name: es_string_token_t](es_event_od_delete_user_t/user_name.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_od_delete_user_t)*