# ar_world_anchor_get_origin_from_anchor_transform

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Get the transform from an anchor to the origin coordinate system.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern simd_float4x4 ar_world_anchor_get_origin_from_anchor_transform(ar_world_anchor_t anchor);
```

## Return Value

The origin from anchor transform.

## Parameters

- `anchor`: The anchor.

## See Also

### World anchor functions
- [ar_world_anchor_get_identifier](./ar_world_anchor_get_identifier.md)
  Get the identifier of an anchor.
- [ar_world_anchor_get_timestamp](./ar_world_anchor_get_timestamp.md)
  Get the timestamp corresponding to an anchor.
- [ar_world_anchor_is_equal_to_world_anchor](./ar_world_anchor_is_equal_to_world_anchor.md)
  Returns a bool value that indicates whether the two world anchors are equal.
- [ar_world_anchor_is_tracked](./ar_world_anchor_is_tracked.md)
  Determine whether an anchor is tracked.
- [ar_world_tracking_provider_copy_all_world_anchors](./ar_world_tracking_provider_copy_all_world_anchors.md)
  Copies all known world anchors from the world tracking provider asynchronously.
- [ar_world_tracking_provider_copy_all_world_anchors_f](./ar_world_tracking_provider_copy_all_world_anchors_f.md)
  Copies all known world anchors from the world tracking provider asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_world_anchor_get_origin_from_anchor_transform)*