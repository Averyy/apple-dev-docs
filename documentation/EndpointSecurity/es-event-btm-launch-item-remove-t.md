# es_event_btm_launch_item_remove_t

**Framework**: Endpoint Security  
**Kind**: struct

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_btm_launch_item_remove_t
```

## Topics

### Initializers
- [init(instigator: UnsafeMutablePointer<es_process_t>?, app: UnsafeMutablePointer<es_process_t>?, item: UnsafeMutablePointer<es_btm_launch_item_t>, instigator_token: UnsafeMutablePointer<audit_token_t>?, app_token: UnsafeMutablePointer<audit_token_t>?)](es_event_btm_launch_item_remove_t/init(instigator:app:item:instigator_token:app_token:).md)
### Instance Properties
- [var app: UnsafeMutablePointer<es_process_t>?](es_event_btm_launch_item_remove_t/app.md)
- [var app_token: UnsafeMutablePointer<audit_token_t>?](es_event_btm_launch_item_remove_t/app_token.md)
- [var instigator: UnsafeMutablePointer<es_process_t>?](es_event_btm_launch_item_remove_t/instigator.md)
- [var instigator_token: UnsafeMutablePointer<audit_token_t>?](es_event_btm_launch_item_remove_t/instigator_token.md)
- [var item: UnsafeMutablePointer<es_btm_launch_item_t>](es_event_btm_launch_item_remove_t/item.md)

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
- [struct es_event_gatekeeper_user_override_t](es_event_gatekeeper_user_override_t.md)
- [struct es_event_login_login_t](es_event_login_login_t.md)
- [struct es_event_login_logout_t](es_event_login_logout_t.md)
- [struct es_event_lw_session_lock_t](es_event_lw_session_lock_t.md)
- [struct es_event_lw_session_login_t](es_event_lw_session_login_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_btm_launch_item_remove_t)*