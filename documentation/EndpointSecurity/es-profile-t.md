# es_profile_t

**Framework**: Endpoint Security  
**Kind**: struct

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_profile_t
```

## Topics

### Initializers
- [init()](es_profile_t/init.md)
- [init(identifier: es_string_token_t, uuid: es_string_token_t, install_source: es_profile_source_t, organization: es_string_token_t, display_name: es_string_token_t, scope: es_string_token_t)](es_profile_t/init(identifier:uuid:install_source:organization:display_name:scope:).md)
### Instance Properties
- [var display_name: es_string_token_t](es_profile_t/display_name.md)
- [var identifier: es_string_token_t](es_profile_t/identifier.md)
- [var install_source: es_profile_source_t](es_profile_t/install_source.md)
- [var organization: es_string_token_t](es_profile_t/organization.md)
- [var scope: es_string_token_t](es_profile_t/scope.md)
- [var uuid: es_string_token_t](es_profile_t/uuid.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_profile_t)*