# append(contentsOf:)

**Framework**: RealityKit  
**Kind**: method

Adds the specified list of entity as children to this entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func append<S>(contentsOf sequence: S) where S : Sequence, S.Element : Entity
```

## Parameters

- `sequence`: The child entities to add to the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/append(contentsof:)-7ndu7)*