# rotation(to:)

**Framework**: Spatial  
**Kind**: method

Returns the rotation around the origin from the first point to the second point.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func rotation(to other: Point3D) -> Rotation3D
```

#### Return Value

The rotation between two points.

## Parameters

- `other`: The second point that the function computes the rotation to.

## See Also

- [var origin: Point3D](point3d/origin.md)
- [var simd: simd_double3](point3d/simd.md)
  A simd three-element vector that contains the x-, y-, and z-coordinate values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/point3d/rotation(to:))*