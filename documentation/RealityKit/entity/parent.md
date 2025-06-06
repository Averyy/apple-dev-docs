# parent

**Framework**: RealityKit  
**Kind**: property

The parent entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var parent: Entity? { get }
```

#### Discussion

An entity has at most one parent entity. If an entity isn’t part of a hierarchy, or if it is a root entity, the [`parent`](hashierarchy/parent.md) property is `nil`.

Use the [`setParent(_:preservingWorldTransform:)`](hashierarchy/setparent(_:preservingworldtransform:).md) method to change an entity’s parent. Use the [`removeFromParent(preservingWorldTransform:)`](hashierarchy/removefromparent(preservingworldtransform:).md) method to remove the parent. These methods automatically update the corresponding [`children`](hashierarchy/children.md) collections of the new and old parent.

## See Also

- [func setParent(Entity?, preservingWorldTransform: Bool)](entity/setparent(_:preservingworldtransform:).md)
  Attaches the entity as a child to the specified entity.
- [func removeFromParent(preservingWorldTransform: Bool)](entity/removefromparent(preservingworldtransform:).md)
  Removes the entity from its current parent or from the scene if it is a root entity.
- [var children: Entity.ChildCollection](entity/children.md)
  The child entities that the entity manages.
- [func addChild(Entity, preservingWorldTransform: Bool)](entity/addchild(_:preservingworldtransform:).md)
  Adds the given entity to the collection of child entities.
- [func removeChild(Entity, preservingWorldTransform: Bool)](entity/removechild(_:preservingworldtransform:).md)
  Removes the given child from the entity.
- [Entity.ChildCollection](entity/childcollection.md)
  A collection of child entities.
- [protocol HasHierarchy](hashierarchy.md)
  An interface that provides access to a parent entity and child entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/parent)*