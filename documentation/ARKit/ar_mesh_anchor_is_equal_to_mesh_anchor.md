# ar_mesh_anchor_is_equal_to_mesh_anchor

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Returns a bool value that indicates whether the two mesh anchors are equal.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern bool ar_mesh_anchor_is_equal_to_mesh_anchor(ar_mesh_anchor_t mesh_anchor, ar_mesh_anchor_t other_mesh_anchor);
```

## Return Value

`YES` if the mesh anchors are equal, otherwise `NO`.

## Parameters

- `mesh_anchor`: A mesh anchor to be compared.
- `other_mesh_anchor`: The other mesh anchor to be compared to.

## See Also

### Mesh anchor functions
- [ar_mesh_anchor_get_identifier](./ar_mesh_anchor_get_identifier.md)
  Get the identifier of an anchor.
- [ar_mesh_anchor_get_origin_from_anchor_transform](./ar_mesh_anchor_get_origin_from_anchor_transform.md)
  Get the transform from an anchor to the origin coordinate system.
- [ar_mesh_anchor_get_timestamp](./ar_mesh_anchor_get_timestamp.md)
  Get the timestamp corresponding to an anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_mesh_anchor_is_equal_to_mesh_anchor)*