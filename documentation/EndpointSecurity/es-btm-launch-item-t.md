# es_btm_launch_item_t

**Framework**: Endpoint Security  
**Kind**: struct

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_btm_launch_item_t
```

## Topics

### Initializers
- [init()](es_btm_launch_item_t/init.md)
- [init(item_type: es_btm_item_type_t, legacy: Bool, managed: Bool, uid: uid_t, item_url: es_string_token_t, app_url: es_string_token_t)](es_btm_launch_item_t/init(item_type:legacy:managed:uid:item_url:app_url:).md)
### Instance Properties
- [var app_url: es_string_token_t](es_btm_launch_item_t/app_url.md)
- [var item_type: es_btm_item_type_t](es_btm_launch_item_t/item_type.md)
- [var item_url: es_string_token_t](es_btm_launch_item_t/item_url.md)
- [var legacy: Bool](es_btm_launch_item_t/legacy.md)
- [var managed: Bool](es_btm_launch_item_t/managed.md)
- [var uid: uid_t](es_btm_launch_item_t/uid.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct es_authorization_result_t](es_authorization_result_t.md)
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
- [struct es_event_lw_session_login_t](es_event_lw_session_login_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_btm_launch_item_t)*