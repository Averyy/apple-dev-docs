# ar_accessories_remove_accessories

**Framework**: ARKit  
**Kind**: func

Remove accessories from a collection.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
extern void ar_accessories_remove_accessories(ar_accessories_t accessories, ar_accessories_t accessories_to_remove);
```

## Parameters

- `accessories`: The collection of accessories to alter.
- `accessories_to_remove`: The accessories to remove.

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

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_accessories_remove_accessories)*