# ar_device_anchor_get_timestamp

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Get the timestamp corresponding to an anchor.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern CFTimeInterval ar_device_anchor_get_timestamp(ar_device_anchor_t anchor);
```

## Return Value

The timestamp associated with the anchor.

## Parameters

- `anchor`: The anchor.

## See Also

### Device anchor functions
- [ar_device_anchor_get_identifier](./ar_device_anchor_get_identifier.md)
  Get the identifier of an anchor.
- [ar_device_anchor_get_origin_from_anchor_transform](./ar_device_anchor_get_origin_from_anchor_transform.md)
  Get the transform from an anchor to the origin coordinate system.
- [ar_device_anchor_is_tracked](./ar_device_anchor_is_tracked.md)
  Determine whether an anchor is tracked.
- [ar_device_anchor_get_tracking_state](./ar_device_anchor_get_tracking_state.md)
  Gets the tracking state of the device anchor.
- [ar_device_anchor_get_origin_from_anchor_transform_with_correction](./ar_device_anchor_get_origin_from_anchor_transform_with_correction.md)
  Get the transform from an anchor to the origin coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_device_anchor_get_timestamp)*