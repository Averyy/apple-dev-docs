# ar_hand_skeleton_enumerate_joints_f

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Enumerates the joints in an `ar_hand_skeleton_t` using a function.

**Availability**:
- visionOS 1.0+

## Declaration

```c
extern void ar_hand_skeleton_enumerate_joints_f(ar_hand_skeleton_t hand_skeleton, void *context, ar_skeleton_joint_enumerator_function_t joint_enumerator_function);
```

## Parameters

- `hand_skeleton`: The hand skeleton.
- `context`: The application-defined context parameter to pass to the function.
- `joint_enumerator_function`: The enumerator function.

## See Also

### Hand skeleton functions
- [ar_hand_skeleton_create](./ar_hand_skeleton_create.md)
  Create a hand skeleton in a neutral pose that allows access to constants like joint indices, names, counts, etc.
- [ar_hand_skeleton_enumerate_joints](./ar_hand_skeleton_enumerate_joints.md)
  Enumerate the names of joints in an `ar_hand_skeleton_t` using an enumeration block.
- [ar_hand_skeleton_get_joint_count](./ar_hand_skeleton_get_joint_count.md)
  Get the total number of joints in the hand skeleton.
- [ar_hand_skeleton_get_joint_named](./ar_hand_skeleton_get_joint_named.md)
  Get a joint by it’s name from the hand skeleton.
- [ar_hand_skeleton_is_equal_to_hand_skeleton](./ar_hand_skeleton_is_equal_to_hand_skeleton.md)
  Returns a bool value that indicates whether the two hand skeletons are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_hand_skeleton_enumerate_joints_f)*