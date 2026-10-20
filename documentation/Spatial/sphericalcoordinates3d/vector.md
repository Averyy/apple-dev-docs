# vector

**Framework**: Spatial  
**Kind**: property  
**Role**: Instance Property

A simd three-element vector that contains the radius, inclination, and azimuth values.

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
var vector: simd_double3 { get set }
```

```c
simd_double3 vector;
```

## See Also

### Inspecting a spherical coordinates structure’s properties
- [var azimuth: Angle2D](./azimuth.md)
  The azimuthal angle, in radians.
- [var inclination: Angle2D](./inclination.md)
  The inclination angle, in radians.
- [var radius: Double](./radius.md)
  The distance to the origin.
- [var customMirror: Mirror](./custommirror.md)
  The custom mirror for this instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sphericalcoordinates3d/vector)*