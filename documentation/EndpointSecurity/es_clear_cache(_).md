# es_clear_cache(_:)

**Framework**: Endpoint Security  
**Kind**: func  
**Role**: Function

Clears all cached results for all clients.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func es_clear_cache(_ client: OpaquePointer) -> es_clear_cache_result_t
```

```c
extern es_clear_cache_result_t es_clear_cache(es_client_t *client);
```

## Discussion

Endpoint Security shares caches across all clients, so you can provide any valid client as the parameter to this function.

## Parameters

- `client`: The client that performs the request.

## See Also

### Managing Cached Results
- [struct es_clear_cache_result_t](./es_clear_cache_result_t.md)
  Values that indicate the result of clearing a cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_clear_cache(_:))*