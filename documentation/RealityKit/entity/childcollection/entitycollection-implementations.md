# EntityCollection Implementations

**Framework**: RealityKit

## Topics

### Instance Methods
- [func append(Entity)](entity/childcollection/append(_:).md)
  Adds the specified entity to the end of this collection.
- [func append<S>(contentsOf: S)](entity/childcollection/append(contentsof:).md)
  Adds the specified list of entity as children to this entity.
- [func insert(Entity, beforeIndex: Int)](entity/childcollection/insert(_:beforeindex:).md)
  Adds the specified entity to this collection directly before the entity at the given index. If the entity is already located before the index, the collection will not change.
- [func insert<S>(contentsOf: S, beforeIndex: Int)](entity/childcollection/insert(contentsof:beforeindex:).md)
  Adds the specified sequence of entities to this collection in order, directly before the entity at the given index.
- [func remove(Entity)](entity/childcollection/remove(_:).md)
  Removes the specified child from this entity.
- [func remove(at: Int)](entity/childcollection/remove(at:).md)
  Removes the specified child from this entity.
- [func removeAll()](entity/childcollection/removeall.md)
  Removes all children from this entity.
- [func removeAll(where: (Entity) throws -> Bool) rethrows](entity/childcollection/removeall(where:).md)
  Removes all entities from this collection that satisfy the given predicate.
- [func replaceAll<S>(S)](entity/childcollection/replaceall(_:).md)
  Removes all children from this entity and adds the specified list of entities as the new children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/entitycollection-implementations)*