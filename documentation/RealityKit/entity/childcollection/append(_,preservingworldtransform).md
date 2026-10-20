# append(_:preservingWorldTransform:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Adds the specified entity as a child to this entity.

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
@preconcurrency func append(_ child: Entity, preservingWorldTransform: Bool = false)
```

## Parameters

- `child`: The child entity to add to the collection.
- `preservingWorldTransform`: `true` to preserve the world transform. `false` to preserve the relative transform. (Use `true` if the model should keep its effective location and size in the scene!)

## See Also

### Adding entities
- [func append<S>(contentsOf: S, preservingWorldTransforms: Bool)](./append%28contentsof,preservingworldtransforms%29-7g61.md)
  Adds the specified list of entity as children to this entity.
- [func append(contentsOf: [Entity], preservingWorldTransforms: Bool)](./append%28contentsof,preservingworldtransforms%29-7p4hd.md)
  Adds the specified list of entity as children to this entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/append(_:preservingworldtransform:))*