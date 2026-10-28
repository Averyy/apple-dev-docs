# generateBox(size:cornerRadius:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Creates a box mesh from a length for the box’s width, height, and depth, and a radius for the corners.

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
@preconcurrency static func generateBox(size: Float, cornerRadius: Float = 0) -> MeshResource
```

**Other overloads**:

```swift
@MainActor
@preconcurrency static func generateBox(size: SIMD3<Float>, cornerRadius: Float = 0) -> MeshResource
```

## Discussion

The method centers the box at the entity’s origin and aligns the box’s faces with the coordinate system’s axes.

> **Note**: The method clamps `cornerRadius` so that it doesn’t exceed half the length of the box’s smallest dimension.

## Parameters

- `size`: The length of the box’s width, height, and depth, in meters.
- `cornerRadius`: The radius of each corner’s circular arc, in meters. Values for `cornerRadius` can be, at most, equal to `size / 2.0`. For example, if the box’s dimensions are `5.0` x `5.0` x `5.0`, the corner radius needs to be in the range `[0.0, 2.5]`.

## See Also

### Creating a box
- [static func generateBox(size: SIMD3<Float>, cornerRadius: Float) -> MeshResource](./generatebox%28size,cornerradius%29-2ovma.md)
  Creates a box mesh from a vector of three scalar values that represent width, height, and depth, respectively, and a radius for the corners.
- [static func generateBox(width: Float, height: Float, depth: Float, cornerRadius: Float, splitFaces: Bool) -> MeshResource](./generatebox%28width,height,depth,cornerradius,splitfaces%29.md)
  Creates a box mesh from a width, height, depth and a corner radius, with the ability to assign different materials to each face.
- [static func generateBox(size: SIMD3<Float>, majorCornerRadius: Float, minorCornerRadius: Float) -> MeshResource](./generatebox%28size,majorcornerradius,minorcornerradius%29.md)
  Creates a box mesh from a vector of three scalar values that represent width, height, and depth, respectively, and radii for the corners.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/generatebox(size:cornerradius:)-8em0v)*