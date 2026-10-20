# IKComponent.ConstraintCollection

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
struct ConstraintCollection
```

#### Overview

Supports subscripting by index, element’s identifier or element’s name.

## Topics

### Instance Properties
- [var count: Int](./constraintcollection/count.md)
  The number of elements in the collection.
- [var isEmpty: Bool](./constraintcollection/isempty.md)
  A Boolean value indicating whether the collection is empty.
### Instance Methods
- [func contains(IKComponent.ConstraintCollection.Element.ID) -> Bool](./constraintcollection/contains%28_%29.md)
  Returns a Boolean value that indicates whether the collection contains an element with a specific identifier.
- [func set(IKComponent.ConstraintCollection.Element) -> IKComponent.ConstraintCollection.Element?](./constraintcollection/set%28_%29.md)
  Updates the element with identifier matching the new value.
### Subscripts
- [subscript(_:)](./constraintcollection/subscript%28_%29.md)
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
- [IKComponent.SolverCollection](./solvercollection.md)
  Ordered dictionary like container with fixed size.
- [IKComponent.Constraint](./constraint.md)
  The update stage object that lets you read and update the current settings of a single constraint in an IK solver.
- [class IKResource](../ikresource.md)
  A reference counted immutable resource which contains one or more inverse kinematics solver rigs.
- [struct IKSolverDefinition](../iksolverdefinition.md)
  A container describing a solver instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikcomponent/constraintcollection)*