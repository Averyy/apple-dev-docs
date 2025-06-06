# IKRig.ConstraintsCollection

**Framework**: RealityKit  
**Kind**: struct

Ordered dictionary-like container.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct ConstraintsCollection
```

#### Overview

Supports subscripting by index, element’s identifier or element’s name.

## Topics

### Structures
- [IKRig.ConstraintsCollection.Iterator](ikrig/constraintscollection/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
### Initializers
- [init([IKRig.ConstraintsCollection.Element])](ikrig/constraintscollection/init(_:).md)
  Creates a collection with the provided constraints.
- [init(arrayLiteral: IKRig.ConstraintsCollection.Element...)](ikrig/constraintscollection/init(arrayliteral:).md)
  Creates an instance initialized with the given elements.
### Instance Properties
- [var count: Int](ikrig/constraintscollection/count.md)
  The number of elements in the collection.
- [var endIndex: IKRig.ConstraintsCollection.Index](ikrig/constraintscollection/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var isEmpty: Bool](ikrig/constraintscollection/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: IKRig.ConstraintsCollection.Index](ikrig/constraintscollection/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func contains(IKRig.ConstraintsCollection.Element.ID) -> Bool](ikrig/constraintscollection/contains(_:).md)
  Returns a Boolean value that indicates whether the collection contains an element with a specific identifier.
- [func index(after: IKRig.ConstraintsCollection.Index) -> IKRig.ConstraintsCollection.Index](ikrig/constraintscollection/index(after:).md)
  Returns the position immediately after the given index.
- [func makeIterator() -> IKRig.ConstraintsCollection.Iterator](ikrig/constraintscollection/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func set(IKRig.ConstraintsCollection.Element) -> IKRig.ConstraintsCollection.Element?](ikrig/constraintscollection/set(_:).md)
  Updates the element with identifier matching the provided value’s identifier.
### Subscripts
- [subscript(String) -> IKRig.ConstraintsCollection.Element?](ikrig/constraintscollection/subscript(_:)-2egqx.md)
  Accesses the element with the specified name.
- [subscript(IKRig.ConstraintsCollection.Element.ID) -> IKRig.ConstraintsCollection.Element?](ikrig/constraintscollection/subscript(_:)-4uqhz.md)
  Accesses the element with the specified identifier.
- [subscript(IKRig.ConstraintsCollection.Index) -> IKRig.ConstraintsCollection.Element](ikrig/constraintscollection/subscript(_:)-8zkqi.md)
  Accesses the element at the specified position.
### Type Aliases
- [IKRig.ConstraintsCollection.ArrayLiteralElement](ikrig/constraintscollection/arrayliteralelement.md)
  The type of the elements of an array literal.
- [IKRig.ConstraintsCollection.Element](ikrig/constraintscollection/element.md)
  A type representing the sequence’s elements.
- [IKRig.ConstraintsCollection.Index](ikrig/constraintscollection/index.md)
  A type that represents a position in the collection.
- [IKRig.ConstraintsCollection.Indices](ikrig/constraintscollection/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [IKRig.ConstraintsCollection.SubSequence](ikrig/constraintscollection/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [Collection Implementations](ikrig/constraintscollection/collection-implementations.md)
- [Sequence Implementations](ikrig/constraintscollection/sequence-implementations.md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct IKRig](ikrig.md)
  A full body inverse kinematics rig definition for a single skeleton.
- [struct Joint](ikrig/joint.md)
  A definition of a rig joint and its IK solver settings.
- [struct JointCollection](ikrig/jointcollection.md)
  Ordered dictionary-like container with a fixed size.
- [struct Constraint](ikrig/constraint.md)
  A definition of a rig constraint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/constraintscollection)*