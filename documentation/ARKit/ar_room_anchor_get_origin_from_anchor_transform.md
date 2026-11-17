# ar_room_anchor_get_origin_from_anchor_transform

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Get the transform from a room anchor to the origin coordinate system.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern simd_float4x4 ar_room_anchor_get_origin_from_anchor_transform(ar_room_anchor_t room_anchor);
```

## Return Value

The origin from room anchor transform.

## Parameters

- `room_anchor`: The room anchor.

## See Also

### Room anchor functions
- [ar_room_anchor_contains_point](./ar_room_anchor_contains_point.md)
  Determine if the room contains the given point.
- [ar_room_anchor_get_geometry](./ar_room_anchor_get_geometry.md)
  Get a mesh representation of the room.
- [ar_room_anchor_get_identifier](./ar_room_anchor_get_identifier.md)
  Get the identifier of a room anchor.
- [ar_room_anchor_get_mesh_anchor_identifiers](./ar_room_anchor_get_mesh_anchor_identifiers.md)
  Get the identifiers of all scene reconstruction mesh anchors in a room anchor.
- [ar_room_anchor_get_mesh_geometries_for_classification](./ar_room_anchor_get_mesh_geometries_for_classification.md)
  Get disjoint mesh geometries of a given classification.
- [ar_room_anchor_get_plane_anchor_identifiers](./ar_room_anchor_get_plane_anchor_identifiers.md)
  Get the identifiers of all plane anchors in a room anchor.
- [ar_room_anchor_get_timestamp](./ar_room_anchor_get_timestamp.md)
  Get the timestamp corresponding to when the room anchor was updated.
- [ar_room_anchor_is_current_room](./ar_room_anchor_is_current_room.md)
  Determine if the room anchor represents the current room the person is in.
- [ar_room_anchor_is_equal_to_room_anchor](./ar_room_anchor_is_equal_to_room_anchor.md)
  Returns a bool value that indicates whether the two room anchors are equal.
- [ar_room_anchor_get_mesh_geometries_for_surface_classification](./ar_room_anchor_get_mesh_geometries_for_surface_classification.md)
  Get disjoint mesh geometries of a given surface classification.
- [ar_room_anchors_enumerate_anchors](./ar_room_anchors_enumerate_anchors.md)
  Enumerate a collection of room anchors.
- [ar_room_anchors_enumerate_anchors_f](./ar_room_anchors_enumerate_anchors_f.md)
  Enumerates a collection of room anchors using a function.
- [ar_room_anchors_get_count](./ar_room_anchors_get_count.md)
  Get the count of room anchors in a collection.
- [ar_room_anchor_get_origin_from_anchor_transform_with_correction](./ar_room_anchor_get_origin_from_anchor_transform_with_correction.md)
  Get the transform from a room anchor to the origin coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_room_anchor_get_origin_from_anchor_transform)*