# SPSphericalCoordinates3DMakeWithPackedVector

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```c
static SPSphericalCoordinates3D SPSphericalCoordinates3DMakeWithPackedVector(simd_packed_double4 source);
```

## Return Value

A new spherical coordinates structure.

## Discussion

Creates a Spatial spherical coordinates structure from a packed simd vector.

## Parameters

- `source`: The source vector, where `x` is the radius, `y` is the inclination (in radians), and `z` is the azimuth (in radians).


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spsphericalcoordinates3dmakewithpackedvector)*