# scale(relativeTo:)

**Framework**: RealityKit  
**Kind**: method

Gets the scale of an entity relative to the given entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func scale(relativeTo referenceEntity: Entity?) -> SIMD3<Float>
```

## Parameters

- `referenceEntity`: The entity that defines a frame of reference. Set   this to   to indicate world space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/scale(relativeto:))*