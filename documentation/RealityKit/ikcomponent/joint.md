# IKComponent.Joint

**Framework**: RealityKit  
**Kind**: class

The update stage object that lets you read and update the current settings of a single joint in an IK solver.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
class Joint
```

#### Overview

The settings this object exposes are the runtime editable values of a solver joint. Initial values are set in [`IKRig.Joint`](ikrig/joint.md).

## Topics

### Instance Properties
- [var fkWeightPerAxis: SIMD3<Float>](ikcomponent/joint/fkweightperaxis.md)
  The per-axis weight of the source animation demand on the joint.
- [let id: IKComponent.Joint.ID](ikcomponent/joint/id-swift.property.md)
  The identifier of this joint.
- [var name: String](ikcomponent/joint/name.md)
  The name of the joint.
- [var rotationStiffness: SIMD3<Float>](ikcomponent/joint/rotationstiffness.md)
  The per-axis rotational stiffness of the joint.
### Type Aliases
- [IKComponent.Joint.ID](ikcomponent/joint/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [struct IKComponent](ikcomponent.md)
  A component that allows you to procedurally animate a skeletal model using a full body inverse kinematics solver.
- [IKComponent.JointCollection](ikcomponent/jointcollection.md)
  Ordered dictionary like container with fixed size.
- [IKComponent.Solver](ikcomponent/solver.md)
  The update stage object that lets you read and update the current settings of a single solver instance.
- [IKComponent.SolverCollection](ikcomponent/solvercollection.md)
  Ordered dictionary like container with fixed size.
- [IKComponent.Constraint](ikcomponent/constraint.md)
  The update stage object that lets you read and update the current settings of a single constraint in an IK solver.
- [IKComponent.ConstraintCollection](ikcomponent/constraintcollection.md)
  Ordered dictionary like container with fixed size.
- [class IKResource](ikresource.md)
  A reference counted immutable resource which contains one or more inverse kinematics solver rigs.
- [struct IKSolverDefinition](iksolverdefinition.md)
  A container describing a solver instance.
- [IKSolverDefinition.ID](iksolverdefinition/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikcomponent/joint)*