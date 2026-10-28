# SPPoint3DMakeWithVector

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```c
static SPPoint3D SPPoint3DMakeWithVector(simd_double3 xyz);
```

## Return Value

A new point.

## Discussion

Creates a point with coordinates specified as a 3-element SIMD vector.

## Parameters

- `xyz`: The source vector.

## See Also

### Creating a 3D point structure
- [SPPoint3DMakeWithSize](./sppoint3dmakewithsize.md)
  Creates a point from the specified Spatial size structure.
- [SPPoint3DMakeWithSphericalCoordinates](./sppoint3dmakewithsphericalcoordinates.md)
  Returns a Spatial point that represents the Cartesian coordinates of the specified spherical coordinates structure.
- [SPPoint3DMakeWithVector](./sppoint3dmakewithvector-39d4f.md)
  Creates a point from the specified double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppoint3dmakewithvector-6eegc)*