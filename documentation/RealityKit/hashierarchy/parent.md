# parent

**Framework**: RealityKit  
**Kind**: property

The parent entity.

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
@preconcurrency var parent: Entity? { get }
```

#### Discussion

An entity has at most one parent entity. If an entity isn’t part of a hierarchy, or if it is a root entity, the [`parent`](hashierarchy/parent.md) property is `nil`.

Use the [`setParent(_:preservingWorldTransform:)`](hashierarchy/setparent(_:preservingworldtransform:).md) method to change an entity’s parent. Use the [`removeFromParent(preservingWorldTransform:)`](hashierarchy/removefromparent(preservingworldtransform:).md) method to remove the parent. These methods automatically update the corresponding [`children`](hashierarchy/children.md) collections of the new and old parent.

## See Also

- [func setParent(Entity?, preservingWorldTransform: Bool)](hashierarchy/setparent(_:preservingworldtransform:).md)
  Attaches the entity as a child to the specified entity.
- [func removeFromParent(preservingWorldTransform: Bool)](hashierarchy/removefromparent(preservingworldtransform:).md)
  Removes the entity from its current parent or from the scene if it is a root entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hashierarchy/parent)*