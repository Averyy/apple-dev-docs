# translateX(by:yBy:)

**Framework**: Foundation  
**Kind**: method

Applies the specified translation factors to the receiver’s transformation matrix.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func translateX(by deltaX: Double, yBy deltaY: Double)
```

#### Discussion

Subsequent transformations cause coordinates to be shifted by `deltaX` units along the x axis and by `deltaY` units along the y axis. Translation factors do not affect `NSSize` values, which specify a differential between points.

## Parameters

- `deltaX`: The number of units to move along the x axis.
- `deltaY`: The number of units to move along the y axis.

## See Also

- [func rotate(byDegrees: Double)](nsaffinetransform/rotate(bydegrees:).md)
  Applies a rotation factor (measured in degrees) to the receiver’s transformation matrix.
- [func rotate(byRadians: Double)](nsaffinetransform/rotate(byradians:).md)
  Applies a rotation factor (measured in radians) to the receiver’s transformation matrix.
- [func scale(by: Double)](nsaffinetransform/scale(by:).md)
  Applies the specified scaling factor along both x and y axes to the receiver’s transformation matrix.
- [func scaleX(by: Double, yBy: Double)](nsaffinetransform/scalex(by:yby:).md)
  Applies scaling factors to each axis of the receiver’s transformation matrix.
- [func append(NSAffineTransform)](nsaffinetransform/append(_:).md)
  Appends the specified matrix to the receiver’s matrix.
- [func prepend(NSAffineTransform)](nsaffinetransform/prepend(_:).md)
  Prepends the specified matrix to the receiver’s matrix.
- [func invert()](nsaffinetransform/invert.md)
  Replaces the receiver’s matrix with its inverse matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsaffinetransform/translatex(by:yby:))*