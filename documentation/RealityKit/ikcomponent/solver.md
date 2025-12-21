# IKComponent.Solver

**Framework**: RealityKit  
**Kind**: class

The update stage object that lets you read and update the current settings of a single solver instance.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
class Solver
```

#### Overview

The settings this object exposes are the runtime editable values on the solver instance itself, the solver joints and constraints. For the full list of settings adjustable during creation, see [`IKRig`](ikrig.md).

## Topics

### Structures
- [IKComponent.Solver.ID](ikcomponent/solver/id-swift.struct.md)
  The solver instance identifier type.
### Instance Properties
- [var constraints: IKComponent.ConstraintCollection](ikcomponent/solver/constraints.md)
  The collection of all of the constraint update stage objects of the solver instance.
- [var globalFkWeight: Float](ikcomponent/solver/globalfkweight.md)
  The solver global forward kinematics demand’s weight.
- [var id: IKComponent.Solver.ID](ikcomponent/solver/id-swift.property.md)
  The solver instance identifier.
- [var joints: IKComponent.JointCollection](ikcomponent/solver/joints.md)
  The collection of all of the joint update stage objects of the solver instance.
- [var maxIterations: Int](ikcomponent/solver/maxiterations.md)
  The maximum number of iterations the solver is allowed to do per frame.
### Instance Methods
- [func reset()](ikcomponent/solver/reset.md)
  Enqueues a solver reset call that executes before the next solve.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikcomponent/solver)*