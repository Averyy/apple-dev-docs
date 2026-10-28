# es_unsubscribe_all(_:)

**Framework**: Endpoint Security  
**Kind**: func  
**Role**: Function

Unsubscribes a client from all events.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func es_unsubscribe_all(_ client: OpaquePointer) -> es_return_t
```

```c
extern es_return_t es_unsubscribe_all(es_client_t *client);
```

## Return Value

A value that indicates whether subscribing succeeded. [`ES_RETURN_ERROR`](./es_return_error.md) indicates that the caller couldn’t reach the Endpoint Security subsystem or that the request was invalid.

## Parameters

- `client`: The client to unsubscribe.

## See Also

### Subscribing to Events
- [func es_subscribe(OpaquePointer, UnsafePointer<es_event_type_t>, UInt32) -> es_return_t](./es_subscribe%28_,_,_%29.md)
  Subscribes a client to a set of events.
- [func es_subscriptions(OpaquePointer, UnsafeMutablePointer<Int>, UnsafeMutablePointer<UnsafeMutablePointer<es_event_type_t>>?) -> es_return_t](./es_subscriptions%28_,_,_%29.md)
  Returns a list of the client’s subscriptions.
- [func es_unsubscribe(OpaquePointer, UnsafePointer<es_event_type_t>, UInt32) -> es_return_t](./es_unsubscribe%28_,_,_%29.md)
  Unsubscribes the provided client from a set of events.
- [struct es_event_type_t](./es_event_type_t.md)
  A type used to identify a message’s event type and subscribe to events of that type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_unsubscribe_all(_:))*