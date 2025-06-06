# removeAll(keepCapacity:preservingWorldTransforms:)

**Framework**: RealityKit  
**Kind**: method

Removes all children from this entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func removeAll(keepCapacity: Bool = false, preservingWorldTransforms: Bool = false)
```

## Parameters

- `keepCapacity`:   to keep the memory reserved for storing the children.    to free the reserved memory.
- `preservingWorldTransforms`:   to preserve the world transform.   to   preserve the relative transform. (Use   if the   entities should keep its effective location and size in   the scene!)

## See Also

- [func remove(Entity, preservingWorldTransform: Bool)](entity/childcollection/remove(_:preservingworldtransform:).md)
  Removes the specified child from this entity.
- [func remove(at: Int, preservingWorldTransform: Bool)](entity/childcollection/remove(at:preservingworldtransform:).md)
  Removes the specified child from this entity.
- [func removeAll(preservingWorldTransforms: Bool)](entity/childcollection/removeall(preservingworldtransforms:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/removeall(keepcapacity:preservingworldtransforms:))*