# intersects(sphereOrigin:sphereRadius:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the ray intersects a specified sphere.

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
func intersects(sphereOrigin: Point3D, sphereRadius: Double) -> Bool
```

```c
static bool SPRay3DIntersectsSphere(SPRay3D ray, SPPoint3D sphereOrigin, double sphereRadius);
```

## See Also

### Checking characteristics
- [var isFinite: Bool](./isfinite.md)
  A Boolean value that indicates whether all of the values of the ray are finite.
- [var isNaN: Bool](./isnan.md)
  A Boolean value that indicates whether the ray contains any NaN values.
- [var isZero: Bool](./iszero.md)
  A Boolean value that indicates whether all of the values of the ray are zero.
- [func intersects(Rect3D) -> Bool](./intersects%28_%29.md)
  Returns a Boolean value that indicates whether a ray intersects a rectangle.
- [SPRay3DIsFinite](../spray3disfinite.md)
  A Boolean value that indicates whether all of the values of the ray are finite.
- [SPRay3DIsNaN](../spray3disnan.md)
  A Boolean value that indicates whether the ray contains any NaN values.
- [SPRay3DIsZero](../spray3diszero.md)
  A Boolean value that indicates whether all of the values of the ray are zero.
- [SPRay3DIntersectsRect](../spray3dintersectsrect.md)
  Returns a Boolean value that indicates whether a ray intersects a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/ray3d/intersects(sphereorigin:sphereradius:))*