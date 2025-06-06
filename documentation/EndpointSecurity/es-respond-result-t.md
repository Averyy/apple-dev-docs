# es_respond_result_t

**Framework**: Endpoint Security  
**Kind**: struct

Values that indicate the result of responding to a message.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_respond_result_t
```

## Topics

### Success
- [var ES_RESPOND_RESULT_SUCCESS: es_respond_result_t](es_respond_result_success.md)
  Endpoint Security successfully delivered the response.
### Errors
- [var ES_RESPOND_RESULT_ERR_DUPLICATE_RESPONSE: es_respond_result_t](es_respond_result_err_duplicate_response.md)
  The caller responded to a message that already received a response.
- [var ES_RESPOND_RESULT_ERR_INTERNAL: es_respond_result_t](es_respond_result_err_internal.md)
  Communication with the Endpoint Security system failed.
- [var ES_RESPOND_RESULT_ERR_INVALID_ARGUMENT: es_respond_result_t](es_respond_result_err_invalid_argument.md)
  The caller provided one or more invalid arguments.
- [var ES_RESPOND_RESULT_NOT_FOUND: es_respond_result_t](es_respond_result_not_found.md)
  The system couldn’t find the message that the caller sent this response to.
- [var ES_RESPOND_RESULT_ERR_EVENT_TYPE: es_respond_result_t](es_respond_result_err_event_type.md)
  The caller performed an inappropriate response to the event.
### Initializers
- [init(UInt32)](es_respond_result_t/init(_:).md)
- [init(rawValue: UInt32)](es_respond_result_t/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](es_respond_result_t/rawvalue.md)

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
- [struct es_auth_result_t](es_auth_result_t.md)
  Values used when responding to an authorization event.
- [func es_respond_flags_result(OpaquePointer, UnsafePointer<es_message_t>, UInt32, Bool) -> es_respond_result_t](es_respond_flags_result(_:_:_:_:).md)
  Responds to an event that requires authorization flags as a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_respond_result_t)*