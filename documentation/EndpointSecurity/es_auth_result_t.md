# es_auth_result_t

**Framework**: Endpoint Security  
**Kind**: struct  
**Role**: Structure

Values used when responding to an authorization event.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct es_auth_result_t
```

```c
typedef enum { ... } es_auth_result_t;
```

## Topics

### Authorization Values
- [var ES_AUTH_RESULT_ALLOW: es_auth_result_t](./es_auth_result_allow.md)
  The caller authorizes the event and allows it to continue.
- [var ES_AUTH_RESULT_DENY: es_auth_result_t](./es_auth_result_deny.md)
  The caller denies authorization to the event and prevents it from continuing.
### Initializers
- [init(UInt32)](./es_auth_result_t/init%28_%29.md)
- [init(rawValue: UInt32)](./es_auth_result_t/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt32](./es_auth_result_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Responding to Events
- [func es_respond_auth_result(OpaquePointer, UnsafePointer<es_message_t>, es_auth_result_t, Bool) -> es_respond_result_t](./es_respond_auth_result%28_,_,_,_%29.md)
  Responds to an event that requires an authorization response.
- [func es_respond_flags_result(OpaquePointer, UnsafePointer<es_message_t>, UInt32, Bool) -> es_respond_result_t](./es_respond_flags_result%28_,_,_,_%29.md)
  Responds to an event that requires authorization flags as a response.
- [struct es_respond_result_t](./es_respond_result_t.md)
  Values that indicate the result of responding to a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_auth_result_t)*