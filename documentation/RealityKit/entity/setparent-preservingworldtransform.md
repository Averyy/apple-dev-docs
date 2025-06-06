# setParent(_:preservingWorldTransform:)

**Framework**: RealityKit  
**Kind**: method

Attaches the entity as a child to the specified entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func setParent(_ parent: Entity?, preservingWorldTransform: Bool = false)
```

#### Discussion

Attaching an entity to a new parent automatically detaches it from its old parent.

The [`children`](hashierarchy/children.md) collections of both the old and new parent are automatically updated as well.

> ❗ **Important**: On visionOS, only use `preservingWorldTransform` when moving an entity within the same `AnchorEntity`, `ImmersiveSpace` or SwiftUI `WindowGroup` hierarchy. Moving entities across these hierarchy boundaries while `preservingWorldTransform` is set to `true`, is not supported.

On visionOS, only use `preservingWorldTransform` when moving an entity within the same `AnchorEntity`, `ImmersiveSpace` or SwiftUI `WindowGroup` hierarchy. Moving entities across these hierarchy boundaries while `preservingWorldTransform` is set to `true`, is not supported.

## Parameters

- `parent`: The new parent entity. Use   to detach the entity from its   current parent.
- `preservingWorldTransform`: A Boolean that you set to   to preserve   the entity’s world transform, or   to preserve its relative   transform. Use   when you want a model to keep its effective   location and size within a scene.

## See Also

- [var parent: Entity?](entity/parent.md)
  The parent entity.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/setparent(_:preservingworldtransform:))*