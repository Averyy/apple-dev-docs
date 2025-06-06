# append(contentsOf:preservingWorldTransforms:)

**Framework**: RealityKit  
**Kind**: method

Moves all `children` to be children of this entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func append(contentsOf children: Entity.ChildCollection, preservingWorldTransforms: Bool = false)
```

## Parameters

- `children`: The child entities to add to the collection.
- `preservingWorldTransforms`:   to preserve the world transform.   to   preserve the relative transform. (Use   if the   entities should keep its effective location and size in   the scene!)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/append(contentsof:preservingworldtransforms:)-4cjpz)*