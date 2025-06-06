# HandSkeleton.Joint

**Framework**: ARKit  
**Kind**: struct

The name and position of an individual hand joint.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct Joint
```

## Topics

### Inspecting hand joints
- [var name: HandSkeleton.JointName](handskeleton/joint/name.md)
  A name that uniquely identifies this joint among others on the same skeleton.
- [var parentJoint: HandSkeleton.Joint?](handskeleton/joint/parentjoint.md)
  The joint that’s connected to this joint and more closely connected to the base of the skeleton.
### Tracking the position of hand joints
- [var anchorFromJointTransform: simd_float4x4](handskeleton/joint/anchorfromjointtransform.md)
  The position and orientation of this joint relative to the base joint of the skeleton.
- [var parentFromJointTransform: simd_float4x4](handskeleton/joint/parentfromjointtransform.md)
  The transform from the joint to its parent joint’s coordinate system.
- [var isTracked: Bool](handskeleton/joint/istracked.md)
  A Boolean value that indicates whether ARKit is currently tracking this joint.
### Instance Properties
- [var description: String](handskeleton/joint/description.md)
  A textual representation of this joint.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func joint(HandSkeleton.JointName) -> HandSkeleton.Joint](handskeleton/joint(_:).md)
  Retrieves a hand joint based on the joint name you specify.
- [HandSkeleton.JointName](handskeleton/jointname.md)
  The names of different hand joints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/handskeleton/joint)*