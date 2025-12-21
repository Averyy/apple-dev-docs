# IKComponent.Constraint

**Framework**: RealityKit  
**Kind**: class

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

#### Overview

The settings this object exposes are the runtime editable values of the solver constraint. Initial values are set in [`IKRig.Constraint`](ikrig/constraint.md).

## Topics

### Structures
- [IKComponent.Constraint.DemandOptions](ikcomponent/constraint/demandoptions.md)
  Flags for the different demands types that can be active in a single constraint.
### Instance Properties
- [var animationOverrideWeight: (position: Float, rotation: Float)](ikcomponent/constraint/animationoverrideweight.md)
  The blending weights between the FK demand and the your target per demand type.
- [var demands: IKComponent.Constraint.DemandOptions](ikcomponent/constraint/demands.md)
  The set of the active demands of the constraint.
- [let id: IKComponent.Constraint.ID](ikcomponent/constraint/id.md)
  ID of the constraint, that is unique within the solver instance.
- [var jointID: IKComponent.Joint.ID](ikcomponent/constraint/jointid.md)
  The identifier of the constrained rig joint.
- [var lookAtTargetPosition: SIMD3<Float>](ikcomponent/constraint/lookattargetposition.md)
  The point demand which the look-at constraint uses to generate a new orientation demand.
- [var name: String](ikcomponent/constraint/name.md)
  The name of the constraint as defined in the rig.
- [var offset: Transform](ikcomponent/constraint/offset.md)
  The offset applied on top of the target transform before the solve.
- [var target: Transform](ikcomponent/constraint/target.md)
  The packed targets for the positional and orientational demands in model space.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [struct IKComponent](ikcomponent.md)
  A component that allows you to procedurally animate a skeletal model using a full body inverse kinematics solver.
- [IKComponent.Joint](ikcomponent/joint.md)
  The update stage object that lets you read and update the current settings of a single joint in an IK solver.
- [IKComponent.JointCollection](ikcomponent/jointcollection.md)
  Ordered dictionary like container with fixed size.
- [IKComponent.Solver](ikcomponent/solver.md)
  The update stage object that lets you read and update the current settings of a single solver instance.
- [IKComponent.SolverCollection](ikcomponent/solvercollection.md)
  Ordered dictionary like container with fixed size.
- [IKComponent.ConstraintCollection](ikcomponent/constraintcollection.md)
  Ordered dictionary like container with fixed size.
- [class IKResource](ikresource.md)
  A reference counted immutable resource which contains one or more inverse kinematics solver rigs.
- [struct IKSolverDefinition](iksolverdefinition.md)
  A container describing a solver instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikcomponent/constraint)*