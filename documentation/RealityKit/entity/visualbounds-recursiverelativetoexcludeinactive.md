# visualBounds(recursive:relativeTo:excludeInactive:)

**Framework**: RealityKit  
**Kind**: method

Computes a bounding box for the entity in the specified space, optionally including child entities.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func visualBounds(recursive: Bool = true, relativeTo referenceEntity: Entity?, excludeInactive: Bool = false) -> BoundingBox
```

#### Return Value

The bounding box.

#### Discussion

The method has complexity `O(n)`, where `n` is the number of entities in the hierarchy.

## Parameters

- `recursive`: A Boolean that you set to   to incorporate the bounds   of all descendants.
- `referenceEntity`: An entity that defines a frame of reference. Set to    to indicate world space.
- `excludeInactive`: A Boolean that you set to   to exclude inactive   entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/visualbounds(recursive:relativeto:excludeinactive:))*