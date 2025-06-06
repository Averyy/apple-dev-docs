# RealityRenderer.EntityCollection

**Framework**: RealityKit  
**Kind**: struct

A collection of entities in a [`RealityRenderer`](realityrenderer.md).

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
struct EntityCollection
```

#### Overview

This collection is used by [`entities`](realityrenderer/entities.md).

## Topics

### Instance Properties
- [var count: Int](realityrenderer/entitycollection/count.md)
  The number of elements in the collection.
- [var endIndex: Int](realityrenderer/entitycollection/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var startIndex: Int](realityrenderer/entitycollection/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func append<S>(contentsOf: S)](realityrenderer/entitycollection/append(contentsof:).md)
  Adds the specified sequence of entities to the end of this collection, in order.
- [func index(after: Int) -> Int](realityrenderer/entitycollection/index(after:).md)
  Returns the position immediately after the given index.
- [func insert<S>(contentsOf: S, beforeIndex: Int)](realityrenderer/entitycollection/insert(contentsof:beforeindex:).md)
  Adds the specified sequence of entities to this collection in order, directly before the entity at the given index.
- [func remove(Entity)](realityrenderer/entitycollection/remove(_:).md)
  Removes the entity from the collection.
- [func remove(at: Int)](realityrenderer/entitycollection/remove(at:).md)
  Removes the entity at the given index from this collection.
- [func removeAll()](realityrenderer/entitycollection/removeall.md)
  Removes all entities from this collection.
- [func replaceAll<S>(S)](realityrenderer/entitycollection/replaceall(_:).md)
  Replaces all entities in this collection with those from the given sequence.
### Subscripts
- [subscript(Int) -> Entity](realityrenderer/entitycollection/subscript(_:).md)
  Accesses the element at the specified position.
### Type Aliases
- [RealityRenderer.EntityCollection.Element](realityrenderer/entitycollection/element.md)
  A type representing the sequence’s elements.
- [RealityRenderer.EntityCollection.Index](realityrenderer/entitycollection/index.md)
  A type that represents a position in the collection.
- [RealityRenderer.EntityCollection.Indices](realityrenderer/entitycollection/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [RealityRenderer.EntityCollection.Iterator](realityrenderer/entitycollection/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [RealityRenderer.EntityCollection.SubSequence](realityrenderer/entitycollection/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [Collection Implementations](realityrenderer/entitycollection/collection-implementations.md)
- [EntityCollection Implementations](realityrenderer/entitycollection/entitycollection-implementations.md)
- [Sequence Implementations](realityrenderer/entitycollection/sequence-implementations.md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [EntityCollection](entitycollection.md)
- [Sendable](../Swift/Sendable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [class RealityRenderer](realityrenderer.md)
  A renderer that displays a RealityKit scene in an existing Metal workflow.
- [RealityRenderer.CameraSettings](realityrenderer/camerasettings-swift.struct.md)
  Settings for rendering with a camera.
- [RealityRenderer.CameraOutput](realityrenderer/cameraoutput.md)
  Output produced by rendering with a camera.
- [RealityRenderer.ImageBasedLight](realityrenderer/imagebasedlight.md)
  Describe the lighting properties for the scene.
- [RealityRenderer.MetalEventAction](realityrenderer/metaleventaction.md)
  The structure describing an event and value to be signaled or waited for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityrenderer/entitycollection)*