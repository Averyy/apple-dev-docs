# addChild(_:preservingWorldTransform:)

**Framework**: RealityKit  
**Kind**: method

Adds the given entity to the collection of child entities.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func addChild(_ entity: Entity, preservingWorldTransform: Bool = false)
```

#### Discussion

See the [`HasHierarchy`](hashierarchy.md) protocol’s definition of [`addChild(_:preservingWorldTransform:)`](hashierarchy/addchild(_:preservingworldtransform:).md) for more information.

## Parameters

- `entity`: 
- `preservingWorldTransform`: A Boolean that you set to   to preserve   the entity’s world transform, or   to preserve its relative   transform. Use   when you want a model to keep its effective   location and size within a scene.

## See Also

- [var children: Entity.ChildCollection](hashierarchy/children.md)
  The child entities that the entity manages.
- [func removeChild(Entity, preservingWorldTransform: Bool)](hashierarchy/removechild(_:preservingworldtransform:).md)
  Removes the given child from the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hashierarchy/addchild(_:preservingworldtransform:))*