# ar_object_axis_aligned_bounding_box_get_max

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Get maximum X, Y, Z coordinates for the bounding box.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern simd_float3 ar_object_axis_aligned_bounding_box_get_max(ar_object_axis_aligned_bounding_box_t bounding_box);
```

## Return Value

Maximum X, Y, and Z.

## Parameters

- `bounding_box`: The bounding box.

## See Also

### Object bounding box functions
- [ar_object_axis_aligned_bounding_box_get_center](./ar_object_axis_aligned_bounding_box_get_center.md)
  Get center coordinates for the bounding box.
- [ar_object_axis_aligned_bounding_box_get_extent](./ar_object_axis_aligned_bounding_box_get_extent.md)
  Get extent for the bounding box.
- [ar_object_axis_aligned_bounding_box_get_min](./ar_object_axis_aligned_bounding_box_get_min.md)
  Get minimum X, Y, Z coordinates for the bounding box.
- [ar_object_axis_aligned_bounding_box_is_equal_to_bounding_box](./ar_object_axis_aligned_bounding_box_is_equal_to_bounding_box.md)
  Returns a bool value that indicates whether the two bounding boxes are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_object_axis_aligned_bounding_box_get_max)*