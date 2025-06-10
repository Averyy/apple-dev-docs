# Scene.AnchorCollection

**Framework**: RealityKit  
**Kind**: struct

A collection of anchor entities.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency struct AnchorCollection
```

## Topics

### Iterating over the collection
- [func makeIterator() -> Scene.AnchorCollection.Iterator](scene/anchorcollection/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [Scene.AnchorCollection.Iterator](scene/anchorcollection/iterator.md)
  An iterator that presents the elements of the collection.
- [Scene.AnchorCollection.Element](scene/anchorcollection/element.md)
  The type of element traversed by the iterator.
### Accessing anchors
- [subscript(Int) -> any HasAnchoring](scene/anchorcollection/subscript(_:).md)
  Accesses the element at the specified position.
- [Scene.AnchorCollection.SubSequence](scene/anchorcollection/subsequence.md)
  A sequence that represents a contiguous subrange of the collection’s elements.
### Adding anchors
- [func append(any HasAnchoring)](scene/anchorcollection/append(_:).md)
  Adds a new anchor at the end of the collection.
- [func append(contentsOf: [any HasAnchoring])](scene/anchorcollection/append(contentsof:)-3bjib.md)
  Adds anchors from an array to the end of this collection.
- [func append<S>(contentsOf: S)](scene/anchorcollection/append(contentsof:)-4sf55.md)
  Adds anchors from a sequence to the end of this collection.
### Removing anchors
- [func remove(any HasAnchoring)](scene/anchorcollection/remove(_:).md)
  Removes the anchor at the specified position.
- [func remove(at: Int)](scene/anchorcollection/remove(at:).md)
  Removes and returns the anchor at the specified position.
- [func removeAll()](scene/anchorcollection/removeall.md)
  Removes all anchors from the collection.
- [func removeAll(keepCapacity: Bool)](scene/anchorcollection/removeall(keepcapacity:).md)
  Removes all anchors from the collection.
### Replacing anchors
- [func replaceAll([any HasAnchoring])](scene/anchorcollection/replaceall(_:)-tris.md)
  Replaces the existing anchor collection with a provided collection.
- [func replaceAll<S>(S)](scene/anchorcollection/replaceall(_:)-5t195.md)
  Replaces the existing anchor collection with a provided sequence.
### Manipulating indices
- [Scene.AnchorCollection.Index](scene/anchorcollection/index.md)
  A type that represents a position in the collection.
- [Scene.AnchorCollection.Indices](scene/anchorcollection/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [var startIndex: Int](scene/anchorcollection/startindex.md)
  The position of the first element in a nonempty collection.
- [var endIndex: Int](scene/anchorcollection/endindex.md)
  The position one greater than the last valid subscript argument.
- [func index(after: Int) -> Int](scene/anchorcollection/index(after:).md)
  Returns the position immediately after the given index.
### Describing the collection
- [var description: String](scene/anchorcollection/description.md)
  A textual representation of this instance.
### Instance Methods
- [func append(contentsOf:)](scene/anchorcollection/append(contentsof:).md)
  Adds anchors from an array to the end of this collection.
- [func replaceAll(_:)](scene/anchorcollection/replaceall(_:).md)
  Replaces the existing anchor collection with a provided collection.
### Default Implementations
- [CustomStringConvertible Implementations](scene/anchorcollection/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [class Scene](scene.md)
  A container that holds the collection of entities that an AR view renders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection)*