# es_subscriptions(_:_:_:)

**Framework**: Endpoint Security  
**Kind**: func

Returns a list of the client’s subscriptions.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func es_subscriptions(_ client: OpaquePointer, _ count: UnsafeMutablePointer<Int>, _ subscriptions: UnsafeMutablePointer<UnsafeMutablePointer<es_event_type_t>>?) -> es_return_t
```

#### Return Value

A value that indicates whether the subscriptions query succeeded. [`ES_RETURN_ERROR`](es_return_error.md) indicates that the caller couldn’t reach the Endpoint Security subsystem or that the request was invalid.

#### Discussion

On return, the caller takes ownership of the memory pointed to by the `subscriptions` parameter, and must free it.

## Parameters

- `client`: The client to query.
- `count`: On return, the number of items in the   array.
- `subscriptions`: An array of subscribed event types.

## See Also

- [func es_subscribe(OpaquePointer, UnsafePointer<es_event_type_t>, UInt32) -> es_return_t](es_subscribe(_:_:_:).md)
  Subscribes a client to a set of events.
- [func es_unsubscribe(OpaquePointer, UnsafePointer<es_event_type_t>, UInt32) -> es_return_t](es_unsubscribe(_:_:_:).md)
  Unsubscribes the provided client from a set of events.
- [struct es_event_type_t](es_event_type_t.md)
  A type used to identify a message’s event type and subscribe to events of that type.
- [func es_unsubscribe_all(OpaquePointer) -> es_return_t](es_unsubscribe_all(_:).md)
  Unsubscribes a client from all events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_subscriptions(_:_:_:))*