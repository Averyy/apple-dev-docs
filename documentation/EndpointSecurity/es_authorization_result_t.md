# es_authorization_result_t

**Framework**: Endpoint Security  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct es_authorization_result_t
```

```c
typedef struct { ... } es_authorization_result_t;
```

## Topics

### Initializers
- [init()](./es_authorization_result_t/init%28%29.md)
- [init(right_name: es_string_token_t, rule_class: es_authorization_rule_class_t, granted: Bool)](./es_authorization_result_t/init%28right_name,rule_class,granted%29.md)
### Instance Properties
- [var granted: Bool](./es_authorization_result_t/granted.md)
- [var right_name: es_string_token_t](./es_authorization_result_t/right_name.md)
- [var rule_class: es_authorization_rule_class_t](./es_authorization_result_t/rule_class.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Structures
- [struct es_btm_launch_item_t](./es_btm_launch_item_t.md)
- [struct es_event_authentication_auto_unlock_t](./es_event_authentication_auto_unlock_t.md)
- [struct es_event_authentication_od_t](./es_event_authentication_od_t.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_authorization_result_t)*