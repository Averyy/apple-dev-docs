# ar_world_tracking_provider_copy_all_world_anchors_completion_handler_t

**Framework**: ARKit  
**Kind**: typealias  
**Role**: Type Alias

A handler that the provider calls when a request to copy all known world anchors has completed (successfully or not).

**Availability**:
- visionOS 2.0+

## Declaration

```c
typedef void (^)(NSObject<OS_ar_world_anchors> *) ar_world_tracking_provider_copy_all_world_anchors_completion_handler_t;
```

## Discussion

> **Note**: The results will be accurate at the time of callback, but not necessarily at the time of the request.

> **Note**: The returned anchors support ARC. In non-ARC files, use `ar_retain()` and `ar_release()` to retain and release the anchors.

## Parameters

- `all_anchors`: The nullable collection of known world anchors. Passes `null` if data provider is not running and for other errors.

## See Also

### World tracking data types
- [ar_world_tracking_provider_copy_all_world_anchors_completion_function_t](./ar_world_tracking_provider_copy_all_world_anchors_completion_function_t.md)
  Function called when a request to copy all known world anchors has completed (successfully or not).


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_world_tracking_provider_copy_all_world_anchors_completion_handler_t)*