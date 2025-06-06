# EntityCollection

**Framework**: RealityKit  
**Kind**: protocol

An ordered, mutable collection of entities.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
protocol EntityCollection : Collection where Self.Element == Entity, Self.Index == Int
```

## Topics

### Instance Methods
- [func append(Entity)](entitycollection/append(_:).md)
  Adds the specified entity to the end of this collection.
- [func append<S>(contentsOf: S)](entitycollection/append(contentsof:).md)
  Adds the specified sequence of entities to the end of this collection, in order.
- [func insert(Entity, beforeIndex: Int)](entitycollection/insert(_:beforeindex:).md)
  Adds the specified entity to this collection directly before the entity at the given index. If the entity is already located before the index, the collection will not change.
- [func insert<S>(contentsOf: S, beforeIndex: Int)](entitycollection/insert(contentsof:beforeindex:).md)
  Adds the specified sequence of entities to this collection in order, directly before the entity at the given index.
- [func remove(Entity)](entitycollection/remove(_:).md)
  Removes the entity from the collection.
- [func remove(at: Int)](entitycollection/remove(at:).md)
  Removes the entity at the given index from this collection.
- [func removeAll()](entitycollection/removeall.md)
  Removes all entities from this collection.
- [func removeAll(where: (Entity) throws -> Bool) rethrows](entitycollection/removeall(where:).md)
  Removes all entities from this collection that satisfy the given predicate.
- [func replaceAll<S>(S)](entitycollection/replaceall(_:).md)
  Replaces all entities in this collection with those from the given sequence.

## Relationships

### Inherits From
- [Collection](../Swift/Collection.md)
- [Sequence](../Swift/Sequence.md)
### Conforming Types
- [Entity.ChildCollection](entity/childcollection.md)
- [RealityRenderer.EntityCollection](realityrenderer/entitycollection.md)
- [RealityViewEntityCollection](realityviewentitycollection.md)

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
- [struct RealityViewEntityCollection](realityviewentitycollection.md)
  A collection of entities in a RealityView.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entitycollection)*