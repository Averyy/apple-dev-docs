# HandSkeleton.Joint

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

The name and position of an individual hand joint.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct Joint
```

## Topics

### Inspecting hand joints
- [var name: HandSkeleton.JointName](./joint/name.md)
  A name that uniquely identifies this joint among others on the same skeleton.
- [var parentJoint: HandSkeleton.Joint?](./joint/parentjoint.md)
  The joint that’s connected to this joint and more closely connected to the base of the skeleton.
### Tracking the position of hand joints
- [var anchorFromJointTransform: simd_float4x4](./joint/anchorfromjointtransform.md)
  The position and orientation of this joint relative to the base joint of the skeleton.
- [var parentFromJointTransform: simd_float4x4](./joint/parentfromjointtransform.md)
  The transform from the joint to its parent joint’s coordinate system.
- [var isTracked: Bool](./joint/istracked.md)
  A Boolean value that indicates whether ARKit tracks a hand joint.
### Instance Properties
- [var description: String](./joint/description.md)
  A textual representation of this joint.
### Default Implementations
- [ARKitCoordinateSpaceProviding Implementations](./joint/arkitcoordinatespaceproviding-implementations.md)
- [Equatable Implementations](./joint/equatable-implementations.md)

## Relationships

### Conforms To
- [ARKitCoordinateSpaceProviding](../arkitcoordinatespaceproviding.md)
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Retrieving specific hand joints
- [func joint(HandSkeleton.JointName) -> HandSkeleton.Joint](./joint%28_%29.md)
  Retrieves a hand joint based on the joint name you specify.
- [HandSkeleton.JointName](./jointname.md)
  The names of different hand joints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/handskeleton/joint)*