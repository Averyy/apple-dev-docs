# transformMatrix(relativeTo:)

**Framework**: RealityKit  
**Kind**: method

Gets the 4 x 4 transform matrix of an entity relative to the given entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func transformMatrix(relativeTo referenceEntity: Entity?) -> float4x4
```

#### Return Value

The transform of the entity relative to `referenceEntity`.

## Parameters

- `referenceEntity`: The entity that defines a frame of reference. Set   this to   to indicate world space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/transformmatrix(relativeto:)-7yhub)*