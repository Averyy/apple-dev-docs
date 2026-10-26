# ar_skeleton_joint_get_parent_from_joint_transform_with_correction

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Get the transform from the joint to its parent joint’s coordinate system.

**Availability**:
- visionOS 27.0+

## Declaration

```c
extern simd_float4x4 ar_skeleton_joint_get_parent_from_joint_transform_with_correction(ar_skeleton_joint_t joint, ar_transform_correction_t transform_correction);
```

#### Return Value

The transform from the joint to its parent joint’s coordinate system. This function will return an identity matrix when called for the root joint.

#### Discussion

> **Note**: For a hand skeleton, the root of all these transforms starts at the wrist, then the next joint out (metacarpals and forearm) are relative to the wrist, then all knuckles are relative to the metacarpals and so on until the finger tips.

## Parameters

- `joint`: The joint.
- `transform_correction`: The transform correction that should be applied.

## See Also

### Skeleton joint functions
- [ar_skeleton_joint_get_anchor_from_joint_transform](./ar_skeleton_joint_get_anchor_from_joint_transform.md)
- [ar_skeleton_joint_get_index](./ar_skeleton_joint_get_index.md)
- [ar_skeleton_joint_get_parent](./ar_skeleton_joint_get_parent.md)
- [ar_skeleton_joint_get_parent_from_joint_transform](./ar_skeleton_joint_get_parent_from_joint_transform.md)
- [ar_skeleton_joint_is_equal_to_skeleton_joint](./ar_skeleton_joint_is_equal_to_skeleton_joint.md)
- [ar_skeleton_joint_is_tracked](./ar_skeleton_joint_is_tracked.md)
- [ar_skeleton_joint_get_anchor_from_joint_transform_with_correction](./ar_skeleton_joint_get_anchor_from_joint_transform_with_correction.md)
  Get the transform from the joint to the anchor’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_skeleton_joint_get_parent_from_joint_transform_with_correction)*