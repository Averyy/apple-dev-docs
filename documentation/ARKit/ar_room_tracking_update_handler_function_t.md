# ar_room_tracking_update_handler_function_t

**Framework**: ARKit  
**Kind**: typealias  
**Role**: Type Alias

Function called when there are updates to room anchors.

**Availability**:
- visionOS 2.0+

## Declaration

```c
typedef void (*)(void *, NSObject<OS_ar_room_anchors> *, NSObject<OS_ar_room_anchors> *, NSObject<OS_ar_room_anchors> *) ar_room_tracking_update_handler_function_t;
```

## Parameters

- `context`: The application-defined context.
- `added_anchors`: The collection of anchors that were added.
- `updated_anchors`: The collection of anchors that were updated.
- `removed_anchors`: The collection of anchors that were removed.

## See Also

### Room tracking data types
- [ar_room_tracking_configuration_t](./ar_room_tracking_configuration_t.md)
  Configuration for room tracking.
- [ar_room_tracking_provider_t](./ar_room_tracking_provider_t.md)
  A data provider for room tracking.
- [ar_room_tracking_update_handler_t](./ar_room_tracking_update_handler_t.md)
  Handler called when there are updates to room anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_room_tracking_update_handler_function_t)*