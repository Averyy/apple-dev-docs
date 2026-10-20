# es_delete_client(_:)

**Framework**: Endpoint Security  
**Kind**: func  
**Role**: Function

Destroys and disconnects a client instance from the Endpoint Security system.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func es_delete_client(_ client: OpaquePointer?) -> es_return_t
```

```c
extern es_return_t es_delete_client(es_client_t *client);
```

#### Return Value

A value indicating whether deletion succeeded. [`ES_RETURN_ERROR`](./es_return_error.md) indicates that shutdown encountered an error, which results in a resource leak.

## Parameters

- `client`: The client to destroy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_delete_client(_:))*