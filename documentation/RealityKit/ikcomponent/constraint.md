# IKComponent.Constraint

**Framework**: RealityKit  
**Kind**: class  
**Role**: Class

The update stage object that lets you read and update the current settings of a single constraint in an IK solver.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
class Constraint
```

## Overview

The settings this object exposes are the runtime editable values of the solver constraint. Initial values are set in [`IKRig.Constraint`](../ikrig/constraint.md).

## Topics

### Structures
- [IKComponent.Constraint.DemandOptions](./constraint/demandoptions.md)
  Flags for the different demands types that can be active in a single constraint.
### Instance Properties
- [var animationOverrideWeight: (position: Float, rotation: Float)](./constraint/animationoverrideweight.md)
  The blending weights between the FK demand and the your target per demand type.
- [var demands: IKComponent.Constraint.DemandOptions](./constraint/demands.md)
  The set of the active demands of the constraint.
- [let id: IKComponent.Constraint.ID](./constraint/id.md)
  ID of the constraint, that is unique within the solver instance.
- [var jointID: IKComponent.Joint.ID](./constraint/jointid.md)
  The identifier of the constrained rig joint.
- [var lookAtTargetPosition: SIMD3<Float>](./constraint/lookattargetposition.md)
  The point demand which the look-at constraint uses to generate a new orientation demand.
- [var name: String](./constraint/name.md)
  The name of the constraint as defined in the rig.
- [var offset: Transform](./constraint/offset.md)
  The offset applied on top of the target transform before the solve.
- [var target: Transform](./constraint/target.md)
  The packed targets for the positional and orientational demands in model space.

## Relationships

### Conforms To
- [Identifiable](../../Swift/identifiable.md)

## See Also

### Inverse kinematics components
- [struct IKComponent](../ikcomponent.md)
  A component that allows you to procedurally animate a skeletal model using a full body inverse kinematics solver.
- [IKComponent.Joint](./joint.md)
  The update stage object that lets you read and update the current settings of a single joint in an IK solver.
- [IKComponent.JointCollection](./jointcollection.md)
  Ordered dictionary like container with fixed size.
- [IKComponent.Solver](./solver.md)
  The update stage object that lets you read and update the current settings of a single solver instance.
- [IKComponent.SolverCollection](./solvercollection.md)
  Ordered dictionary like container with fixed size.
- [IKComponent.ConstraintCollection](./constraintcollection.md)
  Ordered dictionary like container with fixed size.
- [class IKResource](../ikresource.md)
  A reference counted immutable resource which contains one or more inverse kinematics solver rigs.
- [struct IKSolverDefinition](../iksolverdefinition.md)
  A container describing a solver instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikcomponent/constraint)*