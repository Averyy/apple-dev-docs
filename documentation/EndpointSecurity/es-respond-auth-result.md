# es_respond_auth_result(_:_:_:_:)

**Framework**: Endpoint Security  
**Kind**: func

Responds to an event that requires an authorization response.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func es_respond_auth_result(_ client: OpaquePointer, _ message: UnsafePointer<es_message_t>, _ result: es_auth_result_t, _ cache: Bool) -> es_respond_result_t
```

#### Return Value

A result that indicates whether the response succeeded or failed.

## Parameters

- `client`: The client that produced the event.
- `message`: The message that delivered the event.
- `result`: A result indicating the action the Endpoint Security subsystem should take.
- `cache`: Indicates whether Endpoint Security should cache the result. The caching semantics depend on the specific event type.

## See Also

- [struct es_auth_result_t](es_auth_result_t.md)
  Values used when responding to an authorization event.
- [func es_respond_flags_result(OpaquePointer, UnsafePointer<es_message_t>, UInt32, Bool) -> es_respond_result_t](es_respond_flags_result(_:_:_:_:).md)
  Responds to an event that requires authorization flags as a response.
- [struct es_respond_result_t](es_respond_result_t.md)
  Values that indicate the result of responding to a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_respond_auth_result(_:_:_:_:))*