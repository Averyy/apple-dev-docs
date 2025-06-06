# IKRig.JointCollection

**Framework**: RealityKit  
**Kind**: struct

Ordered dictionary-like container with a fixed size.

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
- [IKRig.JointCollection.Iterator](ikrig/jointcollection/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
### Instance Properties
- [var count: Int](ikrig/jointcollection/count.md)
  The number of elements in the collection.
- [var endIndex: IKRig.JointCollection.Index](ikrig/jointcollection/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var isEmpty: Bool](ikrig/jointcollection/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: IKRig.JointCollection.Index](ikrig/jointcollection/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func contains(IKRig.JointCollection.Element.ID) -> Bool](ikrig/jointcollection/contains(_:).md)
  Returns a Boolean value that indicates whether the collection contains an element with a specific identifier.
- [func forEach(descendantOf: String, inclusive: Bool, update: (inout IKRig.JointCollection.Element) -> Void)](ikrig/jointcollection/foreach(descendantof:inclusive:update:).md)
  Calls the provided closure on each element in the hierarchy rooted at the named joint.
- [func index(after: IKRig.JointCollection.Index) -> IKRig.JointCollection.Index](ikrig/jointcollection/index(after:).md)
  Returns the position immediately after the given index.
- [func makeIterator() -> IKRig.JointCollection.Iterator](ikrig/jointcollection/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func set(IKRig.JointCollection.Element) -> IKRig.JointCollection.Element?](ikrig/jointcollection/set(_:).md)
  Updates the element with identifier matching the provided value’s identifier.
### Subscripts
- [subscript(String) -> IKRig.JointCollection.Element?](ikrig/jointcollection/subscript(_:)-3vtbs.md)
  Accesses the element with the specified name.
- [subscript(IKRig.JointCollection.Element.ID) -> IKRig.JointCollection.Element?](ikrig/jointcollection/subscript(_:)-5317p.md)
  Accesses the element with the specified identifier.
- [subscript(IKRig.JointCollection.Index) -> IKRig.JointCollection.Element](ikrig/jointcollection/subscript(_:)-6stmh.md)
  Accesses the element at the specified position.
### Type Aliases
- [IKRig.JointCollection.Element](ikrig/jointcollection/element.md)
  A type representing the sequence’s elements.
- [IKRig.JointCollection.Index](ikrig/jointcollection/index.md)
  A type that represents a position in the collection.
- [IKRig.JointCollection.Indices](ikrig/jointcollection/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [IKRig.JointCollection.SubSequence](ikrig/jointcollection/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [Collection Implementations](ikrig/jointcollection/collection-implementations.md)
- [Sequence Implementations](ikrig/jointcollection/sequence-implementations.md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct IKRig](ikrig.md)
  A full body inverse kinematics rig definition for a single skeleton.
- [struct Joint](ikrig/joint.md)
  A definition of a rig joint and its IK solver settings.
- [struct Constraint](ikrig/constraint.md)
  A definition of a rig constraint.
- [struct ConstraintsCollection](ikrig/constraintscollection.md)
  Ordered dictionary-like container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/jointcollection)*