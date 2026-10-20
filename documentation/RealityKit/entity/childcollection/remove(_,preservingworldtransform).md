# remove(_:preservingWorldTransform:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified child from this entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func remove(_ child: Entity, preservingWorldTransform: Bool = false)
```

#### Discussion

> **Note**: This may modify the order of the `ChildCollection`.

## Parameters

- `child`: The child entity to remove from the collection.
- `preservingWorldTransform`: `true` to preserve the world transform. `false` to preserve the relative transform. (Use `true` if the entities should keep its effective location and size in the scene!)

## See Also

### Removing entities
- [func remove(at: Int, preservingWorldTransform: Bool)](./remove%28at,preservingworldtransform%29.md)
  Removes the specified child from this entity.
- [func removeAll(preservingWorldTransforms: Bool)](./removeall%28preservingworldtransforms%29.md)
- [func removeAll(keepCapacity: Bool, preservingWorldTransforms: Bool)](./removeall%28keepcapacity,preservingworldtransforms%29.md)
  Removes all children from this entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/remove(_:preservingworldtransform:))*