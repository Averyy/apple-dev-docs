# es_event_authorization_judgement_t

**Framework**: Endpoint Security  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct es_event_authorization_judgement_t
```

```c
typedef struct { ... } es_event_authorization_judgement_t;
```

## Topics

### Initializers
- [init()](./es_event_authorization_judgement_t/init%28%29.md)
- [init(instigator: UnsafeMutablePointer<es_process_t>?, petitioner: UnsafeMutablePointer<es_process_t>?, return_code: Int32, result_count: Int, results: UnsafeMutablePointer<es_authorization_result_t>?, instigator_token: audit_token_t, petitioner_token: audit_token_t)](./es_event_authorization_judgement_t/init%28instigator,petitioner,return_code,result_count,results,instigator_token,petitioner_token%29.md)
### Instance Properties
- [var instigator: UnsafeMutablePointer<es_process_t>?](./es_event_authorization_judgement_t/instigator.md)
- [var instigator_token: audit_token_t](./es_event_authorization_judgement_t/instigator_token.md)
- [var petitioner: UnsafeMutablePointer<es_process_t>?](./es_event_authorization_judgement_t/petitioner.md)
- [var petitioner_token: audit_token_t](./es_event_authorization_judgement_t/petitioner_token.md)
- [var result_count: Int](./es_event_authorization_judgement_t/result_count.md)
- [var results: UnsafeMutablePointer<es_authorization_result_t>?](./es_event_authorization_judgement_t/results.md)
- [var return_code: Int32](./es_event_authorization_judgement_t/return_code.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Structures
- [struct es_authorization_result_t](./es_authorization_result_t.md)
- [struct es_btm_launch_item_t](./es_btm_launch_item_t.md)
- [struct es_event_authentication_auto_unlock_t](./es_event_authentication_auto_unlock_t.md)
- [struct es_event_authentication_od_t](./es_event_authentication_od_t.md)
- [struct es_event_authentication_t](./es_event_authentication_t.md)
- [struct es_event_authentication_token_t](./es_event_authentication_token_t.md)
- [struct es_event_authentication_touchid_t](./es_event_authentication_touchid_t.md)
- [struct es_event_authorization_petition_t](./es_event_authorization_petition_t.md)
- [struct es_event_btm_launch_item_add_t](./es_event_btm_launch_item_add_t.md)
- [struct es_event_btm_launch_item_remove_t](./es_event_btm_launch_item_remove_t.md)
- [struct es_event_gatekeeper_user_override_t](./es_event_gatekeeper_user_override_t.md)
- [struct es_event_login_login_t](./es_event_login_login_t.md)
- [struct es_event_login_logout_t](./es_event_login_logout_t.md)
- [struct es_event_lw_session_lock_t](./es_event_lw_session_lock_t.md)
- [struct es_event_lw_session_login_t](./es_event_lw_session_login_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_authorization_judgement_t)*