# move(to:relativeTo:)

**Framework**: RealityKit  
**Kind**: method

Moves an entity instantly to a new location given by a 4x4 matrix.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func move(to transform: float4x4, relativeTo referenceEntity: Entity?)
```

## Parameters

- `transform`: A 4x4 matrix that indicates the new location.
- `referenceEntity`: The entity that defines a frame of reference. Set   this to   to indicate world space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/move(to:relativeto:)-6yugm)*