# SPPoint3DFloatMakeWithSphericalCoordinates

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
static SPPoint3DFloat SPPoint3DFloatMakeWithSphericalCoordinates(SPSphericalCoordinates3DFloat coords);
```

## Return Value

A new point that contains the spherical coorddinates converted to Cartesian coordinates.

## Discussion

Returns a Spatial point that represents the Cartesian coordinates of the specified spherical coordinates structure.

## Parameters

- `coords`: The source spherical coordinates structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppoint3dfloatmakewithsphericalcoordinates)*