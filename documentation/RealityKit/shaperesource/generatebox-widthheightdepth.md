# generateBox(width:height:depth:)

**Framework**: RealityKit  
**Kind**: method

Creates a box shape with the specified dimensions.

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
@preconcurrency static func generateBox(width: Float, height: Float, depth: Float) -> ShapeResource
```

#### Return Value

The new box centered at the local origin and aligned with the local axes.

#### Discussion

> **Note**: Collision shape extents that fall below 2mm are forced to be 2mm in size - this includes, entities with negative scale values.

## Parameters

- `width`: The extent of the box along the x-axis in meters.
- `height`: The extent of the box along the y-axis in meters.
- `depth`: The extent of the box along the z-axis in meters.

## See Also

- [static func generateBox(size: SIMD3<Float>) -> ShapeResource](shaperesource/generatebox(size:).md)
  Creates a box shape with the specified extent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shaperesource/generatebox(width:height:depth:))*