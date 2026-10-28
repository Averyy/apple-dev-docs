# init(radius:inclination:azimuth:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(radius: Float, inclination: Angle2DFloat, azimuth: Angle2DFloat)
```

```c
static SPSphericalCoordinates3DFloat SPSphericalCoordinates3DFloatMake(float radius, SPAngleFloat inclination, SPAngleFloat azimuth);
```

## Return Value

A new point.

## Discussion

Creates a single-precision spherical coordinates structure.

## Parameters

- `radius`: The distance to the origin.
- `inclination`: The inclination angle.
- `azimuth`: The azimuthal angle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sphericalcoordinates3dfloat/init(radius:inclination:azimuth:))*