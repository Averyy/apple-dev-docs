# remove(at:preservingWorldTransform:)

**Framework**: RealityKit  
**Kind**: method

Removes the specified child from this entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func remove(at index: Int, preservingWorldTransform: Bool = false)
```

#### Discussion

> **Note**: This may modify the order of the `ChildCollection`.

This may modify the order of the `ChildCollection`.

## Parameters

- `index`: The index of the child entity to remove from the collection.
- `preservingWorldTransform`:   to preserve the world transform.   to   preserve the relative transform. (Use   if the   entities should keep its effective location and size in   the scene!)

## See Also

- [func remove(Entity, preservingWorldTransform: Bool)](entity/childcollection/remove(_:preservingworldtransform:).md)
  Removes the specified child from this entity.
- [func removeAll(preservingWorldTransforms: Bool)](entity/childcollection/removeall(preservingworldtransforms:).md)
- [func removeAll(keepCapacity: Bool, preservingWorldTransforms: Bool)](entity/childcollection/removeall(keepcapacity:preservingworldtransforms:).md)
  Removes all children from this entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/remove(at:preservingworldtransform:))*