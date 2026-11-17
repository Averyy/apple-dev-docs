# ar_plane_anchor_get_timestamp

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Get the timestamp corresponding to an anchor.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern CFTimeInterval ar_plane_anchor_get_timestamp(ar_plane_anchor_t anchor);
```

## Return Value

The timestamp associated with the anchor.

## Parameters

- `anchor`: The anchor.

## See Also

### Plane anchor functions
- [ar_plane_detection_provider_copy_all_plane_anchors](./ar_plane_detection_provider_copy_all_plane_anchors.md)
  Copy all plane anchors.
- [ar_plane_extent_is_equal_to_plane_extent](./ar_plane_extent_is_equal_to_plane_extent.md)
  Returns a bool value that indicates whether the two plane extents are equal.
- [ar_plane_geometry_is_equal_to_plane_geometry](./ar_plane_geometry_is_equal_to_plane_geometry.md)
  Returns a bool value that indicates whether the two plane geometries are equal.
- [ar_plane_anchor_get_identifier](./ar_plane_anchor_get_identifier.md)
  Get the identifier of an anchor.
- [ar_plane_anchor_get_origin_from_anchor_transform](./ar_plane_anchor_get_origin_from_anchor_transform.md)
  Get the transform from an anchor to the origin coordinate system.
- [ar_plane_anchor_is_equal_to_plane_anchor](./ar_plane_anchor_is_equal_to_plane_anchor.md)
  Returns a bool value that indicates whether the two plane anchors are equal.
- [ar_plane_anchor_get_origin_from_anchor_transform_with_correction](./ar_plane_anchor_get_origin_from_anchor_transform_with_correction.md)
  Get the transform from an anchor to the origin coordinate system.
- [ar_plane_alignment_t](./ar_plane_alignment_t.md)
  Option set describing possible orientation alignments of a detected plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_plane_anchor_get_timestamp)*