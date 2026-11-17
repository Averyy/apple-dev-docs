# ar_object_anchors_get_count

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Get the count of object anchors in a collection.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern size_t ar_object_anchors_get_count(ar_object_anchors_t object_anchors);
```

## Return Value

The number of object anchors in the collection.

## Parameters

- `object_anchors`: The collection of object anchors.

## See Also

### Object anchor functions
- [ar_object_anchor_get_bounding_box](./ar_object_anchor_get_bounding_box.md)
  Get bounding box for the object. Aligned with frame defining object’s center and axes.
- [ar_object_anchor_get_identifier](./ar_object_anchor_get_identifier.md)
  Get the identifier of an anchor.
- [ar_object_anchor_get_origin_from_anchor_transform](./ar_object_anchor_get_origin_from_anchor_transform.md)
  Get the transform from an anchor to the origin coordinate system.
- [ar_object_anchor_get_reference_object](./ar_object_anchor_get_reference_object.md)
  Get the underlying tracked reference object from an object anchor.
- [ar_object_anchor_get_timestamp](./ar_object_anchor_get_timestamp.md)
  Get the timestamp corresponding to an anchor.
- [ar_object_anchor_is_equal_to_object_anchor](./ar_object_anchor_is_equal_to_object_anchor.md)
  Returns a bool value that indicates whether the two object anchors are equal.
- [ar_object_anchor_is_tracked](./ar_object_anchor_is_tracked.md)
  Determine whether an anchor is tracked.
- [ar_object_anchors_enumerate_anchors](./ar_object_anchors_enumerate_anchors.md)
  Enumerates a collection of object anchors.
- [ar_object_anchors_enumerate_anchors_f](./ar_object_anchors_enumerate_anchors_f.md)
  Enumerates a collection of object anchors using a function.
- [ar_object_anchor_get_origin_from_anchor_transform_with_correction](./ar_object_anchor_get_origin_from_anchor_transform_with_correction.md)
  Get the transform from an anchor to the origin coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_object_anchors_get_count)*