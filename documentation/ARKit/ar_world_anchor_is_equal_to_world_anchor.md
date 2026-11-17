# ar_world_anchor_is_equal_to_world_anchor

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Returns a bool value that indicates whether the two world anchors are equal.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern bool ar_world_anchor_is_equal_to_world_anchor(ar_world_anchor_t anchor, ar_world_anchor_t other_anchor);
```

## Return Value

`YES` if the world anchors are equal, otherwise `NO`.

## Parameters

- `anchor`: A world anchor to be compared.
- `other_anchor`: The other world anchor to be compared to.

## See Also

### World anchor functions
- [ar_world_anchor_get_identifier](./ar_world_anchor_get_identifier.md)
  Get the identifier of an anchor.
- [ar_world_anchor_get_origin_from_anchor_transform](./ar_world_anchor_get_origin_from_anchor_transform.md)
  Get the transform from an anchor to the origin coordinate system.
- [ar_world_anchor_get_timestamp](./ar_world_anchor_get_timestamp.md)
  Get the timestamp corresponding to an anchor.
- [ar_world_anchor_is_tracked](./ar_world_anchor_is_tracked.md)
  Determine whether an anchor is tracked.
- [ar_world_tracking_provider_copy_all_world_anchors](./ar_world_tracking_provider_copy_all_world_anchors.md)
  Copies all known world anchors from the world tracking provider asynchronously.
- [ar_world_tracking_provider_copy_all_world_anchors_f](./ar_world_tracking_provider_copy_all_world_anchors_f.md)
  Copies all known world anchors from the world tracking provider asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_world_anchor_is_equal_to_world_anchor)*