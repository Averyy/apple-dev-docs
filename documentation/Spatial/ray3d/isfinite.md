# isFinite

**Framework**: Spatial  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether all of the values of the ray are finite.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
var isFinite: Bool { get }
```

## See Also

### Checking characteristics
- [var isNaN: Bool](./isnan.md)
  A Boolean value that indicates whether the ray contains any NaN values.
- [var isZero: Bool](./iszero.md)
  A Boolean value that indicates whether all of the values of the ray are zero.
- [func intersects(Rect3D) -> Bool](./intersects%28_%29.md)
  Returns a Boolean value that indicates whether a ray intersects a rectangle.
- [func intersects(sphereOrigin: Point3D, sphereRadius: Double) -> Bool](./intersects%28sphereorigin,sphereradius%29.md)
  Returns a Boolean value that indicates whether the ray intersects a specified sphere.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/ray3d/isfinite)*