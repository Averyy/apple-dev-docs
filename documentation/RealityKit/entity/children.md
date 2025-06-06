# children

**Framework**: RealityKit  
**Kind**: property

The child entities that the entity manages.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var children: Entity.ChildCollection { get set }
```

#### Discussion

An entity can have any number of child entities.

Use the [`addChild(_:preservingWorldTransform:)`](hashierarchy/addchild(_:preservingworldtransform:).md) method to add a child to an entity. Use the [`removeChild(_:preservingWorldTransform:)`](hashierarchy/removechild(_:preservingworldtransform:).md) method to remove one from an entity. These methods automatically update the [`parent`](hashierarchy/parent.md) properties of the child entities.

## See Also

- [var parent: Entity?](entity/parent.md)
  The parent entity.
- [func setParent(Entity?, preservingWorldTransform: Bool)](entity/setparent(_:preservingworldtransform:).md)
  Attaches the entity as a child to the specified entity.
- [func removeFromParent(preservingWorldTransform: Bool)](entity/removefromparent(preservingworldtransform:).md)
  Removes the entity from its current parent or from the scene if it is a root entity.
- [func addChild(Entity, preservingWorldTransform: Bool)](entity/addchild(_:preservingworldtransform:).md)
  Adds the given entity to the collection of child entities.
- [func removeChild(Entity, preservingWorldTransform: Bool)](entity/removechild(_:preservingworldtransform:).md)
  Removes the given child from the entity.
- [Entity.ChildCollection](entity/childcollection.md)
  A collection of child entities.
- [protocol HasHierarchy](hashierarchy.md)
  An interface that provides access to a parent entity and child entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/children)*