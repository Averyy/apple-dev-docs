# ar_visual_fidelity_provider_set_anchor_update_handler_f

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Set the function for receiving field of view anchor updates.

**Availability**:
- visionOS 27.0+

## Declaration

```c
extern void ar_visual_fidelity_provider_set_anchor_update_handler_f(ar_visual_fidelity_provider_t visual_fidelity_data_provider, dispatch_queue_t anchor_updates_queue, void *context, ar_field_of_view_anchor_update_handler_function_t anchor_update_handler_function);
```

## Discussion

> **Note**: Setting this function will override the handler set using `ar_visual_fidelity_provider_set_anchor_update_handler`.

## Parameters

- `visual_fidelity_data_provider`: The visual fidelity data provider.
- `anchor_updates_queue`: The queue on which the function will be called. Passing `NULL` will default to the main queue.
- `context`: The application-defined context parameter to pass to the function.
- `anchor_update_handler_function`: The function to be called when new anchor data arrives.

## See Also

### Visual fidelity
- [ar_polygon_points_add_point](./ar_polygon_points_add_point.md)
  Adds a single point to the polygon points collection.
- [ar_polygon_points_add_points](./ar_polygon_points_add_points.md)
  Adds multiple points to the polygon points collection.
- [ar_polygon_points_create](./ar_polygon_points_create.md)
  Creates a new empty polygon points collection.
- [ar_polygon_points_get_count](./ar_polygon_points_get_count.md)
  Gets the number of points in the collection.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_visual_fidelity_provider_set_anchor_update_handler_f)*