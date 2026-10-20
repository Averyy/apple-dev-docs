# scaleX(by:yBy:)

**Framework**: Foundation  
**Kind**: method

Applies scaling factors to each axis of the receiver’s transformation matrix.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func scaleX(by scaleX: Double, yBy scaleY: Double)
```

#### Discussion

After invoking this method, applying the receiver’s matrix modifies the unit length on the x axis by a factor of `scaleX` and the y axis by a factor of `scaleY`, in addition to performing all previous transformations. A value of 1.0 for either axis scales the content on that axis to the same size.

## Parameters

- `scaleX`: The scaling factor to apply to the x axis.
- `scaleY`: The scaling factor to apply to the y axis.

## See Also

- [func rotate(byDegrees: Double)](nsaffinetransform/rotate(bydegrees:).md)
  Applies a rotation factor (measured in degrees) to the receiver’s transformation matrix.
- [func rotate(byRadians: Double)](nsaffinetransform/rotate(byradians:).md)
  Applies a rotation factor (measured in radians) to the receiver’s transformation matrix.
- [func scale(by: Double)](nsaffinetransform/scale(by:).md)
  Applies the specified scaling factor along both x and y axes to the receiver’s transformation matrix.
- [func translateX(by: Double, yBy: Double)](nsaffinetransform/translatex(by:yby:).md)
  Applies the specified translation factors to the receiver’s transformation matrix.
- [func append(NSAffineTransform)](nsaffinetransform/append(_:).md)
  Appends the specified matrix to the receiver’s matrix.
- [func prepend(NSAffineTransform)](nsaffinetransform/prepend(_:).md)
  Prepends the specified matrix to the receiver’s matrix.
- [func invert()](nsaffinetransform/invert.md)
  Replaces the receiver’s matrix with its inverse matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsaffinetransform/scalex(by:yby:))*