# ar_accessory_tracking_provider_set_update_handler

**Framework**: ARKit  
**Kind**: func

Set the handler for receiving accessory anchor updates.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
extern void ar_accessory_tracking_provider_set_update_handler(ar_accessory_tracking_provider_t accessory_tracking_provider, dispatch_queue_t accessory_tracking_updates_queue, ar_accessory_tracking_update_handler_taccessory_tracking_update_handler);
```

#### Discussion

> **Note**: Routine anchor updates will be disabled unless a handler is provided to this method. This is done to save CPU time for applications which do not need an anchor stream.

> **Note**: Setting this handler will override the function set using `ar_accessory_tracking_provider_set_update_handler_f`.

## Parameters

- `accessory_tracking_provider`: The accessory tracking provider.
- `accessory_tracking_updates_queue`: The queue on which the handler will be called. Passing NULL will default to the main queue.
- `accessory_tracking_update_handler`: The handler to be called when new accessory tracking data arrives.

## See Also

- [ar_accessories_enumerator_function_t](ar_accessories_enumerator_function_t.md)
  Function for enumerating a collection of accessories.
- [ar_accessories_enumerator_t](ar_accessories_enumerator_t.md)
  Handler for enumerating a collection of accessories.
- [ar_accessories_t](ar_accessories_t.md)
- [ar_accessory_anchor_t](ar_accessory_anchor_t.md)
- [ar_accessory_anchors_enumerator_function_t](ar_accessory_anchors_enumerator_function_t.md)
  Function for enumerating a collection of accessory anchors.
- [ar_accessory_anchors_enumerator_t](ar_accessory_anchors_enumerator_t.md)
  Handler for enumerating a collection of accessory anchors.
- [ar_accessory_anchors_t](ar_accessory_anchors_t.md)
- [ar_accessory_device_load_completion_handler_function_t](ar_accessory_device_load_completion_handler_function_t.md)
  Function triggered when a request to load an accessory from a `GCDevice` has completed.
- [ar_accessory_device_load_completion_handler_t](ar_accessory_device_load_completion_handler_t.md)
  Handler triggered when a request to load an accessory from a `GCDevice` has completed.
- [ar_accessory_t](ar_accessory_t.md)
- [ar_accessory_tracking_configuration_t](ar_accessory_tracking_configuration_t.md)
- [ar_accessory_tracking_provider_t](ar_accessory_tracking_provider_t.md)
- [ar_accessory_tracking_update_handler_function_t](ar_accessory_tracking_update_handler_function_t.md)
  Function called when there are updates to accessory anchors.
- [ar_accessory_tracking_update_handler_t](ar_accessory_tracking_update_handler_t.md)
  Handler called when there are updates to accessory anchors.
- [ar_accessory_location_name_aim](ar_accessory_location_name_aim.md)
  Pre-defined accessory location name for spatial gamepad and stylus aim point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_accessory_tracking_provider_set_update_handler)*