# es_event_authentication_od_t

**Framework**: Endpoint Security  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct es_event_authentication_od_t
```

```c
typedef struct { ... } es_event_authentication_od_t;
```

## Topics

### Initializers
- [init()](./es_event_authentication_od_t/init%28%29.md)
- [init(instigator: UnsafeMutablePointer<es_process_t>?, record_type: es_string_token_t, record_name: es_string_token_t, node_name: es_string_token_t, db_path: es_string_token_t, instigator_token: audit_token_t)](./es_event_authentication_od_t/init%28instigator,record_type,record_name,node_name,db_path,instigator_token%29.md)
### Instance Properties
- [var db_path: es_string_token_t](./es_event_authentication_od_t/db_path.md)
- [var instigator: UnsafeMutablePointer<es_process_t>?](./es_event_authentication_od_t/instigator.md)
- [var instigator_token: audit_token_t](./es_event_authentication_od_t/instigator_token.md)
- [var node_name: es_string_token_t](./es_event_authentication_od_t/node_name.md)
- [var record_name: es_string_token_t](./es_event_authentication_od_t/record_name.md)
- [var record_type: es_string_token_t](./es_event_authentication_od_t/record_type.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Structures
- [struct es_authorization_result_t](./es_authorization_result_t.md)
- [struct es_btm_launch_item_t](./es_btm_launch_item_t.md)
- [struct es_event_authentication_auto_unlock_t](./es_event_authentication_auto_unlock_t.md)
- [struct es_event_authentication_t](./es_event_authentication_t.md)
- [struct es_event_authentication_token_t](./es_event_authentication_token_t.md)
- [struct es_event_authentication_touchid_t](./es_event_authentication_touchid_t.md)
- [struct es_event_authorization_judgement_t](./es_event_authorization_judgement_t.md)
- [struct es_event_authorization_petition_t](./es_event_authorization_petition_t.md)
- [struct es_event_btm_launch_item_add_t](./es_event_btm_launch_item_add_t.md)
- [struct es_event_btm_launch_item_remove_t](./es_event_btm_launch_item_remove_t.md)
- [struct es_event_gatekeeper_user_override_t](./es_event_gatekeeper_user_override_t.md)
- [struct es_event_login_login_t](./es_event_login_login_t.md)
- [struct es_event_login_logout_t](./es_event_login_logout_t.md)
- [struct es_event_lw_session_lock_t](./es_event_lw_session_lock_t.md)
- [struct es_event_lw_session_login_t](./es_event_lw_session_login_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_authentication_od_t)*