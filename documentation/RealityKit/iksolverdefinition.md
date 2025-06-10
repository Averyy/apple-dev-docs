# IKSolverDefinition

**Framework**: RealityKit  
**Kind**: struct

A container describing a solver instance.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
struct IKSolverDefinition
```

#### Overview

Adds unique identifier for each solver instance as the rig can be reused.

## Topics

### Initializers
- [init(id: IKSolverDefinition.ID, rig: IKRig)](iksolverdefinition/init(id:rig:).md)
  Creates a solver definition for with a unique solver identifier and a rig.
### Instance Properties
- [let id: IKSolverDefinition.ID](iksolverdefinition/id.md)
  The identifier of the solver instance.
- [var rigDefinition: IKRig](iksolverdefinition/rigdefinition.md)
  The solver’s rig definition.

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
- [IKComponent.Constraint](ikcomponent/constraint.md)
  The update stage object that lets you read and update the current settings of a single constraint in an IK solver.
- [IKComponent.ConstraintCollection](ikcomponent/constraintcollection.md)
  Ordered dictionary like container with fixed size.
- [class IKResource](ikresource.md)
  A reference counted immutable resource which contains one or more inverse kinematics solver rigs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/iksolverdefinition)*