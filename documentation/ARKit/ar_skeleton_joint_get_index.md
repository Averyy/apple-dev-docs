# ar_skeleton_joint_get_index

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Get a joint’s index.

**Availability**:
- visionOS 1.0+

## Declaration

```c
extern uint64_t ar_skeleton_joint_get_index(ar_skeleton_joint_t joint);
```

## Return Value

The index of the joint.

## Parameters

- `joint`: The joint.

## See Also

### Skeleton joint functions
- [ar_skeleton_joint_get_anchor_from_joint_transform](./ar_skeleton_joint_get_anchor_from_joint_transform.md)
  Get the transform from the joint to the anchor’s coordinate system.
- [ar_skeleton_joint_get_parent](./ar_skeleton_joint_get_parent.md)
  Get a joint’s parent joint.
- [ar_skeleton_joint_get_parent_from_joint_transform](./ar_skeleton_joint_get_parent_from_joint_transform.md)
  Get the transform from the joint to its parent joint’s coordinate system.
- [ar_skeleton_joint_is_equal_to_skeleton_joint](./ar_skeleton_joint_is_equal_to_skeleton_joint.md)
  Returns a bool value that indicates whether the two skeleton joints are equal.
- [ar_skeleton_joint_is_tracked](./ar_skeleton_joint_is_tracked.md)
  Determine whether a joint is tracked.
- [ar_skeleton_joint_get_anchor_from_joint_transform_with_correction](./ar_skeleton_joint_get_anchor_from_joint_transform_with_correction.md)
  Get the transform from the joint to the anchor’s coordinate system.
- [ar_skeleton_joint_get_parent_from_joint_transform_with_correction](./ar_skeleton_joint_get_parent_from_joint_transform_with_correction.md)
  Get the transform from the joint to its parent joint’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_skeleton_joint_get_index)*