# generateBox(size:majorCornerRadius:minorCornerRadius:)

**Framework**: RealityKit  
**Kind**: method

Creates a box mesh from a vector of three scalar values that represent width, height, and depth, respectively, and radii for the corners.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static func generateBox(size: SIMD3<Float>, majorCornerRadius: Float = 0.2, minorCornerRadius: Float = 0.05) -> MeshResource
```

#### Discussion

The method centers the box at the entity’s origin and aligns the box’s faces with the coordinate system’s axes.

## Parameters

- `size`: The length of the box’s width, height, and depth, in meters,   along the x-, y-, and z-axis, respectively.
- `majorCornerRadius`: The radius of each corner’s circular arc,   in meters, orthogonal to the z-axis.
- `minorCornerRadius`: The radius of each corner’s circular arc,   in meters, orthogonal to the x-axis.

## See Also

- [static func generateBox(size: Float, cornerRadius: Float) -> MeshResource](meshresource/generatebox(size:cornerradius:)-8em0v.md)
  Creates a box mesh from a length for the box’s width, height, and depth, and a radius for the corners.
- [static func generateBox(size: SIMD3<Float>, cornerRadius: Float) -> MeshResource](meshresource/generatebox(size:cornerradius:)-2ovma.md)
  Creates a box mesh from a vector of three scalar values that represent width, height, and depth, respectively, and a radius for the corners.
- [static func generateBox(width: Float, height: Float, depth: Float, cornerRadius: Float, splitFaces: Bool) -> MeshResource](meshresource/generatebox(width:height:depth:cornerradius:splitfaces:).md)
  Creates a box mesh from a width, height, depth, a radius for the corners, and a Boolean option that splits faces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/generatebox(size:majorcornerradius:minorcornerradius:))*