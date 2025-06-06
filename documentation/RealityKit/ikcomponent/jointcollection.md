# IKComponent.JointCollection

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
struct JointCollection
```

#### Overview

Supports subscripting by index, element’s identifier or element’s name.

## Topics

### Structures
- [IKComponent.JointCollection.Iterator](ikcomponent/jointcollection/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
### Instance Properties
- [var count: Int](ikcomponent/jointcollection/count.md)
  The number of elements in the collection.
- [var endIndex: IKComponent.JointCollection.Index](ikcomponent/jointcollection/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var isEmpty: Bool](ikcomponent/jointcollection/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: IKComponent.JointCollection.Index](ikcomponent/jointcollection/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func contains(IKComponent.JointCollection.Element.ID) -> Bool](ikcomponent/jointcollection/contains(_:).md)
  Returns a Boolean value that indicates whether the collection contains an element with a specific identifier.
- [func index(after: IKComponent.JointCollection.Index) -> IKComponent.JointCollection.Index](ikcomponent/jointcollection/index(after:).md)
  Returns the position immediately after the given index.
- [func makeIterator() -> IKComponent.JointCollection.Iterator](ikcomponent/jointcollection/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func set(IKComponent.JointCollection.Element) -> IKComponent.JointCollection.Element?](ikcomponent/jointcollection/set(_:).md)
  Updates the element with identifier matching the new value.
### Subscripts
- [subscript(IKComponent.JointCollection.Index) -> IKComponent.JointCollection.Element](ikcomponent/jointcollection/subscript(_:)-6b7ld.md)
  Accesses the element at the specified position.
- [subscript(String) -> IKComponent.JointCollection.Element?](ikcomponent/jointcollection/subscript(_:)-91341.md)
  Accesses the element with the specified name.
- [subscript(IKComponent.JointCollection.Element.ID) -> IKComponent.JointCollection.Element?](ikcomponent/jointcollection/subscript(_:)-9nqnp.md)
  Accesses the element with the specified identifier.
### Type Aliases
- [IKComponent.JointCollection.Element](ikcomponent/jointcollection/element.md)
  A type representing the sequence’s elements.
- [IKComponent.JointCollection.Index](ikcomponent/jointcollection/index.md)
  A type that represents a position in the collection.
- [IKComponent.JointCollection.Indices](ikcomponent/jointcollection/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [IKComponent.JointCollection.SubSequence](ikcomponent/jointcollection/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [Collection Implementations](ikcomponent/jointcollection/collection-implementations.md)
- [Sequence Implementations](ikcomponent/jointcollection/sequence-implementations.md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct IKComponent](ikcomponent.md)
  A component that allows you to procedurally animate a skeletal model using a full body inverse kinematics solver.
- [IKComponent.Joint](ikcomponent/joint.md)
  The update stage object that lets you read and update the current settings of a single joint in an IK solver.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikcomponent/jointcollection)*