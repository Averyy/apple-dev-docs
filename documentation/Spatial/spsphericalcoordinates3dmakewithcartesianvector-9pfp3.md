# SPSphericalCoordinates3DMakeWithCartesianVector

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```c
static SPSphericalCoordinates3D SPSphericalCoordinates3DMakeWithCartesianVector(SPVector3D xyz);
```

## Return Value

A new spherical coordinates structure.

## Discussion

Creates a spherical coordinates structure from the Cartesian coordinates represented by the specified Spatial vector.

## Parameters

- `xyz`: The source vector.

## See Also

### Creating a spherical coordinates structure
- [init(radius: Double, inclination: Angle2D, azimuth: Angle2D)](./sphericalcoordinates3d/init%28radius,inclination,azimuth%29.md)
  Creates a new spherical coordinates structure with the specified radius, inclination, and azimuth.
- [SPSphericalCoordinates3DMakeWithCartesianPoint](./spsphericalcoordinates3dmakewithcartesianpoint.md)
  Creates a spherical coordinates structure from the Cartesian coordinates represented by the specified Spatial point.
- [SPSphericalCoordinates3DMakeWithCartesianVector](./spsphericalcoordinates3dmakewithcartesianvector-940l6.md)
  Creates a spherical coordinates structure from the Cartesian coordinates represented by the specified simd vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spsphericalcoordinates3dmakewithcartesianvector-9pfp3)*