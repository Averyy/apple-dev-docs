# init(x:y:z:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

Creates a point from the specified floating-point values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
init<T>(x: T, y: T, z: T) where T : BinaryFloatingPoint
```

## Parameters

- `x`: A floating-point value that specifies the x-coordinate value.
- `y`: A floating-point value that specifies the y-coordinate value.
- `z`: A floating-point value that specifies the z-coordinate value.

## See Also

### Creating a 3D point structure
- [init()](./init%28%29.md)
  Creates a point.
- [init(x: Double, y: Double, z: Double)](./init%28x,y,z%29-3lary.md)
  Creates a point from the specified double-precision values.
- [init(vector: simd_double3)](./init%28vector%29.md)
  Creates a point from the specified double-precision vector.
- [init(Size3D)](./init%28_%29-1f1ha.md)
  Creates a point from the specified Spatial size structure.
- [init(simd_float3)](./init%28_%29-1kved.md)
  Creates a point from the specified single-precision vector.
- [init(Vector3D)](./init%28_%29-34plj.md)
  Creates a point from the specified Spatial vector.
- [init(simd_double3)](./init%28_%29-4gu20.md)
  Creates a point from the specified double-precision vector.
- [init(SphericalCoordinates3D)](./init%28_%29-50tw4.md)
  Returns a Spatial point that represents the Cartesian coordinates of the specified spherical coordinates structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/point3d/init(x:y:z:)-28jhw)*