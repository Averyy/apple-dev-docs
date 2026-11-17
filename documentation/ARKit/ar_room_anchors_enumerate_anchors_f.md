# ar_room_anchors_enumerate_anchors_f

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Enumerates a collection of room anchors using a function.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern void ar_room_anchors_enumerate_anchors_f(ar_room_anchors_t room_anchors, void *context, ar_room_anchors_enumerator_function_t room_anchors_enumerator_function);
```

## Parameters

- `room_anchors`: The collection of room anchors.
- `context`: The application-defined context parameter to pass to the function.
- `room_anchors_enumerator_function`: The enumerator function.

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
- [ar_room_anchor_get_origin_from_anchor_transform](./ar_room_anchor_get_origin_from_anchor_transform.md)
  Get the transform from a room anchor to the origin coordinate system.
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
- [ar_room_anchors_get_count](./ar_room_anchors_get_count.md)
  Get the count of room anchors in a collection.
- [ar_room_anchor_get_origin_from_anchor_transform_with_correction](./ar_room_anchor_get_origin_from_anchor_transform_with_correction.md)
  Get the transform from a room anchor to the origin coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_room_anchors_enumerate_anchors_f)*