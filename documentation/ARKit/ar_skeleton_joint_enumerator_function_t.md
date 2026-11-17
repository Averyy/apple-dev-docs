# ar_skeleton_joint_enumerator_function_t

**Framework**: ARKit  
**Kind**: typealias  
**Role**: Type Alias

Function for enumerating skeleton joints.

**Availability**:
- visionOS 1.0+

## Declaration

```c
typedef _Bool (*)(void *, NSObject<OS_ar_skeleton_joint> *) ar_skeleton_joint_enumerator_function_t;
```

## Return Value

`true` to continue enumerating to the next joint, `false` to stop enumerating.

## Parameters

- `context`: The application-defined context.
- `joint`: The joint.

## See Also

### Skeleton joint data types
- [ar_skeleton_joint_enumerator_t](./ar_skeleton_joint_enumerator_t.md)
  Handler for enumerating skeleton joints.
- [ar_skeleton_joint_t](./ar_skeleton_joint_t.md)
  Represents a joint in a skeleton with its transform and tracking state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_skeleton_joint_enumerator_function_t)*