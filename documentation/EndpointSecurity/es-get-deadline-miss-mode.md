# es_get_deadline_miss_mode(_:_:)

**Framework**: Endpoint Security  
**Kind**: func

Get the current deadline miss mode for the specified client

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func es_get_deadline_miss_mode(_ client: OpaquePointer, _ mode: UnsafeMutablePointer<es_deadline_miss_mode_t>) -> es_return_t
```

#### Return Value

ES_RETURN_SUCCESS on success, ES_RETURN_ERROR on failure

## Parameters

- `client`: The client to query
- `mode`: Output parameter for the current deadline miss mode


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_get_deadline_miss_mode(_:_:))*