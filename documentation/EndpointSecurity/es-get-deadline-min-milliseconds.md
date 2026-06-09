# es_get_deadline_min_milliseconds(_:_:_:)

**Framework**: Endpoint Security  
**Kind**: func

Get the current minimum deadline in milliseconds for a specific event type

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func es_get_deadline_min_milliseconds(_ client: OpaquePointer, _ event: es_event_type_t, _ milliseconds: UnsafeMutablePointer<UInt32>) -> es_return_t
```

#### Return Value

ES_RETURN_SUCCESS on success, ES_RETURN_ERROR on failure or if client is not a descendants client

## Parameters

- `client`: The client to query. Must be a descendants client created with es_new_descendants_client().
- `event`: The event type to query the deadline for
- `milliseconds`: Output parameter for the current minimum deadline in milliseconds for the specified event


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_get_deadline_min_milliseconds(_:_:_:))*