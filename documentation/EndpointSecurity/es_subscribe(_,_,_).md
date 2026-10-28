# es_subscribe(_:_:_:)

**Framework**: Endpoint Security  
**Kind**: func  
**Role**: Function

Subscribes a client to a set of events.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func es_subscribe(_ client: OpaquePointer, _ events: UnsafePointer<es_event_type_t>, _ event_count: UInt32) -> es_return_t
```

```c
extern es_return_t es_subscribe(es_client_t *client, const es_event_type_t *events, uint32_t event_count);
```

## Return Value

A value that indicates whether subscribing succeeded. [`ES_RETURN_ERROR`](./es_return_error.md) indicates that the caller couldn’t reach the Endpoint Security subsystem or that the request was invalid.

## Parameters

- `client`: The client to subscribe.
- `events`: An array of event types to subscribe to.
- `event_count`: The number of event types in the array.

## See Also

### Subscribing to Events
- [func es_subscriptions(OpaquePointer, UnsafeMutablePointer<Int>, UnsafeMutablePointer<UnsafeMutablePointer<es_event_type_t>>?) -> es_return_t](./es_subscriptions%28_,_,_%29.md)
  Returns a list of the client’s subscriptions.
- [func es_unsubscribe(OpaquePointer, UnsafePointer<es_event_type_t>, UInt32) -> es_return_t](./es_unsubscribe%28_,_,_%29.md)
  Unsubscribes the provided client from a set of events.
- [struct es_event_type_t](./es_event_type_t.md)
  A type used to identify a message’s event type and subscribe to events of that type.
- [func es_unsubscribe_all(OpaquePointer) -> es_return_t](./es_unsubscribe_all%28_%29.md)
  Unsubscribes a client from all events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_subscribe(_:_:_:))*