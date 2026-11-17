# ar_barcode_detection_provider_set_update_handler

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Set the handler for receiving barcode detection updates.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern void ar_barcode_detection_provider_set_update_handler(ar_barcode_detection_provider_t barcode_detection_provider, dispatch_queue_t barcode_detection_updates_queue, ar_barcode_detection_update_handler_t barcode_detection_update_handler);
```

## Discussion

> **Note**: Setting this handler will override the function set using `ar_barcode_detection_provider_set_update_handler_f`.

## Parameters

- `barcode_detection_provider`: The barcode detection provider.
- `barcode_detection_updates_queue`: The queue on which the handler will be called. Passing NULL will default to the main queue.
- `barcode_detection_update_handler`: Handler to be called when new anchor data arrives. Refer to `ar_barcode_detection_update_handler_t` for handler signature.

## See Also

### Barcode functions
- [ar_barcode_anchor_copy_payload_data](./ar_barcode_anchor_copy_payload_data.md)
  Get a copy of a barcode anchor’s payload data.
- [ar_barcode_anchor_get_extent](./ar_barcode_anchor_get_extent.md)
  Get the extent of a detected barcode’s bounding box.
- [ar_barcode_anchor_get_identifier](./ar_barcode_anchor_get_identifier.md)
  Get the identifier of an anchor.
- [ar_barcode_anchor_get_origin_from_anchor_transform](./ar_barcode_anchor_get_origin_from_anchor_transform.md)
  Get the transform from an anchor to the origin coordinate system.
- [ar_barcode_anchor_get_payload_string_value](./ar_barcode_anchor_get_payload_string_value.md)
  Get the payload string value of a barcode anchor.
- [ar_barcode_anchor_get_symbology](./ar_barcode_anchor_get_symbology.md)
  Get the symbology of a barcode anchor.
- [ar_barcode_anchor_get_timestamp](./ar_barcode_anchor_get_timestamp.md)
  Get the timestamp corresponding to an anchor.
- [ar_barcode_anchors_enumerate_anchors](./ar_barcode_anchors_enumerate_anchors.md)
  Enumerate a collection of barcode anchors.
- [ar_barcode_anchors_enumerate_anchors_f](./ar_barcode_anchors_enumerate_anchors_f.md)
  Enumerates a collection of barcode anchors using a function.
- [ar_barcode_anchors_get_count](./ar_barcode_anchors_get_count.md)
  Get the count of barcode anchors in a collection.
- [ar_barcode_detection_configuration_create](./ar_barcode_detection_configuration_create.md)
  Create a barcode detection configuration.
- [ar_barcode_detection_configuration_set_detection_symbology](./ar_barcode_detection_configuration_set_detection_symbology.md)
  Set the desired symbologies to detect.
- [ar_barcode_detection_provider_create](./ar_barcode_detection_provider_create.md)
  Create a barcode detection provider.
- [ar_barcode_detection_provider_get_required_authorization_type](./ar_barcode_detection_provider_get_required_authorization_type.md)
  Get the authorization type required by the barcode detection provider.
- [ar_barcode_detection_provider_is_supported](./ar_barcode_detection_provider_is_supported.md)
  Determines whether this device supports the barcode detection provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_barcode_detection_provider_set_update_handler)*