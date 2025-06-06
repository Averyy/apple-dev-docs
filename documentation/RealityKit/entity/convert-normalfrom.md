# convert(normal:from:)

**Framework**: RealityKit  
**Kind**: method

Converts a normal vector from the local space of a reference entity to the local space of the entity on which you called this method.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func convert(normal: SIMD3<Float>, from referenceEntity: Entity?) -> SIMD3<Float>
```

#### Return Value

The normal vector given in the local space of the entity.

## Parameters

- `normal`: A vector perpendicular to a surface at a point, specified   relative to specified relative to  .
- `referenceEntity`: The entity that defines a frame of reference. Set   this to   to indicate world space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/convert(normal:from:))*