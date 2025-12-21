# removeFromParent(preservingWorldTransform:)

**Framework**: RealityKit  
**Kind**: method

Removes the entity from its current parent or from the scene if it is a root entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
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

- [var parent: Entity?](hashierarchy/parent.md)
  The parent entity.
- [func setParent(Entity?, preservingWorldTransform: Bool)](hashierarchy/setparent(_:preservingworldtransform:).md)
  Attaches the entity as a child to the specified entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hashierarchy/removefromparent(preservingworldtransform:))*