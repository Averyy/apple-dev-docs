# Entity.ChildCollection

**Framework**: RealityKit  
**Kind**: struct

A collection of child entities.

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
@preconcurrency struct ChildCollection
```

## Topics

### Accessing collection members
- [subscript(Int) -> Entity](entity/childcollection/subscript(_:).md)
  Accesses the element at the specified position. (See `Collection.subscript`.)
### Adding entities
- [func append<S>(contentsOf: S, preservingWorldTransforms: Bool)](entity/childcollection/append(contentsof:preservingworldtransforms:)-7g61.md)
  Adds the specified list of entity as children to this entity.
- [func append(Entity, preservingWorldTransform: Bool)](entity/childcollection/append(_:preservingworldtransform:).md)
  Adds the specified entity as a child to this entity.
- [func append(contentsOf: [Entity], preservingWorldTransforms: Bool)](entity/childcollection/append(contentsof:preservingworldtransforms:)-7p4hd.md)
  Adds the specified list of entity as children to this entity.
### Removing entities
- [func remove(Entity, preservingWorldTransform: Bool)](entity/childcollection/remove(_:preservingworldtransform:).md)
  Removes the specified child from this entity.
- [func remove(at: Int, preservingWorldTransform: Bool)](entity/childcollection/remove(at:preservingworldtransform:).md)
  Removes the specified child from this entity.
- [func removeAll(preservingWorldTransforms: Bool)](entity/childcollection/removeall(preservingworldtransforms:).md)
- [func removeAll(keepCapacity: Bool, preservingWorldTransforms: Bool)](entity/childcollection/removeall(keepcapacity:preservingworldtransforms:).md)
  Removes all children from this entity.
### Replacing entities
- [func replaceAll([Entity], preservingWorldTransforms: Bool)](entity/childcollection/replaceall(_:preservingworldtransforms:)-4mgff.md)
  Removes all children from this entity and adds the specified list of entities as the new children.
- [func replaceAll<S>(S, preservingWorldTransforms: Bool)](entity/childcollection/replaceall(_:preservingworldtransforms:)-1vwk4.md)
  Removes all children from this entity and adds the specified list of entities as the new children.
### Iterating over collection of entities
- [Entity.ChildCollection.IndexingIterator](entity/childcollection/indexingiterator.md)
### Selecting entities
- [subscript(Int) -> Entity](entity/childcollection/subscript(_:).md)
  Accesses the element at the specified position. (See `Collection.subscript`.)
### Describing a collection
- [var description: String](entity/childcollection/description.md)
  A textual representation of this instance. (See `CustomStringConvertible`.)
### Manipulating indices
- [var startIndex: Int](entity/childcollection/startindex.md)
  The position of the first element in a nonempty collection. (See `Collection.startIndex`.)
- [var endIndex: Int](entity/childcollection/endindex.md)
  TThe collection’s “past the end” position—that is, the position one greater than the last valid subscript argument. (See `Collection.endIndex`.)
- [func index(after: Int) -> Int](entity/childcollection/index(after:).md)
  Returns the position immediately after the given index. (See `Collection.index`.)
### Instance Methods
- [func append(contentsOf:preservingWorldTransforms:)](entity/childcollection/append(contentsof:preservingworldtransforms:).md)
  Adds the specified list of entity as children to this entity.
- [func replaceAll(_:preservingWorldTransforms:)](entity/childcollection/replaceall(_:preservingworldtransforms:).md)
  Removes all children from this entity and adds the specified list of entities as the new children.
### Default Implementations
- [CustomStringConvertible Implementations](entity/childcollection/customstringconvertible-implementations.md)
- [EntityCollection Implementations](entity/childcollection/entitycollection-implementations.md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [EntityCollection](entitycollection.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [protocol HasHierarchy](hashierarchy.md)
  An interface that provides access to a parent entity and child entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection)*