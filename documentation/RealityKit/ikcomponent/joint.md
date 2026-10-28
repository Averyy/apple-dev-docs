# IKComponent.Joint

**Framework**: RealityKit  
**Kind**: class  
**Role**: Class

The update stage object that lets you read and update the current settings of a single joint in an IK solver.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
class Joint
```

## Overview

The settings this object exposes are the runtime editable values of a solver joint. Initial values are set in [`IKRig.Joint`](../ikrig/joint.md).

## Topics

### Instance Properties
- [var fkWeightPerAxis: SIMD3<Float>](./joint/fkweightperaxis.md)
  The per-axis weight of the source animation demand on the joint.
- [let id: IKComponent.Joint.ID](./joint/id.md)
  The identifier of this joint.
- [var name: String](./joint/name.md)
  The name of the joint.
- [var rotationStiffness: SIMD3<Float>](./joint/rotationstiffness.md)
  The per-axis rotational stiffness of the joint.

## Relationships

### Conforms To
- [Identifiable](../../Swift/identifiable.md)

## See Also

### Inverse kinematics components
- [struct IKComponent](../ikcomponent.md)
  A component that allows you to procedurally animate a skeletal model using a full body inverse kinematics solver.
- [IKComponent.JointCollection](./jointcollection.md)
  Ordered dictionary like container with fixed size.
- [IKComponent.Solver](./solver.md)
  The update stage object that lets you read and update the current settings of a single solver instance.
- [IKComponent.SolverCollection](./solvercollection.md)
  Ordered dictionary like container with fixed size.
- [IKComponent.Constraint](./constraint.md)
  The update stage object that lets you read and update the current settings of a single constraint in an IK solver.
- [IKComponent.ConstraintCollection](./constraintcollection.md)
  Ordered dictionary like container with fixed size.
- [class IKResource](../ikresource.md)
  A reference counted immutable resource which contains one or more inverse kinematics solver rigs.
- [struct IKSolverDefinition](../iksolverdefinition.md)
  A container describing a solver instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikcomponent/joint)*