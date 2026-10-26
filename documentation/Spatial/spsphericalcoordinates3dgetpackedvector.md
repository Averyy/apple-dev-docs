# SPSphericalCoordinates3DGetPackedVector

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
static simd_packed_double4 SPSphericalCoordinates3DGetPackedVector(SPSphericalCoordinates3D coords);
```

#### Return Value

A new packed simd vector, where `x` is the radius, `y` is the inclination (in radians), and `z` is the azimuth (in radians).

#### Discussion

Creates a packed simd vector from a Spatial spherical coordinates structure.

## Parameters

- `coords`: The source spherical coordinates structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spsphericalcoordinates3dgetpackedvector)*