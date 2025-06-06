# IKComponent.ConstraintCollection

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
struct ConstraintCollection
```

#### Overview

Supports subscripting by index, element’s identifier or element’s name.

## Topics

### Structures
- [IKComponent.ConstraintCollection.Iterator](ikcomponent/constraintcollection/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
### Instance Properties
- [var count: Int](ikcomponent/constraintcollection/count.md)
  The number of elements in the collection.
- [var endIndex: IKComponent.ConstraintCollection.Index](ikcomponent/constraintcollection/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var isEmpty: Bool](ikcomponent/constraintcollection/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: IKComponent.ConstraintCollection.Index](ikcomponent/constraintcollection/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func contains(IKComponent.ConstraintCollection.Element.ID) -> Bool](ikcomponent/constraintcollection/contains(_:).md)
  Returns a Boolean value that indicates whether the collection contains an element with a specific identifier.
- [func index(after: IKComponent.ConstraintCollection.Index) -> IKComponent.ConstraintCollection.Index](ikcomponent/constraintcollection/index(after:).md)
  Returns the position immediately after the given index.
- [func makeIterator() -> IKComponent.ConstraintCollection.Iterator](ikcomponent/constraintcollection/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func set(IKComponent.ConstraintCollection.Element) -> IKComponent.ConstraintCollection.Element?](ikcomponent/constraintcollection/set(_:).md)
  Updates the element with identifier matching the new value.
### Subscripts
- [subscript(IKComponent.ConstraintCollection.Element.ID) -> IKComponent.ConstraintCollection.Element?](ikcomponent/constraintcollection/subscript(_:)-5ciqk.md)
  Accesses the element with the specified identifier.
- [subscript(IKComponent.ConstraintCollection.Index) -> IKComponent.ConstraintCollection.Element](ikcomponent/constraintcollection/subscript(_:)-97k1h.md)
  Accesses the element at the specified position.
- [subscript(String) -> IKComponent.ConstraintCollection.Element?](ikcomponent/constraintcollection/subscript(_:)-9kcf0.md)
  Accesses the element with the specified name.
### Type Aliases
- [IKComponent.ConstraintCollection.Element](ikcomponent/constraintcollection/element.md)
  A type representing the sequence’s elements.
- [IKComponent.ConstraintCollection.Index](ikcomponent/constraintcollection/index.md)
  A type that represents a position in the collection.
- [IKComponent.ConstraintCollection.Indices](ikcomponent/constraintcollection/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [IKComponent.ConstraintCollection.SubSequence](ikcomponent/constraintcollection/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [Collection Implementations](ikcomponent/constraintcollection/collection-implementations.md)
- [Sequence Implementations](ikcomponent/constraintcollection/sequence-implementations.md)

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
- [IKComponent.SolverCollection](ikcomponent/solvercollection.md)
  Ordered dictionary like container with fixed size.
- [IKComponent.Constraint](ikcomponent/constraint.md)
  The update stage object that lets you read and update the current settings of a single constraint in an IK solver.
- [class IKResource](ikresource.md)
  A reference counted immutable resource which contains one or more inverse kinematics solver rigs.
- [struct IKSolverDefinition](iksolverdefinition.md)
  A container describing a solver instance.
- [IKSolverDefinition.ID](iksolverdefinition/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikcomponent/constraintcollection)*