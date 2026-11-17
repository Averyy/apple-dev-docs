# ar_barcode_anchors_enumerator_function_t

**Framework**: ARKit  
**Kind**: typealias  
**Role**: Type Alias

Function for enumerating a collection of barcode anchors.

**Availability**:
- visionOS 2.0+

## Declaration

```c
typedef _Bool (*)(void *, NSObject<OS_ar_barcode_anchor> *) ar_barcode_anchors_enumerator_function_t;
```

## Return Value

`true` to continue enumerating, or `false` to stop enumerating.

## Parameters

- `context`: The application-defined context.
- `barcode_anchor`: The barcode anchor.

## See Also

### Barcode data types
- [ar_barcode_anchor_t](./ar_barcode_anchor_t.md)
  An anchor that tracks a barcode’s position and orientation in the physical environment.
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
- [ar_barcode_detection_update_handler_t](./ar_barcode_detection_update_handler_t.md)
  Handler called when there are updates to barcode anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_barcode_anchors_enumerator_function_t)*