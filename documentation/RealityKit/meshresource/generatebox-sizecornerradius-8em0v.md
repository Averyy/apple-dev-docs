# generateBox(size:cornerRadius:)

**Framework**: RealityKit  
**Kind**: method

Creates a box mesh from a length for the box’s width, height, and depth, and a radius for the corners.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency static func generateBox(size: Float, cornerRadius: Float = 0) -> MeshResource
```

#### Discussion

The method centers the box at the entity’s origin and aligns the box’s faces with the coordinate system’s axes.

> **Note**: The method clamps `cornerRadius` so that it doesn’t exceed half the length of the box’s smallest dimension.

## Parameters

- `size`: The length of the box’s width, height, and depth, in meters.
- `cornerRadius`: The radius of each corner’s circular arc, in meters.   Values for   can be, at most, equal to  .   For example, if the box’s dimensions are   x   x  ,   the corner radius needs to be in the range  .

## See Also

- [static func generateBox(size: SIMD3<Float>, cornerRadius: Float) -> MeshResource](meshresource/generatebox(size:cornerradius:)-2ovma.md)
  Creates a box mesh from a vector of three scalar values that represent width, height, and depth, respectively, and a radius for the corners.
- [static func generateBox(width: Float, height: Float, depth: Float, cornerRadius: Float, splitFaces: Bool) -> MeshResource](meshresource/generatebox(width:height:depth:cornerradius:splitfaces:).md)
  Creates a box mesh from a width, height, depth, a radius for the corners, and a Boolean option that splits faces.
- [static func generateBox(size: SIMD3<Float>, majorCornerRadius: Float, minorCornerRadius: Float) -> MeshResource](meshresource/generatebox(size:majorcornerradius:minorcornerradius:).md)
  Creates a box mesh from a vector of three scalar values that represent width, height, and depth, respectively, and radii for the corners.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/generatebox(size:cornerradius:)-8em0v)*