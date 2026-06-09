# es_set_deadline_max_milliseconds(_:_:_:_:)

**Framework**: Endpoint Security  
**Kind**: func

Set the maximum deadline in milliseconds for specified auth event types for this client

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func es_set_deadline_max_milliseconds(_ client: OpaquePointer, _ events: UnsafePointer<es_event_type_t>, _ event_count: UInt32, _ milliseconds: UInt32) -> es_return_t
```

#### Return Value

ES_RETURN_SUCCESS on success, ES_RETURN_ERROR on failure or if milliseconds exceeds system default

#### Discussion

This allows clients to configure lower per-event-type deadlines so that operations don’t block for too long if the client fails to respond. The kernel will automatically unblock operations based on the client’s deadline miss mode when the deadline expires.

> **Note**: If a deadline minimum has been set (see es_set_deadline_min_milliseconds) and the new maximum would be lower than the current minimum, the minimum is adjusted down to match.

## Parameters

- `client`: The client to configure
- `events`: Array of event types to configure deadlines for
- `event_count`: Number of events in the events array


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_set_deadline_max_milliseconds(_:_:_:_:))*