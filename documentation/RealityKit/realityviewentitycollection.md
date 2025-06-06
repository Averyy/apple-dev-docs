# RealityViewEntityCollection

**Framework**: RealityKit  
**Kind**: struct

A collection of entities in a RealityView.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct RealityViewEntityCollection
```

#### Overview

This collection is used by [`entities`](realityviewcontent/entities-swift.property.md).

## Topics

### Instance Properties
- [var count: Int](realityviewentitycollection/count.md)
  The number of elements in the collection.
- [var endIndex: Int](realityviewentitycollection/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var startIndex: Int](realityviewentitycollection/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func append<S>(contentsOf: S)](realityviewentitycollection/append(contentsof:).md)
  Adds the specified sequence of entities to the end of this collection, in order.
- [func index(after: Int) -> Int](realityviewentitycollection/index(after:).md)
  Returns the position immediately after the given index.
- [func insert<S>(contentsOf: S, beforeIndex: Int)](realityviewentitycollection/insert(contentsof:beforeindex:).md)
  Adds the specified sequence of entities to this collection in order, directly before the entity at the given index.
- [func remove(Entity)](realityviewentitycollection/remove(_:).md)
  Removes the entity from the collection.
- [func remove(at: Int)](realityviewentitycollection/remove(at:).md)
  Removes the entity at the given index from this collection.
- [func removeAll()](realityviewentitycollection/removeall.md)
  Removes all entities from this collection.
- [func replaceAll<S>(S)](realityviewentitycollection/replaceall(_:).md)
  Replaces all entities in this collection with those from the given sequence.
### Subscripts
- [subscript(Int) -> Entity](realityviewentitycollection/subscript(_:).md)
  Accesses the element at the specified position.
### Type Aliases
- [RealityViewEntityCollection.Element](realityviewentitycollection/element.md)
  A type representing the sequence’s elements.
- [RealityViewEntityCollection.Index](realityviewentitycollection/index.md)
  A type that represents a position in the collection.
- [RealityViewEntityCollection.Indices](realityviewentitycollection/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [RealityViewEntityCollection.Iterator](realityviewentitycollection/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [RealityViewEntityCollection.SubSequence](realityviewentitycollection/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [Collection Implementations](realityviewentitycollection/collection-implementations.md)
- [EntityCollection Implementations](realityviewentitycollection/entitycollection-implementations.md)
- [Sequence Implementations](realityviewentitycollection/sequence-implementations.md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [EntityCollection](entitycollection.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct RealityView](realityview.md)
  A view that contains RealityKit content.
- [struct RealityViewContent](realityviewcontent.md)
  The content of a visionOS reality view.
- [struct RealityViewCameraContent](realityviewcameracontent.md)
  The content of a reality view that is displayed through a camera.
- [protocol RealityViewContentProtocol](realityviewcontentprotocol.md)
  A protocol representing the content of a reality view.
- [struct RealityViewDefaultPlaceholder](realityviewdefaultplaceholder.md)
  A view that represents the default placeholder for a RealityView.
- [protocol EntityCollection](entitycollection.md)
  An ordered, mutable collection of entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewentitycollection)*