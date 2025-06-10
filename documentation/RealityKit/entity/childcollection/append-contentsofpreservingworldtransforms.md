# append(contentsOf:preservingWorldTransforms:)

**Framework**: RealityKit  
**Kind**: method

Adds the specified list of entity as children to this entity.

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
@preconcurrency func append(contentsOf array: [Entity], preservingWorldTransforms: Bool = false)
```

## Parameters

- `array`: The child entities to add to the collection.
- `preservingWorldTransforms`:   to preserve the world transform.   to   preserve the relative transform. (Use   if the   entities should keep its effective location and size in   the scene!)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/append(contentsof:preservingworldtransforms:))*