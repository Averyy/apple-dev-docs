# removeAll(keepCapacity:preservingWorldTransforms:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Removes all children from this entity.

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
@preconcurrency func removeAll(keepCapacity: Bool = false, preservingWorldTransforms: Bool = false)
```

## Parameters

- `keepCapacity`: `true` to keep the memory reserved for storing the children. `false` to free the reserved memory.
- `preservingWorldTransforms`: `true` to preserve the world transform. `false` to preserve the relative transform. (Use `true` if the entities should keep its effective location and size in the scene!)

## See Also

### Removing entities
- [func remove(Entity, preservingWorldTransform: Bool)](./remove%28_,preservingworldtransform%29.md)
  Removes the specified child from this entity.
- [func remove(at: Int, preservingWorldTransform: Bool)](./remove%28at,preservingworldtransform%29.md)
  Removes the specified child from this entity.
- [func removeAll(preservingWorldTransforms: Bool)](./removeall%28preservingworldtransforms%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/removeall(keepcapacity:preservingworldtransforms:))*