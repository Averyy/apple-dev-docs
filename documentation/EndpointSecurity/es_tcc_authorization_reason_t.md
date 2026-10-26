# es_tcc_authorization_reason_t

**Framework**: Endpoint Security  
**Kind**: struct  
**Role**: Structure

ess_tcc_authorization_reason_t

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct es_tcc_authorization_reason_t
```

```c
typedef enum { ... } es_tcc_authorization_reason_t;
```

#### Overview

Represents the reason a TCC permission was updated.

## Topics

### Initializers
- [init(UInt32)](./es_tcc_authorization_reason_t/init%28_%29.md)
- [init(rawValue: UInt32)](./es_tcc_authorization_reason_t/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt32](./es_tcc_authorization_reason_t/rawvalue.md)
### Enumeration Cases
- [ES_TCC_AUTHORIZATION_REASON_APP_TYPE_POLICY](./es_tcc_authorization_reason_app_type_policy.md)
  A system process changed the authorization right
- [ES_TCC_AUTHORIZATION_REASON_ENTITLED](./es_tcc_authorization_reason_entitled.md)
  A system process changed the authorization right
- [ES_TCC_AUTHORIZATION_REASON_ERROR](./es_tcc_authorization_reason_error.md)
- [ES_TCC_AUTHORIZATION_REASON_MDM_POLICY](./es_tcc_authorization_reason_mdm_policy.md)
  A system process changed the authorization right
- [ES_TCC_AUTHORIZATION_REASON_MISSING_USAGE_STRING](./es_tcc_authorization_reason_missing_usage_string.md)
  A system process changed the authorization right
- [ES_TCC_AUTHORIZATION_REASON_NONE](./es_tcc_authorization_reason_none.md)
- [ES_TCC_AUTHORIZATION_REASON_PREFLIGHT_UNKNOWN](./es_tcc_authorization_reason_preflight_unknown.md)
  A system process changed the authorization right
- [ES_TCC_AUTHORIZATION_REASON_PROMPT_CANCEL](./es_tcc_authorization_reason_prompt_cancel.md)
  A system process changed the authorization right
- [ES_TCC_AUTHORIZATION_REASON_PROMPT_TIMEOUT](./es_tcc_authorization_reason_prompt_timeout.md)
  A system process changed the authorization right
- [ES_TCC_AUTHORIZATION_REASON_SERVICE_OVERRIDE_POLICY](./es_tcc_authorization_reason_service_override_policy.md)
  A system process changed the authorization right
- [ES_TCC_AUTHORIZATION_REASON_SERVICE_POLICY](./es_tcc_authorization_reason_service_policy.md)
  A system process changed the authorization right
- [ES_TCC_AUTHORIZATION_REASON_SYSTEM_SET](./es_tcc_authorization_reason_system_set.md)
  User changed the authorization right via Preferences
- [ES_TCC_AUTHORIZATION_REASON_USER_CONSENT](./es_tcc_authorization_reason_user_consent.md)
- [ES_TCC_AUTHORIZATION_REASON_USER_SET](./es_tcc_authorization_reason_user_set.md)
  User answered a prompt

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_reason_t)*