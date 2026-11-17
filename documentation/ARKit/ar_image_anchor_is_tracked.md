# ar_image_anchor_is_tracked

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Determine whether an anchor is tracked.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern bool ar_image_anchor_is_tracked(ar_image_anchor_t anchor);
```

## Return Value

`true` if the anchor is tracked, `false` otherwise.

## Parameters

- `anchor`: The anchor.

## See Also

### Image anchor functions
- [ar_image_anchor_get_identifier](./ar_image_anchor_get_identifier.md)
  Get the identifier of an anchor.
- [ar_image_anchor_get_origin_from_anchor_transform](./ar_image_anchor_get_origin_from_anchor_transform.md)
  Get the transform from an anchor to the origin coordinate system.
- [ar_image_anchor_get_timestamp](./ar_image_anchor_get_timestamp.md)
  Get the timestamp corresponding to an anchor.
- [ar_image_anchor_is_equal_to_image_anchor](./ar_image_anchor_is_equal_to_image_anchor.md)
  Returns a bool value that indicates whether the two image anchors are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_image_anchor_is_tracked)*