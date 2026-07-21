# es_set_deadline_miss_mode(_:_:)

**Framework**: Endpoint Security  
**Kind**: func

Set the deadline miss mode for the specified client

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func es_set_deadline_miss_mode(_ client: OpaquePointer, _ mode: es_deadline_miss_mode_t) -> es_return_t
```

#### Return Value

ES_RETURN_SUCCESS on success, ES_RETURN_ERROR on failure

#### Discussion

This determines how the system responds when the client fails to respond to an auth event within the deadline. The default mode is ES_DEADLINE_MISS_MODE_KILL.

> **Note**: This allows clients to defer deadline management to the kernel instead of implementing their own timeout mechanisms.

> **Note**: When `ES_DEADLINE_MISS_MODE_FAIL_CLOSED` is used, if an `AUTH` message is dropped because the message queue was full, it will be `DENY`ed instead of the usual `ALLOW` behaviour.

## Parameters

- `client`: The client to configure
- `mode`: The deadline miss mode to set


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_set_deadline_miss_mode(_:_:))*