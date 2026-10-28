# ar_polygon_points_get_count

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Gets the number of points in the collection.

**Availability**:
- visionOS 27.0+

## Declaration

```c
extern size_t ar_polygon_points_get_count(ar_polygon_points_t polygon_points);
```

## Return Value

The number of points in the collection.

## Parameters

- `polygon_points`: The polygon points collection. Must not be `NULL`.

## See Also

### Visual fidelity
- [ar_polygon_points_add_point](./ar_polygon_points_add_point.md)
  Adds a single point to the polygon points collection.
- [ar_polygon_points_add_points](./ar_polygon_points_add_points.md)
  Adds multiple points to the polygon points collection.
- [ar_polygon_points_create](./ar_polygon_points_create.md)
  Creates a new empty polygon points collection.
- [ar_polygon_points_get_point_at_index](./ar_polygon_points_get_point_at_index.md)
  Gets a point at a specific index.
- [ar_polygon_points_is_equal_to_polygon_points](./ar_polygon_points_is_equal_to_polygon_points.md)
  Check if two polygon points collections are equal.
- [ar_polygon_points_t](./ar_polygon_points_t.md)
  A collection of 2D polygon points.
- [ar_reference_object_configuration_t](./ar_reference_object_configuration_t.md)
  Defines a configuration for an individual reference object.
- [ar_field_of_view_anchor_get_identifier](./ar_field_of_view_anchor_get_identifier.md)
  Get the identifier of the field of view anchor.
- [ar_field_of_view_anchor_get_left_polygon_points](./ar_field_of_view_anchor_get_left_polygon_points.md)
  Get the left eye polygon boundary points defining the preset FoV.
- [ar_field_of_view_anchor_get_origin_from_anchor_transform](./ar_field_of_view_anchor_get_origin_from_anchor_transform.md)
  Get the transform from the anchor to the origin coordinate system.
- [ar_field_of_view_anchor_get_origin_from_anchor_transform_with_correction](./ar_field_of_view_anchor_get_origin_from_anchor_transform_with_correction.md)
  Get the transform from an anchor to the origin coordinate system with a transform correction option.
- [ar_field_of_view_anchor_get_right_polygon_points](./ar_field_of_view_anchor_get_right_polygon_points.md)
  Get the right eye polygon boundary points defining the preset FoV.
- [ar_field_of_view_anchor_get_timestamp](./ar_field_of_view_anchor_get_timestamp.md)
  Get the timestamp of the field of view anchor.
- [ar_field_of_view_anchor_is_equal_to_field_of_view_anchor](./ar_field_of_view_anchor_is_equal_to_field_of_view_anchor.md)
  Check if two field of view anchors are equal.
- [ar_field_of_view_create_polygon](./ar_field_of_view_create_polygon.md)
  Create a polygon-based field of view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_polygon_points_get_count)*