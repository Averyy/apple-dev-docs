# ar_skeleton_joint_is_equal_to_skeleton_joint

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Returns a bool value that indicates whether the two skeleton joints are equal.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern bool ar_skeleton_joint_is_equal_to_skeleton_joint(ar_skeleton_joint_t skeleton_joint, ar_skeleton_joint_t other_skeleton_joint);
```

## Return Value

`YES` if the skeleton joints are equal, otherwise `NO`.

## Parameters

- `skeleton_joint`: A skeleton joint to be compared.
- `other_skeleton_joint`: The other skeleton joint to be compared to.

## See Also

### Skeleton joint functions
- [ar_skeleton_joint_get_anchor_from_joint_transform](./ar_skeleton_joint_get_anchor_from_joint_transform.md)
  Get the transform from the joint to the anchor’s coordinate system.
- [ar_skeleton_joint_get_index](./ar_skeleton_joint_get_index.md)
  Get a joint’s index.
- [ar_skeleton_joint_get_parent](./ar_skeleton_joint_get_parent.md)
  Get a joint’s parent joint.
- [ar_skeleton_joint_get_parent_from_joint_transform](./ar_skeleton_joint_get_parent_from_joint_transform.md)
  Get the transform from the joint to its parent joint’s coordinate system.
- [ar_skeleton_joint_is_tracked](./ar_skeleton_joint_is_tracked.md)
  Determine whether a joint is tracked.
- [ar_skeleton_joint_get_anchor_from_joint_transform_with_correction](./ar_skeleton_joint_get_anchor_from_joint_transform_with_correction.md)
  Get the transform from the joint to the anchor’s coordinate system.
- [ar_skeleton_joint_get_parent_from_joint_transform_with_correction](./ar_skeleton_joint_get_parent_from_joint_transform_with_correction.md)
  Get the transform from the joint to its parent joint’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_skeleton_joint_is_equal_to_skeleton_joint)*