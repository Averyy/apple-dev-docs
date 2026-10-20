# es_event_su_t

**Framework**: Endpoint Security  
**Kind**: struct

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_su_t
```

## Topics

### Initializers
- [init()](es_event_su_t/init.md)
- [init(success: Bool, failure_message: es_string_token_t, from_uid: uid_t, from_username: es_string_token_t, has_to_uid: Bool, to_uid: es_event_su_t.__Unnamed_union_to_uid, to_username: es_string_token_t, shell: es_string_token_t, argc: Int, argv: UnsafeMutablePointer<es_string_token_t>?, env_count: Int, env: UnsafeMutablePointer<es_string_token_t>?)](es_event_su_t/init(success:failure_message:from_uid:from_username:has_to_uid:to_uid:to_username:shell:argc:argv:env_count:env:).md)
### Instance Properties
- [var argc: Int](es_event_su_t/argc.md)
- [var argv: UnsafeMutablePointer<es_string_token_t>?](es_event_su_t/argv.md)
- [var env: UnsafeMutablePointer<es_string_token_t>?](es_event_su_t/env.md)
- [var env_count: Int](es_event_su_t/env_count.md)
- [var failure_message: es_string_token_t](es_event_su_t/failure_message.md)
- [var from_uid: uid_t](es_event_su_t/from_uid.md)
- [var from_username: es_string_token_t](es_event_su_t/from_username.md)
- [var has_to_uid: Bool](es_event_su_t/has_to_uid.md)
- [var shell: es_string_token_t](es_event_su_t/shell.md)
- [var success: Bool](es_event_su_t/success.md)
- [var to_uid: es_event_su_t.__Unnamed_union_to_uid](es_event_su_t/to_uid.md)
- [var to_username: es_string_token_t](es_event_su_t/to_username.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_su_t)*