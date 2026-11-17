# ar_room_tracking_update_handler_t

**Framework**: ARKit  
**Kind**: typealias  
**Role**: Type Alias

Handler called when there are updates to room anchors.

**Availability**:
- visionOS 2.0+

## Declaration

```c
typedef void (^)(NSObject<OS_ar_room_anchors> *, NSObject<OS_ar_room_anchors> *, NSObject<OS_ar_room_anchors> *) ar_room_tracking_update_handler_t;
```

## Parameters

- `added_anchors`: The collection of anchors that were added.
- `updated_anchors`: The collection of anchors that were updated.
- `removed_anchors`: The collection of anchors that were removed.

## See Also

### Room tracking data types
- [ar_room_tracking_configuration_t](./ar_room_tracking_configuration_t.md)
  Configuration for room tracking.
- [ar_room_tracking_provider_t](./ar_room_tracking_provider_t.md)
  A data provider for room tracking.
- [ar_room_tracking_update_handler_function_t](./ar_room_tracking_update_handler_function_t.md)
  Function called when there are updates to room anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_room_tracking_update_handler_t)*