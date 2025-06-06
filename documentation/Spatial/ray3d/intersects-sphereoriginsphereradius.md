# intersects(sphereOrigin:sphereRadius:)

**Framework**: Spatial  
**Kind**: method

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

## See Also

- [var isFinite: Bool](ray3d/isfinite.md)
  A Boolean value that indicates whether all of the values of the ray are finite.
- [var isNaN: Bool](ray3d/isnan.md)
  A Boolean value that indicates whether the ray contains any NaN values.
- [var isZero: Bool](ray3d/iszero.md)
  A Boolean value that indicates whether all of the values of the ray are zero.
- [func intersects(Rect3D) -> Bool](ray3d/intersects(_:).md)
  Returns a Boolean value that indicates whether a ray intersects a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/ray3d/intersects(sphereorigin:sphereradius:))*