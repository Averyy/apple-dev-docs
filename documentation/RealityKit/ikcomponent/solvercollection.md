# IKComponent.SolverCollection

**Framework**: RealityKit  
**Kind**: struct

Ordered dictionary like container with fixed size.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct SolverCollection
```

#### Overview

Supports subscripting by index, element’s identifier or element’s name.

## Topics

### Structures
- [IKComponent.SolverCollection.Iterator](ikcomponent/solvercollection/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
### Instance Properties
- [var count: Int](ikcomponent/solvercollection/count.md)
  The number of elements in the collection.
- [var endIndex: IKComponent.SolverCollection.Index](ikcomponent/solvercollection/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var isEmpty: Bool](ikcomponent/solvercollection/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: IKComponent.SolverCollection.Index](ikcomponent/solvercollection/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func contains(IKComponent.SolverCollection.Element.ID) -> Bool](ikcomponent/solvercollection/contains(_:).md)
  Returns a Boolean value that indicates whether the collection contains an element with a specific identifier.
- [func index(after: IKComponent.SolverCollection.Index) -> IKComponent.SolverCollection.Index](ikcomponent/solvercollection/index(after:).md)
  Returns the position immediately after the given index.
- [func makeIterator() -> IKComponent.SolverCollection.Iterator](ikcomponent/solvercollection/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func set(IKComponent.SolverCollection.Element) -> IKComponent.SolverCollection.Element?](ikcomponent/solvercollection/set(_:).md)
  Updates the element with identifier matching the new value.
### Subscripts
- [subscript(IKComponent.SolverCollection.Element.ID) -> IKComponent.SolverCollection.Element?](ikcomponent/solvercollection/subscript(_:)-3kxyb.md)
  Accesses the element with the specified identifier.
- [subscript(IKComponent.SolverCollection.Index) -> IKComponent.SolverCollection.Element](ikcomponent/solvercollection/subscript(_:)-672e7.md)
  Accesses the element at the specified position.
### Type Aliases
- [IKComponent.SolverCollection.Element](ikcomponent/solvercollection/element.md)
  A type representing the sequence’s elements.
- [IKComponent.SolverCollection.Index](ikcomponent/solvercollection/index.md)
  A type that represents a position in the collection.
- [IKComponent.SolverCollection.Indices](ikcomponent/solvercollection/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [IKComponent.SolverCollection.SubSequence](ikcomponent/solvercollection/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [Collection Implementations](ikcomponent/solvercollection/collection-implementations.md)
- [Sequence Implementations](ikcomponent/solvercollection/sequence-implementations.md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct IKComponent](ikcomponent.md)
  A component that allows you to procedurally animate a skeletal model using a full body inverse kinematics solver.
- [IKComponent.Joint](ikcomponent/joint.md)
  The update stage object that lets you read and update the current settings of a single joint in an IK solver.
- [IKComponent.JointCollection](ikcomponent/jointcollection.md)
  Ordered dictionary like container with fixed size.
- [IKComponent.Solver](ikcomponent/solver.md)
  The update stage object that lets you read and update the current settings of a single solver instance.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikcomponent/solvercollection)*