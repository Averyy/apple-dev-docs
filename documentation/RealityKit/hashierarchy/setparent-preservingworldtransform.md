# setParent(_:preservingWorldTransform:)

**Framework**: RealityKit  
**Kind**: method

Attaches the entity as a child to the specified entity.

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
@preconcurrency func setParent(_ parent: Entity?, preservingWorldTransform: Bool = false)
```

#### Discussion

Attaching an entity to a new parent automatically detaches it from its old parent.

The [`children`](hashierarchy/children.md) collections of both the old and new parent are automatically updated as well.

> ❗ **Important**: On visionOS, only use `preservingWorldTransform` when moving an entity within the same `AnchorEntity`, `ImmersiveSpace` or SwiftUI `WindowGroup` hierarchy. Moving entities across these hierarchy boundaries while `preservingWorldTransform` is set to `true`, is not supported.

## Parameters

- `parent`: The new parent entity. Use   to detach the entity from its   current parent.
- `preservingWorldTransform`: A Boolean that you set to   to preserve   the entity’s world transform, or   to preserve its relative   transform. Use   when you want a model to keep its effective   location and size within a scene.

## See Also

- [var parent: Entity?](hashierarchy/parent.md)
  The parent entity.
- [func removeFromParent(preservingWorldTransform: Bool)](hashierarchy/removefromparent(preservingworldtransform:).md)
  Removes the entity from its current parent or from the scene if it is a root entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hashierarchy/setparent(_:preservingworldtransform:))*