# SPRay3DIntersectsRect

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether a ray intersects a rectangle.

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
static bool SPRay3DIntersectsRect(SPRay3D ray, SPRect3D rect);
```

## See Also

### Checking characteristics
- [func intersects(sphereOrigin: Point3D, sphereRadius: Double) -> Bool](./ray3d/intersects%28sphereorigin,sphereradius%29.md)
  Returns a Boolean value that indicates whether the ray intersects a specified sphere.
- [SPRay3DIsFinite](./spray3disfinite.md)
  A Boolean value that indicates whether all of the values of the ray are finite.
- [SPRay3DIsNaN](./spray3disnan.md)
  A Boolean value that indicates whether the ray contains any NaN values.
- [SPRay3DIsZero](./spray3diszero.md)
  A Boolean value that indicates whether all of the values of the ray are zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spray3dintersectsrect)*