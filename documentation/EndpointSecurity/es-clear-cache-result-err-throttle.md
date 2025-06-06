# ES_CLEAR_CACHE_RESULT_ERR_THROTTLE

**Framework**: Endpoint Security  
**Kind**: var

Clearing the cache failed because the rate of calls was too high.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var ES_CLEAR_CACHE_RESULT_ERR_THROTTLE: es_clear_cache_result_t { get }
```

#### Discussion

If you receive this response, slow down the rate at which you make calls to [`es_clear_cache(_:)`](es_clear_cache(_:).md).

## See Also

- [var ES_CLEAR_CACHE_RESULT_ERR_INTERNAL: es_clear_cache_result_t](es_clear_cache_result_err_internal.md)
  Communication with the Endpoint Security system failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_clear_cache_result_err_throttle)*