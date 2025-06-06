# es_respond_flags_result(_:_:_:_:)

**Framework**: Endpoint Security  
**Kind**: func

Responds to an event that requires authorization flags as a response.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func es_respond_flags_result(_ client: OpaquePointer, _ message: UnsafePointer<es_message_t>, _ authorized_flags: UInt32, _ cache: Bool) -> es_respond_result_t
```

#### Return Value

A result that indicates whether the response succeeded or failed.

#### Discussion

Some events require you to respond with [`es_respond_auth_result(_:_:_:_:)`](es_respond_auth_result(_:_:_:_:).md). Responding to such events with this method instead fails with an error.

## Parameters

- `client`: The client that produced the event.
- `message`: The message that delivered the event.
- `authorized_flags`: A   value to apply as a mask on the flags in the event.
- `cache`: Indicates whether Endpoint Security should cache this result. The caching semantics depend on the specific event type.

## See Also

- [func es_respond_auth_result(OpaquePointer, UnsafePointer<es_message_t>, es_auth_result_t, Bool) -> es_respond_result_t](es_respond_auth_result(_:_:_:_:).md)
  Responds to an event that requires an authorization response.
- [struct es_auth_result_t](es_auth_result_t.md)
  Values used when responding to an authorization event.
- [struct es_respond_result_t](es_respond_result_t.md)
  Values that indicate the result of responding to a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_respond_flags_result(_:_:_:_:))*