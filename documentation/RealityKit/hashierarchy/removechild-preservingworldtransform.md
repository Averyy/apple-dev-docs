# removeChild(_:preservingWorldTransform:)

**Framework**: RealityKit  
**Kind**: method

Removes the given child from the entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
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

- [var children: Entity.ChildCollection](hashierarchy/children.md)
  The child entities that the entity manages.
- [func addChild(Entity, preservingWorldTransform: Bool)](hashierarchy/addchild(_:preservingworldtransform:).md)
  Adds the given entity to the collection of child entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hashierarchy/removechild(_:preservingworldtransform:))*