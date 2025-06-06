# init(x:y:z:)

**Framework**: Spatial  
**Kind**: init

Creates a vector from the specified floating-point values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
init<T>(x: T, y: T, z: T) where T : BinaryFloatingPoint
```

## Parameters

- `x`: A floating-point value that specifies the x value.
- `y`: A floating-point value that specifies the y value.
- `z`: A floating-point value that specifies the z value.

## See Also

- [init()](vector3d/init.md)
  Creates a vector.
- [init(x: Double, y: Double, z: Double)](vector3d/init(x:y:z:)-2ejxw.md)
  Creates a vector from the specified double-precision values.
- [init(simd_float3)](vector3d/init(_:)-73gdm.md)
  Creates a ray from the specified single-precision vector.
- [init(simd_double3)](vector3d/init(_:)-1a9i3.md)
  Creates a vector from the specified double-precision vector.
- [init(vector: simd_double3)](vector3d/init(vector:).md)
  Creates a vector from the specified double-precision vector.
- [init(RotationAxis3D)](vector3d/init(_:)-3br9h.md)
  Creates a vector from the specified Spatial rotation axis.
- [init(Point3D)](vector3d/init(_:)-8vcph.md)
  Creates a vector from the specified Spatial point structure.
- [init(Size3D)](vector3d/init(_:)-8egfs.md)
  Creates a vector from the specified Spatial size structure.
- [init(SphericalCoordinates3D)](vector3d/init(_:)-9ker1.md)
  Creates a vector from the specified Spatial spherical coordinates structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/vector3d/init(x:y:z:)-29hwg)*