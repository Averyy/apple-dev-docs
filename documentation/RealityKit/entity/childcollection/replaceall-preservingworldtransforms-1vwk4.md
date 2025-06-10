# replaceAll(_:preservingWorldTransforms:)

**Framework**: RealityKit  
**Kind**: method

Removes all children from this entity and adds the specified list of entities as the new children.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func replaceAll<S>(_ children: S, preservingWorldTransforms: Bool = false) where S : Sequence, S.Element : Entity
```

## Parameters

- `children`: The list of the new children.
- `preservingWorldTransforms`:   to preserve the world transform.   to   preserve the relative transform. (Use   if the   entities should keep its effective location and size in   the scene!)

## See Also

- [func replaceAll([Entity], preservingWorldTransforms: Bool)](entity/childcollection/replaceall(_:preservingworldtransforms:)-4mgff.md)
  Removes all children from this entity and adds the specified list of entities as the new children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/replaceall(_:preservingworldtransforms:)-1vwk4)*