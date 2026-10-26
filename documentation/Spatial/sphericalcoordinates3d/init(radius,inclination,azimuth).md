# init(radius:inclination:azimuth:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

Creates a new spherical coordinates structure with the specified radius, inclination, and azimuth.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(radius: Double, inclination: Angle2D, azimuth: Angle2D)
```

```c
static SPSphericalCoordinates3D SPSphericalCoordinates3DMake(double radius, SPAngle inclination, SPAngle azimuth);
```

## See Also

### Creating a spherical coordinates structure
- [init()](./init%28%29.md)
  Creates a spherical coordinates structure.
- [init(Vector3D)](./init%28_%29-2eoox.md)
  Creates a spherical coordinates structure from the Cartesian coordinates represented by the specified simd vector.
- [init(Point3D)](./init%28_%29-45qdy.md)
  Creates a spherical coordinates structure from the Cartesian coordinates represented by the specified Spatial point.
- [init(simd_double3)](./init%28_%29-1xzjz.md)
  Creates a new spherical coordinates structure from the specified Cartesian coordinates represented by a simd vector.
- [init(vector: simd_double3)](./init%28vector%29.md)
  Creates a new spherical coordinates structure from the specified Cartesian coordinates represented by a simd vector.
- [init(x: Double, y: Double, z: Double)](./init%28x,y,z%29.md)
  Creates a new spherical coordinates structure from the specified Cartesian coordinates.
- [SPSphericalCoordinates3DMakeWithCartesianPoint](../spsphericalcoordinates3dmakewithcartesianpoint.md)
  Creates a spherical coordinates structure from the Cartesian coordinates represented by the specified Spatial point.
- [SPSphericalCoordinates3DMakeWithCartesianVector](../spsphericalcoordinates3dmakewithcartesianvector-940l6.md)
  Creates a spherical coordinates structure from the Cartesian coordinates represented by the specified simd vector.
- [SPSphericalCoordinates3DMakeWithCartesianVector](../spsphericalcoordinates3dmakewithcartesianvector-9pfp3.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sphericalcoordinates3d/init(radius:inclination:azimuth:))*