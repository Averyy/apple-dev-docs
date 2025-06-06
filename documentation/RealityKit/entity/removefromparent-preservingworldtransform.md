# removeFromParent(preservingWorldTransform:)

**Framework**: RealityKit  
**Kind**: method

Removes the entity from its current parent or from the scene if it is a root entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func removeFromParent(preservingWorldTransform: Bool = false)
```

#### Discussion

This method behaves like the [`setParent(_:preservingWorldTransform:)`](hashierarchy/setparent(_:preservingworldtransform:).md) method with a value of `nil` for the `parent` parameter, except that method has no effect on root entities. A root entity is one that is stored in a scene’s [`anchors`](scene/anchors.md) collection.

The [`children`](hashierarchy/children.md) collections of any modified parent entities are automatically updated as well.

## Parameters

- `preservingWorldTransform`: A Boolean that you set to   to preserve   the entity’s world transform, or   to preserve its relative   transform. Use   when you want a model to keep its effective   location and size within a scene.

## See Also

- [var parent: Entity?](entity/parent.md)
  The parent entity.
- [func setParent(Entity?, preservingWorldTransform: Bool)](entity/setparent(_:preservingworldtransform:).md)
  Attaches the entity as a child to the specified entity.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/removefromparent(preservingworldtransform:))*