# ar_barcode_detection_update_handler_t

**Framework**: ARKit  
**Kind**: typealias  
**Role**: Type Alias

Handler called when there are updates to barcode anchors.

**Availability**:
- visionOS 2.0+

## Declaration

```c
typedef void (^)(NSObject<OS_ar_barcode_anchors> *, NSObject<OS_ar_barcode_anchors> *, NSObject<OS_ar_barcode_anchors> *) ar_barcode_detection_update_handler_t;
```

## Parameters

- `added_anchors`: The collection of anchors that were added.
- `updated_anchors`: The collection of anchors that were updated.
- `removed_anchors`: The collection of anchors that were removed.

## See Also

### Barcode data types
- [ar_barcode_anchor_t](./ar_barcode_anchor_t.md)
  An anchor that tracks a barcode’s position and orientation in the physical environment.
- [ar_barcode_anchors_enumerator_function_t](./ar_barcode_anchors_enumerator_function_t.md)
  Function for enumerating a collection of barcode anchors.
- [ar_barcode_anchors_enumerator_t](./ar_barcode_anchors_enumerator_t.md)
  Handler for enumerating a collection of barcode anchors.
- [ar_barcode_anchors_t](./ar_barcode_anchors_t.md)
  A collection of barcode anchors.
- [ar_barcode_detection_callbacks_t](./ar_barcode_detection_callbacks_t.md)
  Callbacks for barcode detection events.
- [ar_barcode_detection_configuration_t](./ar_barcode_detection_configuration_t.md)
  Configuration for barcode detection.
- [ar_barcode_detection_provider_t](./ar_barcode_detection_provider_t.md)
  A data provider for barcode detection.
- [ar_barcode_detection_update_handler_function_t](./ar_barcode_detection_update_handler_function_t.md)
  Function called when there are updates to barcode anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_barcode_detection_update_handler_t)*