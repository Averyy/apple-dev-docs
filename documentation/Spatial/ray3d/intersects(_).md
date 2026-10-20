# intersects(_:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether a ray intersects a rectangle.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
func intersects(_ rect: Rect3D) -> Bool
```

#### Return Value

A Boolean value that indicates whether the ray intersects the rectangle.

## Parameters

- `rect`: The rectangle that the function compares against.

## See Also

### Checking characteristics
- [var isFinite: Bool](./isfinite.md)
  A Boolean value that indicates whether all of the values of the ray are finite.
- [var isNaN: Bool](./isnan.md)
  A Boolean value that indicates whether the ray contains any NaN values.
- [var isZero: Bool](./iszero.md)
  A Boolean value that indicates whether all of the values of the ray are zero.
- [func intersects(sphereOrigin: Point3D, sphereRadius: Double) -> Bool](./intersects%28sphereorigin,sphereradius%29.md)
  Returns a Boolean value that indicates whether the ray intersects a specified sphere.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/ray3d/intersects(_:))*