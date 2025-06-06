# es_event_tcc_modify_t

**Framework**: Endpointsecurity  
**Kind**: struct

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_tcc_modify_t
```

#### Overview

Or revoked.

> **Note**: This event type does not support caching.

## Topics

### Initializers
- [init()](es_event_tcc_modify_t/init.md)
- [init(service: es_string_token_t, identity: es_string_token_t, identity_type: es_tcc_identity_type_t, update_type: es_tcc_event_type_t, instigator_token: audit_token_t, instigator: UnsafeMutablePointer<es_process_t>?, responsible_token: UnsafeMutablePointer<audit_token_t>?, responsible: UnsafeMutablePointer<es_process_t>?, right: es_tcc_authorization_right_t, reason: es_tcc_authorization_reason_t)](es_event_tcc_modify_t/init(service:identity:identity_type:update_type:instigator_token:instigator:responsible_token:responsible:right:reason:).md)
### Instance Properties
- [var identity: es_string_token_t](es_event_tcc_modify_t/identity.md)
- [var identity_type: es_tcc_identity_type_t](es_event_tcc_modify_t/identity_type.md)
  es_tcc_identity_type_t
- [var instigator: UnsafeMutablePointer<es_process_t>?](es_event_tcc_modify_t/instigator.md)
- [var instigator_token: audit_token_t](es_event_tcc_modify_t/instigator_token.md)
- [var reason: es_tcc_authorization_reason_t](es_event_tcc_modify_t/reason.md)
  ess_tcc_authorization_reason_t
- [var responsible: UnsafeMutablePointer<es_process_t>?](es_event_tcc_modify_t/responsible.md)
- [var responsible_token: UnsafeMutablePointer<audit_token_t>?](es_event_tcc_modify_t/responsible_token.md)
- [var right: es_tcc_authorization_right_t](es_event_tcc_modify_t/right.md)
  ess_tcc_authorization_right_t
- [var service: es_string_token_t](es_event_tcc_modify_t/service.md)
- [var update_type: es_tcc_event_type_t](es_event_tcc_modify_t/update_type.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_tcc_modify_t)*