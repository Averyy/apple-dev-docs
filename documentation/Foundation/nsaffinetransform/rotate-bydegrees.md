# rotate(byDegrees:)

**Framework**: Foundation  
**Kind**: method

Applies a rotation factor (measured in degrees) to the receiver’s transformation matrix.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func rotate(byDegrees angle: Double)
```

#### Discussion

After invoking this method, applying the receiver’s matrix turns the axes counterclockwise about the current origin by `angle` degrees, in addition to performing all previous transformations.

## Parameters

- `angle`: The rotation angle, measured in degrees.

## See Also

- [func rotate(byRadians: Double)](nsaffinetransform/rotate(byradians:).md)
  Applies a rotation factor (measured in radians) to the receiver’s transformation matrix.
- [func scale(by: Double)](nsaffinetransform/scale(by:).md)
  Applies the specified scaling factor along both x and y axes to the receiver’s transformation matrix.
- [func scaleX(by: Double, yBy: Double)](nsaffinetransform/scalex(by:yby:).md)
  Applies scaling factors to each axis of the receiver’s transformation matrix.
- [func translateX(by: Double, yBy: Double)](nsaffinetransform/translatex(by:yby:).md)
  Applies the specified translation factors to the receiver’s transformation matrix.
- [func append(NSAffineTransform)](nsaffinetransform/append(_:).md)
  Appends the specified matrix to the receiver’s matrix.
- [func prepend(NSAffineTransform)](nsaffinetransform/prepend(_:).md)
  Prepends the specified matrix to the receiver’s matrix.
- [func invert()](nsaffinetransform/invert.md)
  Replaces the receiver’s matrix with its inverse matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsaffinetransform/rotate(bydegrees:))*