# IKRig.Joint

**Framework**: RealityKit  
**Kind**: struct

A definition of a rig joint and its IK solver settings.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct Joint
```

## Topics

### Structures
- [IKRig.Joint.ID](ikrig/joint/id-swift.struct.md)
  The identity type for a joint in a rig.
- [IKRig.Joint.LimitsDefinition](ikrig/joint/limitsdefinition.md)
  A definition of joint rotation limits.
### Initializers
- [init(name: String, parentID: IKRig.Joint.ID?, restTransform: Transform)](ikrig/joint/init(name:parentid:resttransform:).md)
  Creates a joint with the provided base elements.
### Instance Properties
- [var active: Bool](ikrig/joint/active.md)
  A boolean value that sets whether the solver rotates the joint.
- [var fkWeightPerAxis: SIMD3<Float>](ikrig/joint/fkweightperaxis.md)
  The per-axis weight of the FK demand on the joint.
- [var id: IKRig.Joint.ID](ikrig/joint/id-swift.property.md)
  The identifier of the joint.
- [var limits: IKRig.Joint.LimitsDefinition?](ikrig/joint/limits.md)
  The per-axis rotation limits of the joint.
- [let name: String](ikrig/joint/name.md)
  The name of the joint.
- [var parentID: IKRig.Joint.ID?](ikrig/joint/parentid.md)
  The identifier of the parent joint if there is one.
- [var restTransform: Transform](ikrig/joint/resttransform.md)
  The local space transformation of the joint in the solver’s rest pose.
- [var rotationStiffness: SIMD3<Float>](ikrig/joint/rotationstiffness.md)
  The per-axis rotational stiffness of the joint.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [struct IKRig](ikrig.md)
  A full body inverse kinematics rig definition for a single skeleton.
- [struct JointCollection](ikrig/jointcollection.md)
  Ordered dictionary-like container with a fixed size.
- [struct Constraint](ikrig/constraint.md)
  A definition of a rig constraint.
- [struct ConstraintsCollection](ikrig/constraintscollection.md)
  Ordered dictionary-like container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/joint)*