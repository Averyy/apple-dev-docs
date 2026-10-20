# IKComponent.SolverCollection

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Ordered dictionary like container with fixed size.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct SolverCollection
```

#### Overview

Supports subscripting by index, element’s identifier or element’s name.

## Topics

### Instance Properties
- [var count: Int](./solvercollection/count.md)
  The number of elements in the collection.
- [var isEmpty: Bool](./solvercollection/isempty.md)
  A Boolean value indicating whether the collection is empty.
### Instance Methods
- [func contains(IKComponent.SolverCollection.Element.ID) -> Bool](./solvercollection/contains%28_%29.md)
  Returns a Boolean value that indicates whether the collection contains an element with a specific identifier.
- [func set(IKComponent.SolverCollection.Element) -> IKComponent.SolverCollection.Element?](./solvercollection/set%28_%29.md)
  Updates the element with identifier matching the new value.
### Subscripts
- [subscript(IKComponent.SolverCollection.Element.ID) -> IKComponent.SolverCollection.Element?](./solvercollection/subscript%28_%29.md)
  Accesses the element with the specified identifier.

## Relationships

### Conforms To
- [Collection](../../Swift/collection.md)
- [Sequence](../../Swift/sequence.md)

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
- [IKComponent.Constraint](./constraint.md)
  The update stage object that lets you read and update the current settings of a single constraint in an IK solver.
- [IKComponent.ConstraintCollection](./constraintcollection.md)
  Ordered dictionary like container with fixed size.
- [class IKResource](../ikresource.md)
  A reference counted immutable resource which contains one or more inverse kinematics solver rigs.
- [struct IKSolverDefinition](../iksolverdefinition.md)
  A container describing a solver instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikcomponent/solvercollection)*