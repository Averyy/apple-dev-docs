# generateBox(size:)

**Framework**: RealityKit  
**Kind**: method

Creates a box shape with the specified extent.

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
@preconcurrency static func generateBox(size: SIMD3<Float>) -> ShapeResource
```

#### Return Value

The new box centered at the local origin and aligned with the local axes.

#### Discussion

> **Note**: Collision shape extents that fall below 2mm are forced to be 2mm in size - this includes, entities with negative scale values.

## Parameters

- `size`: The box extent in meters along the local axes.

## See Also

- [static func generateBox(width: Float, height: Float, depth: Float) -> ShapeResource](shaperesource/generatebox(width:height:depth:).md)
  Creates a box shape with the specified dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shaperesource/generatebox(size:))*