# ar_object_tracking_update_handler_function_t

**Framework**: ARKit  
**Kind**: typealias  
**Role**: Type Alias

Function called when there are updates to object anchors.

**Availability**:
- visionOS 2.0+

## Declaration

```c
typedef void (*)(void *, NSObject<OS_ar_object_anchors> *, NSObject<OS_ar_object_anchors> *, NSObject<OS_ar_object_anchors> *) ar_object_tracking_update_handler_function_t;
```

## Parameters

- `context`: The application-defined context.
- `added_anchors`: The collection of anchors that were added.
- `updated_anchors`: The collection of anchors that were updated.
- `removed_anchors`: The collection of anchors that were removed.

## See Also

### Object tracking data types
- [ar_object_tracking_configuration_t](./ar_object_tracking_configuration_t.md)
  Object tracking configuration.
- [ar_object_tracking_provider_t](./ar_object_tracking_provider_t.md)
  Object tracking provider.
- [ar_object_tracking_update_handler_t](./ar_object_tracking_update_handler_t.md)
  Handler called when there are updates to object anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_object_tracking_update_handler_function_t)*