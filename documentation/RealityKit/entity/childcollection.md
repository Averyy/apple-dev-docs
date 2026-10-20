# Entity.ChildCollection

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A collection of child entities.

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
@preconcurrency struct ChildCollection
```

## Topics

### Accessing collection members
- [subscript(Int) -> Entity](./childcollection/subscript%28_%29.md)
  Accesses the element at the specified position. (See `Collection.subscript`.)
### Adding entities
- [func append<S>(contentsOf: S, preservingWorldTransforms: Bool)](./childcollection/append%28contentsof,preservingworldtransforms%29-7g61.md)
  Adds the specified list of entity as children to this entity.
- [func append(Entity, preservingWorldTransform: Bool)](./childcollection/append%28_,preservingworldtransform%29.md)
  Adds the specified entity as a child to this entity.
- [func append(contentsOf: [Entity], preservingWorldTransforms: Bool)](./childcollection/append%28contentsof,preservingworldtransforms%29-7p4hd.md)
  Adds the specified list of entity as children to this entity.
### Removing entities
- [func remove(Entity, preservingWorldTransform: Bool)](./childcollection/remove%28_,preservingworldtransform%29.md)
  Removes the specified child from this entity.
- [func remove(at: Int, preservingWorldTransform: Bool)](./childcollection/remove%28at,preservingworldtransform%29.md)
  Removes the specified child from this entity.
- [func removeAll(preservingWorldTransforms: Bool)](./childcollection/removeall%28preservingworldtransforms%29.md)
- [func removeAll(keepCapacity: Bool, preservingWorldTransforms: Bool)](./childcollection/removeall%28keepcapacity,preservingworldtransforms%29.md)
  Removes all children from this entity.
### Replacing entities
- [func replaceAll([Entity], preservingWorldTransforms: Bool)](./childcollection/replaceall%28_,preservingworldtransforms%29-4mgff.md)
  Removes all children from this entity and adds the specified list of entities as the new children.
- [func replaceAll<S>(S, preservingWorldTransforms: Bool)](./childcollection/replaceall%28_,preservingworldtransforms%29-1vwk4.md)
  Removes all children from this entity and adds the specified list of entities as the new children.
### Iterating over collection of entities
- [Entity.ChildCollection.IndexingIterator](./childcollection/indexingiterator.md)
### Describing a collection
- [var description: String](./childcollection/description.md)
  A textual representation of this instance. (See `CustomStringConvertible`.)
### Manipulating indices
- [var startIndex: Int](./childcollection/startindex.md)
  The position of the first element in a nonempty collection. (See `Collection.startIndex`.)
- [var endIndex: Int](./childcollection/endindex.md)
  TThe collection’s “past the end” position—that is, the position one greater than the last valid subscript argument. (See `Collection.endIndex`.)
- [func index(after: Int) -> Int](./childcollection/index%28after%29.md)
  Returns the position immediately after the given index. (See `Collection.index`.)
### Instance Methods
- [func append(contentsOf:preservingWorldTransforms:)](./childcollection/append%28contentsof,preservingworldtransforms%29.md)
  Adds the specified list of entity as children to this entity.
- [func replaceAll(_:preservingWorldTransforms:)](./childcollection/replaceall%28_,preservingworldtransforms%29.md)
  Removes all children from this entity and adds the specified list of entities as the new children.
### Default Implementations
- [CustomStringConvertible Implementations](./childcollection/customstringconvertible-implementations.md)
- [EntityCollection Implementations](./childcollection/entitycollection-implementations.md)

## Relationships

### Conforms To
- [Collection](../../Swift/collection.md)
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [EntityCollection](../entitycollection.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Relating entities
- [var parameters: Entity.ParameterSet](./parameters.md)
  Represents a reference to the parameters for a particular entity.
- [protocol HasHierarchy](../hashierarchy.md)
  An interface that provides access to a parent entity and child entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection)*