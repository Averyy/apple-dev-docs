# es_clear_cache_result_t

**Framework**: Endpoint Security  
**Kind**: struct  
**Role**: Structure

Values that indicate the result of clearing a cache.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct es_clear_cache_result_t
```

```c
typedef enum { ... } es_clear_cache_result_t;
```

## Topics

### Success
- [var ES_CLEAR_CACHE_RESULT_SUCCESS: es_clear_cache_result_t](./es_clear_cache_result_success.md)
  Clearing the cache succeeded.
### Errors
- [var ES_CLEAR_CACHE_RESULT_ERR_INTERNAL: es_clear_cache_result_t](./es_clear_cache_result_err_internal.md)
  Communication with the Endpoint Security system failed.
- [var ES_CLEAR_CACHE_RESULT_ERR_THROTTLE: es_clear_cache_result_t](./es_clear_cache_result_err_throttle.md)
  Clearing the cache failed because the rate of calls was too high.
### Initializers
- [init(UInt32)](./es_clear_cache_result_t/init%28_%29.md)
- [init(rawValue: UInt32)](./es_clear_cache_result_t/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt32](./es_clear_cache_result_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Managing Cached Results
- [func es_clear_cache(OpaquePointer) -> es_clear_cache_result_t](./es_clear_cache%28_%29.md)
  Clears all cached results for all clients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_clear_cache_result_t)*