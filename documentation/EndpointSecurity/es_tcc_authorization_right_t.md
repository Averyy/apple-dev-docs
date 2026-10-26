# es_tcc_authorization_right_t

**Framework**: Endpoint Security  
**Kind**: struct  
**Role**: Structure

ess_tcc_authorization_right_t

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct es_tcc_authorization_right_t
```

```c
typedef enum { ... } es_tcc_authorization_right_t;
```

#### Overview

Represents the type of authorization permission an application has to a TCC Service.

## Topics

### Initializers
- [init(UInt32)](./es_tcc_authorization_right_t/init%28_%29.md)
- [init(rawValue: UInt32)](./es_tcc_authorization_right_t/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt32](./es_tcc_authorization_right_t/rawvalue.md)
### Enumeration Cases
- [ES_TCC_AUTHORIZATION_RIGHT_ADD_MODIFY_ADDED](./es_tcc_authorization_right_add_modify_added.md)
- [ES_TCC_AUTHORIZATION_RIGHT_ALLOWED](./es_tcc_authorization_right_allowed.md)
- [ES_TCC_AUTHORIZATION_RIGHT_DENIED](./es_tcc_authorization_right_denied.md)
- [ES_TCC_AUTHORIZATION_RIGHT_LEARN_MORE](./es_tcc_authorization_right_learn_more.md)
- [ES_TCC_AUTHORIZATION_RIGHT_LIMITED](./es_tcc_authorization_right_limited.md)
- [ES_TCC_AUTHORIZATION_RIGHT_SESSION_PID](./es_tcc_authorization_right_session_pid.md)
- [ES_TCC_AUTHORIZATION_RIGHT_UNKNOWN](./es_tcc_authorization_right_unknown.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_right_t)*