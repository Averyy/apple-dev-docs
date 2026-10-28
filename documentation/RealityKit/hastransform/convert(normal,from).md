# convert(normal:from:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Converts a normal vector from the local space of a reference entity to the local space of the entity on which you called this method.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func convert(normal: SIMD3<Float>, from referenceEntity: Entity?) -> SIMD3<Float>
```

## Return Value

The normal vector given in the local space of the entity.

## Parameters

- `normal`: A vector perpendicular to a surface at a point, specified relative to specified relative to `referenceEntity`.
- `referenceEntity`: The entity that defines a frame of reference. Set this to `nil` to indicate world space.

## See Also

### Converting values between coordinate spaces
- [func convert(position: SIMD3<Float>, from: Entity?) -> SIMD3<Float>](./convert%28position,from%29.md)
  Converts a position from the local space of a reference entity to the local space of the entity on which you called this method.
- [func convert(position: SIMD3<Float>, to: Entity?) -> SIMD3<Float>](./convert%28position,to%29.md)
  Converts a position from the local space of the entity on which you called this method to the local space of a reference entity.
- [func convert(direction: SIMD3<Float>, from: Entity?) -> SIMD3<Float>](./convert%28direction,from%29.md)
  Converts a direction vector from the local space of a reference entity to the local space of the entity on which you called this method.
- [func convert(direction: SIMD3<Float>, to: Entity?) -> SIMD3<Float>](./convert%28direction,to%29.md)
  Converts a direction vector from the local space of the entity on which you called this method to the local space of a reference entity.
- [func convert(normal: SIMD3<Float>, to: Entity?) -> SIMD3<Float>](./convert%28normal,to%29.md)
  Converts a normal vector from the local space of the entity on which you called this method to the local space of a reference entity.
- [func convert(transform: Transform, from: Entity?) -> Transform](./convert%28transform,from%29.md)
  Converts the scale, rotation, and position of a transform from the local space of a reference entity to the local space of the entity on which you called this method.
- [func convert(transform: Transform, to: Entity?) -> Transform](./convert%28transform,to%29.md)
  Converts the scale, rotation, and position of a transform from the local space of the entity on which you called this method to the local space of a reference entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/convert(normal:from:))*