# ar_hand_skeleton_create

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Create a hand skeleton in a neutral pose that allows access to constants like joint indices, names, counts, etc.

**Availability**:
- visionOS 1.0+

## Declaration

```c
extern ar_hand_skeleton_tar_hand_skeleton_create();
```

## Return Value

An instance of `ar_hand_skeleton_t`.

## Discussion

> **Note**: This type supports ARC. In non-ARC files, use `ar_retain()` and `ar_release()` to retain and release the object.

## See Also

### Hand skeleton functions
- [ar_hand_skeleton_enumerate_joints](./ar_hand_skeleton_enumerate_joints.md)
  Enumerate the names of joints in an `ar_hand_skeleton_t` using an enumeration block.
- [ar_hand_skeleton_enumerate_joints_f](./ar_hand_skeleton_enumerate_joints_f.md)
  Enumerates the joints in an `ar_hand_skeleton_t` using a function.
- [ar_hand_skeleton_get_joint_count](./ar_hand_skeleton_get_joint_count.md)
  Get the total number of joints in the hand skeleton.
- [ar_hand_skeleton_get_joint_named](./ar_hand_skeleton_get_joint_named.md)
  Get a joint by it’s name from the hand skeleton.
- [ar_hand_skeleton_is_equal_to_hand_skeleton](./ar_hand_skeleton_is_equal_to_hand_skeleton.md)
  Returns a bool value that indicates whether the two hand skeletons are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_hand_skeleton_create)*