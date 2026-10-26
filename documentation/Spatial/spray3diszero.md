# SPRay3DIsZero

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

A Boolean value that indicates whether all of the values of the ray are zero.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```c
static bool SPRay3DIsZero(SPRay3D ray);
```

## See Also

### Checking characteristics
- [func intersects(sphereOrigin: Point3D, sphereRadius: Double) -> Bool](./ray3d/intersects%28sphereorigin,sphereradius%29.md)
  Returns a Boolean value that indicates whether the ray intersects a specified sphere.
- [SPRay3DIsFinite](./spray3disfinite.md)
  A Boolean value that indicates whether all of the values of the ray are finite.
- [SPRay3DIsNaN](./spray3disnan.md)
  A Boolean value that indicates whether the ray contains any NaN values.
- [SPRay3DIntersectsRect](./spray3dintersectsrect.md)
  Returns a Boolean value that indicates whether a ray intersects a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spray3diszero)*