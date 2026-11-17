# ar_mesh_anchor_get_origin_from_anchor_transform

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Get the transform from an anchor to the origin coordinate system.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern simd_float4x4 ar_mesh_anchor_get_origin_from_anchor_transform(ar_mesh_anchor_t anchor);
```

## Return Value

The origin from anchor transform.

## Parameters

- `anchor`: The anchor.

## See Also

### Mesh anchor functions
- [ar_mesh_anchor_get_identifier](./ar_mesh_anchor_get_identifier.md)
  Get the identifier of an anchor.
- [ar_mesh_anchor_get_timestamp](./ar_mesh_anchor_get_timestamp.md)
  Get the timestamp corresponding to an anchor.
- [ar_mesh_anchor_is_equal_to_mesh_anchor](./ar_mesh_anchor_is_equal_to_mesh_anchor.md)
  Returns a bool value that indicates whether the two mesh anchors are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_mesh_anchor_get_origin_from_anchor_transform)*