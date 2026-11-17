# ar_object_axis_aligned_bounding_box_is_equal_to_bounding_box

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Returns a bool value that indicates whether the two bounding boxes are equal.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern bool ar_object_axis_aligned_bounding_box_is_equal_to_bounding_box(ar_object_axis_aligned_bounding_box_t bounding_box, ar_object_axis_aligned_bounding_box_t other_bounding_box);
```

## Return Value

`YES` if the bounding boxes are equal, otherwise `NO`.

## Parameters

- `bounding_box`: A bounding box to be compared.
- `other_bounding_box`: The other bounding box to be compared to.

## See Also

### Object bounding box functions
- [ar_object_axis_aligned_bounding_box_get_center](./ar_object_axis_aligned_bounding_box_get_center.md)
  Get center coordinates for the bounding box.
- [ar_object_axis_aligned_bounding_box_get_extent](./ar_object_axis_aligned_bounding_box_get_extent.md)
  Get extent for the bounding box.
- [ar_object_axis_aligned_bounding_box_get_max](./ar_object_axis_aligned_bounding_box_get_max.md)
  Get maximum X, Y, Z coordinates for the bounding box.
- [ar_object_axis_aligned_bounding_box_get_min](./ar_object_axis_aligned_bounding_box_get_min.md)
  Get minimum X, Y, Z coordinates for the bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_object_axis_aligned_bounding_box_is_equal_to_bounding_box)*