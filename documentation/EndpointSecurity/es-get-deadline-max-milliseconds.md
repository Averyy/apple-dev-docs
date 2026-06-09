# es_get_deadline_max_milliseconds(_:_:_:)

**Framework**: Endpoint Security  
**Kind**: func

Get the current maximum deadline in milliseconds for a specific event type

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func es_get_deadline_max_milliseconds(_ client: OpaquePointer, _ event: es_event_type_t, _ milliseconds: UnsafeMutablePointer<UInt32>) -> es_return_t
```

#### Return Value

ES_RETURN_SUCCESS on success, ES_RETURN_ERROR on failure

## Parameters

- `client`: The client to query
- `event`: The event type to query the deadline for
- `milliseconds`: Output parameter for the current maximum deadline in milliseconds for the specified event


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_get_deadline_max_milliseconds(_:_:_:))*