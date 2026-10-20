# offsetBy(rotation:translation:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Creates a new shape resource by applying a rotation and a translation.

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
@preconcurrency func offsetBy(rotation: simd_quatf = simd_quatf(ix: 0, iy: 0, iz: 0, r: 1), translation: SIMD3<Float> = SIMD3<Float>()) -> ShapeResource
```

#### Return Value

The transformed resource.

## Parameters

- `rotation`: The rotation to apply to the existing shape resource.
- `translation`: The translation to apply to the existing shape resource.

## See Also

### Transforming a shape
- [func offsetBy(rotation: simd_quatf) -> ShapeResource](./offsetby%28rotation%29.md)
  Creates a new shape resource by applying a rotation.
- [func offsetBy(translation: SIMD3<Float>) -> ShapeResource](./offsetby%28translation%29.md)
  Creates a new shape resource by applying a translation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shaperesource/offsetby(rotation:translation:))*