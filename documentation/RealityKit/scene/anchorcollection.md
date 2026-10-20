# Scene.AnchorCollection

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A collection of anchor entities.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency struct AnchorCollection
```

## Topics

### Iterating over the collection
- [func makeIterator() -> Scene.AnchorCollection.Iterator](./anchorcollection/makeiterator%28%29.md)
  Returns an iterator over the elements of the collection.
- [Scene.AnchorCollection.Iterator](./anchorcollection/iterator.md)
  An iterator that presents the elements of the collection.
- [Scene.AnchorCollection.Element](./anchorcollection/element.md)
  The type of element traversed by the iterator.
### Accessing anchors
- [subscript(Int) -> any HasAnchoring](./anchorcollection/subscript%28_%29.md)
  Accesses the element at the specified position.
- [Scene.AnchorCollection.SubSequence](./anchorcollection/subsequence.md)
  A sequence that represents a contiguous subrange of the collection’s elements.
### Adding anchors
- [func append(any HasAnchoring)](./anchorcollection/append%28_%29.md)
  Adds a new anchor at the end of the collection.
- [func append(contentsOf: [any HasAnchoring])](./anchorcollection/append%28contentsof%29-3bjib.md)
  Adds anchors from an array to the end of this collection.
- [func append<S>(contentsOf: S)](./anchorcollection/append%28contentsof%29-4sf55.md)
  Adds anchors from a sequence to the end of this collection.
### Removing anchors
- [func remove(any HasAnchoring)](./anchorcollection/remove%28_%29.md)
  Removes the anchor at the specified position.
- [func remove(at: Int)](./anchorcollection/remove%28at%29.md)
  Removes and returns the anchor at the specified position.
- [func removeAll()](./anchorcollection/removeall%28%29.md)
  Removes all anchors from the collection.
- [func removeAll(keepCapacity: Bool)](./anchorcollection/removeall%28keepcapacity%29.md)
  Removes all anchors from the collection.
### Replacing anchors
- [func replaceAll([any HasAnchoring])](./anchorcollection/replaceall%28_%29-tris.md)
  Replaces the existing anchor collection with a provided collection.
- [func replaceAll<S>(S)](./anchorcollection/replaceall%28_%29-5t195.md)
  Replaces the existing anchor collection with a provided sequence.
### Manipulating indices
- [Scene.AnchorCollection.Index](./anchorcollection/index.md)
  A type that represents a position in the collection.
- [var startIndex: Int](./anchorcollection/startindex.md)
  The position of the first element in a nonempty collection.
- [var endIndex: Int](./anchorcollection/endindex.md)
  The position one greater than the last valid subscript argument.
- [func index(after: Int) -> Int](./anchorcollection/index%28after%29.md)
  Returns the position immediately after the given index.
### Describing the collection
- [var description: String](./anchorcollection/description.md)
  A textual representation of this instance.
### Instance Methods
- [func append(contentsOf:)](./anchorcollection/append%28contentsof%29.md)
  Adds anchors from an array to the end of this collection.
- [func replaceAll(_:)](./anchorcollection/replaceall%28_%29.md)
  Replaces the existing anchor collection with a provided collection.
### Type Aliases
- [Scene.AnchorCollection.Indices](./anchorcollection/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
### Default Implementations
- [CustomStringConvertible Implementations](./anchorcollection/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Collection](../../Swift/collection.md)
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Scene management
- [class Scene](../scene.md)
  A container that holds the collection of entities that an AR view renders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection)*