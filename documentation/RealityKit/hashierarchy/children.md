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

- [func addChild(Entity, preservingWorldTransform: Bool)](hashierarchy/addchild(_:preservingworldtransform:).md)
  Adds the given entity to the collection of child entities.
- [func removeChild(Entity, preservingWorldTransform: Bool)](hashierarchy/removechild(_:preservingworldtransform:).md)
  Removes the given child from the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hashierarchy/children)*