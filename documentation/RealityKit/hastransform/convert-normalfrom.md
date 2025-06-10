# convert(normal:from:)

**Framework**: RealityKit  
**Kind**: method

Converts a normal vector from the local space of a reference entity to the local space of the entity on which you called this method.

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
@preconcurrency func convert(normal: SIMD3<Float>, from referenceEntity: Entity?) -> SIMD3<Float>
```

#### Return Value

The normal vector given in the local space of the entity.

## Parameters

- `normal`: A vector perpendicular to a surface at a point, specified   relative to specified relative to  .
- `referenceEntity`: The entity that defines a frame of reference. Set   this to   to indicate world space.

## See Also

- [func convert(position: SIMD3<Float>, from: Entity?) -> SIMD3<Float>](hastransform/convert(position:from:).md)
  Converts a position from the local space of a reference entity to the local space of the entity on which you called this method.
- [func convert(position: SIMD3<Float>, to: Entity?) -> SIMD3<Float>](hastransform/convert(position:to:).md)
  Converts a position from the local space of the entity on which you called this method to the local space of a reference entity.
- [func convert(direction: SIMD3<Float>, from: Entity?) -> SIMD3<Float>](hastransform/convert(direction:from:).md)
  Converts a direction vector from the local space of a reference entity to the local space of the entity on which you called this method.
- [func convert(direction: SIMD3<Float>, to: Entity?) -> SIMD3<Float>](hastransform/convert(direction:to:).md)
  Converts a direction vector from the local space of the entity on which you called this method to the local space of a reference entity.
- [func convert(normal: SIMD3<Float>, to: Entity?) -> SIMD3<Float>](hastransform/convert(normal:to:).md)
  Converts a normal vector from the local space of the entity on which you called this method to the local space of a reference entity.
- [func convert(transform: Transform, from: Entity?) -> Transform](hastransform/convert(transform:from:).md)
  Converts the scale, rotation, and position of a transform from the local space of a reference entity to the local space of the entity on which you called this method.
- [func convert(transform: Transform, to: Entity?) -> Transform](hastransform/convert(transform:to:).md)
  Converts the scale, rotation, and position of a transform from the local space of the entity on which you called this method to the local space of a reference entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/convert(normal:from:))*