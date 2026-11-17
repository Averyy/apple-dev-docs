# ar_hand_anchor_is_equal_to_hand_anchor

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Returns a bool value that indicates whether the two hand anchors are equal.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern bool ar_hand_anchor_is_equal_to_hand_anchor(ar_hand_anchor_t anchor, ar_hand_anchor_t other_anchor);
```

## Return Value

`YES` if the hand anchors are equal, otherwise `NO`.

## Parameters

- `anchor`: A hand anchor to be compared.
- `other_anchor`: The other hand anchor to be compared to.

## See Also

### Hand anchor functions
- [ar_hand_anchor_get_hand_skeleton](./ar_hand_anchor_get_hand_skeleton.md)
  Get the hand skeleton of a hand anchor.
- [ar_hand_anchor_get_identifier](./ar_hand_anchor_get_identifier.md)
  Get the identifier of an anchor.
- [ar_hand_anchor_get_origin_from_anchor_transform](./ar_hand_anchor_get_origin_from_anchor_transform.md)
  Get the transform from an anchor to the origin coordinate system.
- [ar_hand_anchor_get_timestamp](./ar_hand_anchor_get_timestamp.md)
  Get the timestamp corresponding to an anchor.
- [ar_hand_anchor_is_tracked](./ar_hand_anchor_is_tracked.md)
  Determine whether an anchor is tracked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_hand_anchor_is_equal_to_hand_anchor)*