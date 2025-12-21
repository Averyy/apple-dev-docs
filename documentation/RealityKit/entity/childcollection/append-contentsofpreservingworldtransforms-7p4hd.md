# append(contentsOf:preservingWorldTransforms:)

**Framework**: RealityKit  
**Kind**: method

Adds the specified list of entity as children to this entity.

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
@preconcurrency func append(contentsOf array: [Entity], preservingWorldTransforms: Bool = false)
```

## Parameters

- `array`: The child entities to add to the collection.
- `preservingWorldTransforms`:   to preserve the world transform.   to   preserve the relative transform. (Use   if the   entities should keep its effective location and size in   the scene!)

## See Also

- [func append<S>(contentsOf: S, preservingWorldTransforms: Bool)](entity/childcollection/append(contentsof:preservingworldtransforms:)-7g61.md)
  Adds the specified list of entity as children to this entity.
- [func append(Entity, preservingWorldTransform: Bool)](entity/childcollection/append(_:preservingworldtransform:).md)
  Adds the specified entity as a child to this entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/append(contentsof:preservingworldtransforms:)-7p4hd)*