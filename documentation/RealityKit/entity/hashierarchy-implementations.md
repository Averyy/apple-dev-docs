# HasHierarchy Implementations

**Framework**: RealityKit

## Topics

### Instance Properties
- [var children: Entity.ChildCollection](entity/children.md)
  The child entities that the entity manages.
- [var parent: Entity?](entity/parent.md)
  The parent entity.
### Instance Methods
- [func addChild(Entity, preservingWorldTransform: Bool)](entity/addchild(_:preservingworldtransform:).md)
  Adds the given entity to the collection of child entities.
- [func removeChild(Entity, preservingWorldTransform: Bool)](entity/removechild(_:preservingworldtransform:).md)
  Removes the given child from the entity.
- [func removeFromParent(preservingWorldTransform: Bool)](entity/removefromparent(preservingworldtransform:).md)
  Removes the entity from its current parent or from the scene if it is a root entity.
- [func setParent(Entity?, preservingWorldTransform: Bool)](entity/setparent(_:preservingworldtransform:).md)
  Attaches the entity as a child to the specified entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/hashierarchy-implementations)*