# removeChild(_:preservingWorldTransform:)

**Framework**: RealityKit  
**Kind**: method

Removes the given child from the entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func removeChild(_ entity: Entity, preservingWorldTransform: Bool = false)
```

#### Discussion

See the [`HasHierarchy`](hashierarchy.md) protocol’s definition of [`removeChild(_:preservingWorldTransform:)`](hashierarchy/removechild(_:preservingworldtransform:).md) for more information.

## Parameters

- `entity`: 
- `preservingWorldTransform`: A Boolean that you set to   to preserve   the entity’s world transform, or   to preserve its relative   transform. Use   when you want a model to keep its effective   location and size within a scene.

## See Also

- [var parent: Entity?](entity/parent.md)
  The parent entity.
- [func setParent(Entity?, preservingWorldTransform: Bool)](entity/setparent(_:preservingworldtransform:).md)
  Attaches the entity as a child to the specified entity.
- [func removeFromParent(preservingWorldTransform: Bool)](entity/removefromparent(preservingworldtransform:).md)
  Removes the entity from its current parent or from the scene if it is a root entity.
- [var children: Entity.ChildCollection](entity/children.md)
  The child entities that the entity manages.
- [func addChild(Entity, preservingWorldTransform: Bool)](entity/addchild(_:preservingworldtransform:).md)
  Adds the given entity to the collection of child entities.
- [Entity.ChildCollection](entity/childcollection.md)
  A collection of child entities.
- [protocol HasHierarchy](hashierarchy.md)
  An interface that provides access to a parent entity and child entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/removechild(_:preservingworldtransform:))*