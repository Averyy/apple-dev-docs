# ar_hand_skeleton_is_equal_to_hand_skeleton

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Returns a bool value that indicates whether the two hand skeletons are equal.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern bool ar_hand_skeleton_is_equal_to_hand_skeleton(ar_hand_skeleton_t hand_skeleton, ar_hand_skeleton_t other_hand_skeleton);
```

## Return Value

`YES` if the hand skeletons are equal, otherwise `NO`.

## Parameters

- `hand_skeleton`: A hand skeleton to be compared.
- `other_hand_skeleton`: The other hand skeleton to be compared to.

## See Also

### Hand skeleton functions
- [ar_hand_skeleton_create](./ar_hand_skeleton_create.md)
  Create a hand skeleton in a neutral pose that allows access to constants like joint indices, names, counts, etc.
- [ar_hand_skeleton_enumerate_joints](./ar_hand_skeleton_enumerate_joints.md)
  Enumerate the names of joints in an `ar_hand_skeleton_t` using an enumeration block.
- [ar_hand_skeleton_enumerate_joints_f](./ar_hand_skeleton_enumerate_joints_f.md)
  Enumerates the joints in an `ar_hand_skeleton_t` using a function.
- [ar_hand_skeleton_get_joint_count](./ar_hand_skeleton_get_joint_count.md)
  Get the total number of joints in the hand skeleton.
- [ar_hand_skeleton_get_joint_named](./ar_hand_skeleton_get_joint_named.md)
  Get a joint by it’s name from the hand skeleton.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_hand_skeleton_is_equal_to_hand_skeleton)*