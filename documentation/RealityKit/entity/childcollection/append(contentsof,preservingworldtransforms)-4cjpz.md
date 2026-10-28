# append(contentsOf:preservingWorldTransforms:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Moves all `children` to be children of this entity.

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
@preconcurrency func append(contentsOf children: Entity.ChildCollection, preservingWorldTransforms: Bool = false)
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func append(contentsOf array: [Entity], preservingWorldTransforms: Bool = false)
```

```swift
@MainActor
@preconcurrency func append<S>(contentsOf sequence: S, preservingWorldTransforms: Bool = false) where S : Sequence, S.Element : Entity
```

## Parameters

- `children`: The child entities to add to the collection.
- `preservingWorldTransforms`: `true` to preserve the world transform. `false` to preserve the relative transform. (Use `true` if the entities should keep its effective location and size in the scene!)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/append(contentsof:preservingworldtransforms:)-4cjpz)*