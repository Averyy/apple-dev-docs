# PhysicsJoints

**Framework**: RealityKit  
**Kind**: struct

A collection of physics joints.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct PhysicsJoints
```

## Topics

### Operators
- [static func == (PhysicsJoints, PhysicsJoints) -> Bool](physicsjoints/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init()](physicsjoints/init.md)
  Creates a new, empty collection.
- [init(any Sequence<any PhysicsJoint>)](physicsjoints/init(_:).md)
- [init(arrayLiteral: any PhysicsJoint...)](physicsjoints/init(arrayliteral:).md)
  Creates an instance initialized with the given elements.
### Instance Properties
- [var count: Int](physicsjoints/count.md)
  The number of elements in the collection.
- [var endIndex: Int](physicsjoints/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [let startIndex: Int](physicsjoints/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func index(after: Int) -> Int](physicsjoints/index(after:).md)
  Returns the position immediately after the given index.
- [func index(before: Int) -> Int](physicsjoints/index(before:).md)
  Returns the position immediately before the given index.
- [func replaceSubrange<C>(Range<Int>, with: C)](physicsjoints/replacesubrange(_:with:).md)
  Replaces the specified subrange of elements with the given collection.
### Subscripts
- [subscript(Int) -> any PhysicsJoint](physicsjoints/subscript(_:).md)
  Accesses the element at the specified position.
### Type Aliases
- [PhysicsJoints.ArrayLiteralElement](physicsjoints/arrayliteralelement.md)
  The type of the elements of an array literal.
- [PhysicsJoints.Element](physicsjoints/element.md)
  A type representing the sequence’s elements.
- [PhysicsJoints.Index](physicsjoints/index.md)
  A type that represents a position in the collection.
- [PhysicsJoints.Indices](physicsjoints/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [PhysicsJoints.Iterator](physicsjoints/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [PhysicsJoints.SubSequence](physicsjoints/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [BidirectionalCollection Implementations](physicsjoints/bidirectionalcollection-implementations.md)
- [Collection Implementations](physicsjoints/collection-implementations.md)
- [Equatable Implementations](physicsjoints/equatable-implementations.md)
- [MutableCollection Implementations](physicsjoints/mutablecollection-implementations.md)
- [RangeReplaceableCollection Implementations](physicsjoints/rangereplaceablecollection-implementations.md)
- [Sequence Implementations](physicsjoints/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [MutableCollection](../Swift/MutableCollection.md)
- [RangeReplaceableCollection](../Swift/RangeReplaceableCollection.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct PhysicsRevoluteJoint](physicsrevolutejoint.md)
  A joint that allows one degree of rotational freedom between two entity pins, similar to a door swinging on its hinges.
- [struct PhysicsPrismaticJoint](physicsprismaticjoint.md)
  A joint that allows movement along a straight line, similar to a sliding drawer.
- [struct PhysicsSphericalJoint](physicssphericaljoint.md)
  A spherical joint that allows free rotational movement between two entities’ pins.
- [struct PhysicsCustomJoint](physicscustomjoint.md)
  A joint with six degrees of freedom that can be individually specified.
- [struct PhysicsDistanceJoint](physicsdistancejoint.md)
  A joint that maintains a minimum and maximum distance between two entity pins.
- [struct PhysicsFixedJoint](physicsfixedjoint.md)
  A joint that rigidly connects two entity pins, with zero degrees of freedom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsjoints)*