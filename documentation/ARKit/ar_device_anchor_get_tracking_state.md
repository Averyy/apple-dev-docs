# ar_device_anchor_get_tracking_state

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Gets the tracking state of the device anchor.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern ar_device_anchor_tracking_state_t ar_device_anchor_get_tracking_state(ar_device_anchor_t anchor);
```

#### Return Value

The tracking state of this anchor.

## Parameters

- `anchor`: The anchor.

## See Also

### Device anchor functions
- [ar_device_anchor_get_identifier](./ar_device_anchor_get_identifier.md)
- [ar_device_anchor_get_origin_from_anchor_transform](./ar_device_anchor_get_origin_from_anchor_transform.md)
- [ar_device_anchor_get_timestamp](./ar_device_anchor_get_timestamp.md)
- [ar_device_anchor_is_tracked](./ar_device_anchor_is_tracked.md)
- [ar_device_anchor_get_origin_from_anchor_transform_with_correction](./ar_device_anchor_get_origin_from_anchor_transform_with_correction.md)
  Get the transform from an anchor to the origin coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_device_anchor_get_tracking_state)*