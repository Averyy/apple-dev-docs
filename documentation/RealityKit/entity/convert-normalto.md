# convert(normal:to:)

**Framework**: RealityKit  
**Kind**: method

Converts a normal vector from the local space of the entity on which you called this method to the local space of a reference entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func convert(normal: SIMD3<Float>, to referenceEntity: Entity?) -> SIMD3<Float>
```

#### Return Value

The normal vector specified relative to `referenceEntity`.

## Parameters

- `normal`: A vector perpendicular to a surface at a point, given in the   local space of the entity.
- `referenceEntity`: The entity that defines a frame of reference. Set   this to   to indicate world space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/convert(normal:to:))*