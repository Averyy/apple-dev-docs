# offsetBy(translation:)

**Framework**: RealityKit  
**Kind**: method

Creates a new shape resource by applying a translation.

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
@preconcurrency func offsetBy(translation: SIMD3<Float>) -> ShapeResource
```

#### Return Value

The transformed resource.

## Parameters

- `translation`: The translation to apply to the existing shape resource.

## See Also

- [func offsetBy(rotation: simd_quatf) -> ShapeResource](shaperesource/offsetby(rotation:).md)
  Creates a new shape resource by applying a rotation.
- [func offsetBy(rotation: simd_quatf, translation: SIMD3<Float>) -> ShapeResource](shaperesource/offsetby(rotation:translation:).md)
  Creates a new shape resource by applying a rotation and a translation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shaperesource/offsetby(translation:))*