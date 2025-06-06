# prepend(_:)

**Framework**: Foundation  
**Kind**: method

Prepends the specified matrix to the receiver’s matrix.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func prepend(_ transform: AffineTransform)
```

#### Discussion

This method multiplies the matrix in `transform` by the receiver’s matrix and replaces the receiver’s matrix with the result. This type of operation is the same as applying the transformations in `transform` followed by the transformations in the receiver.

## Parameters

- `transform`: The matrix to prepend to the receiver.

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
- [func invert()](nsaffinetransform/invert.md)
  Replaces the receiver’s matrix with its inverse matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsaffinetransform/prepend(_:))*