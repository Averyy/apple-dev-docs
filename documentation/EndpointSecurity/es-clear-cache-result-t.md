# es_clear_cache_result_t

**Framework**: Endpoint Security  
**Kind**: struct

Values that indicate the result of clearing a cache.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_clear_cache_result_t
```

## Topics

### Success
- [var ES_CLEAR_CACHE_RESULT_SUCCESS: es_clear_cache_result_t](es_clear_cache_result_success.md)
  Clearing the cache succeeded.
### Errors
- [var ES_CLEAR_CACHE_RESULT_ERR_INTERNAL: es_clear_cache_result_t](es_clear_cache_result_err_internal.md)
  Communication with the Endpoint Security system failed.
- [var ES_CLEAR_CACHE_RESULT_ERR_THROTTLE: es_clear_cache_result_t](es_clear_cache_result_err_throttle.md)
  Clearing the cache failed because the rate of calls was too high.
### Initializers
- [init(UInt32)](es_clear_cache_result_t/init(_:).md)
- [init(rawValue: UInt32)](es_clear_cache_result_t/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](es_clear_cache_result_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func es_clear_cache(OpaquePointer) -> es_clear_cache_result_t](es_clear_cache(_:).md)
  Clears all cached results for all clients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_clear_cache_result_t)*