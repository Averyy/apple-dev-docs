# es_set_deadline_min_milliseconds(_:_:_:_:)

**Framework**: Endpoint Security  
**Kind**: func

Set the minimum deadline in milliseconds for specified auth event types for this client

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func es_set_deadline_min_milliseconds(_ client: OpaquePointer, _ events: UnsafePointer<es_event_type_t>, _ event_count: UInt32, _ milliseconds: UInt32) -> es_return_t
```

#### Return Value

ES_RETURN_SUCCESS on success, ES_RETURN_ERROR on failure, if client is not a descendants client, or if any event in the array is a bootstrap auth event.

#### Discussion

This allows descendants clients to configure a deadline floor so that deadlines are never shorter than the specified value. Descendants clients can already kill or suspend their child processes directly, furthermore no system daemons are the children of ES clients, so strict deadline enforcement is unnecessary.

> **Note**: The default minimum deadline is 0 (no floor).

> **Note**: The minimum is not capped by the system default. Setting a minimum above the system default is permitted and will effectively extend deadlines beyond the system default.

> **Note**: If the new minimum would exceed the current maximum for any of the specified events, the maximum is adjusted up to match.

## Parameters

- `client`: The client to configure. Must be a descendants client created with es_new_descendants_client().
- `events`: Array of event types to configure deadlines for. May not include ES_EVENT_TYPE_AUTH_BOOTSTRAP_CHECK_IN or ES_EVENT_TYPE_AUTH_BOOTSTRAP_LOOK_UP.
- `event_count`: Number of events in the events array
- `milliseconds`: The minimum deadline in milliseconds


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_set_deadline_min_milliseconds(_:_:_:_:))*