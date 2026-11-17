# ar_mesh_anchor_get_identifier

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Get the identifier of an anchor.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern void ar_mesh_anchor_get_identifier(ar_mesh_anchor_t anchor, uuid_t out_identifier);
```

## Parameters

- `anchor`: The anchor.
- `out_identifier`: A pointer to a UUID to fill out with the anchor identifier. Must be non-null.

## See Also

### Mesh anchor functions
- [ar_mesh_anchor_get_origin_from_anchor_transform](./ar_mesh_anchor_get_origin_from_anchor_transform.md)
  Get the transform from an anchor to the origin coordinate system.
- [ar_mesh_anchor_get_timestamp](./ar_mesh_anchor_get_timestamp.md)
  Get the timestamp corresponding to an anchor.
- [ar_mesh_anchor_is_equal_to_mesh_anchor](./ar_mesh_anchor_is_equal_to_mesh_anchor.md)
  Returns a bool value that indicates whether the two mesh anchors are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_mesh_anchor_get_identifier)*