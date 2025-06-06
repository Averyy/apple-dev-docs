# invert()

**Framework**: Foundation  
**Kind**: method

Replaces the receiver’s matrix with its inverse matrix.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func invert()
```

#### Discussion

Inverse matrices are useful for undoing the effects of a matrix. If a previous point (x,y) was transformed to (x’,y’), inverting the matrix and applying it to point (x’,y’) yields the point (x,y).

You can also use inverse matrices in conjunction with the [`concat()`](nsaffinetransform/concat().md) method to remove the effects of concatenating the matrix to the current transformation matrix of the current graphic context.

## See Also

- [func rotate(byDegrees: Double)](nsaffinetransform/rotate(bydegrees:).md)
  Applies a rotation factor (measured in degrees) to the receiver’s transformation matrix.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsaffinetransform/invert())*