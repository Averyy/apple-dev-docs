# es_auth_result_t

**Framework**: Endpoint Security  
**Kind**: struct

Values used when responding to an authorization event.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_auth_result_t
```

## Topics

### Authorization Values
- [var ES_AUTH_RESULT_ALLOW: es_auth_result_t](es_auth_result_allow.md)
  The caller authorizes the event and allows it to continue.
- [var ES_AUTH_RESULT_DENY: es_auth_result_t](es_auth_result_deny.md)
  The caller denies authorization to the event and prevents it from continuing.
### Initializers
- [init(UInt32)](es_auth_result_t/init(_:).md)
- [init(rawValue: UInt32)](es_auth_result_t/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](es_auth_result_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func es_respond_auth_result(OpaquePointer, UnsafePointer<es_message_t>, es_auth_result_t, Bool) -> es_respond_result_t](es_respond_auth_result(_:_:_:_:).md)
  Responds to an event that requires an authorization response.
- [func es_respond_flags_result(OpaquePointer, UnsafePointer<es_message_t>, UInt32, Bool) -> es_respond_result_t](es_respond_flags_result(_:_:_:_:).md)
  Responds to an event that requires authorization flags as a response.
- [struct es_respond_result_t](es_respond_result_t.md)
  Values that indicate the result of responding to a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_auth_result_t)*