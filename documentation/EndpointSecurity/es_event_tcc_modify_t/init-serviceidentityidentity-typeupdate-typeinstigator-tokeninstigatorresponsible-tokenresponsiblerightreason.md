# init(service:identity:identity_type:update_type:instigator_token:instigator:responsible_token:responsible:right:reason:)

**Framework**: Endpoint Security  
**Kind**: init

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
init(service: es_string_token_t, identity: es_string_token_t, identity_type: es_tcc_identity_type_t, update_type: es_tcc_event_type_t, instigator_token: audit_token_t, instigator: UnsafeMutablePointer<es_process_t>?, responsible_token: UnsafeMutablePointer<audit_token_t>?, responsible: UnsafeMutablePointer<es_process_t>?, right: es_tcc_authorization_right_t, reason: es_tcc_authorization_reason_t)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_tcc_modify_t/init(service:identity:identity_type:update_type:instigator_token:instigator:responsible_token:responsible:right:reason:))*