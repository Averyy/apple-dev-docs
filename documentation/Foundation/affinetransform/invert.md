# invert()

**Framework**: Foundation  
**Kind**: method

Inverts the transformation matrix, if possible.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- macOS 10.10+
- tvOS 9.0+
- watchOS 2.0+

## Declaration

```swift
mutating func invert()
```

#### Discussion

Matrices with a determinant less than the smallest valid representation of a double value and greater than zero are invalid for representing as an inverse. If this can potentially happen to the input transform, use the [`inverted()`](affinetransform/inverted().md) method instead. The [`inverted()`](affinetransform/inverted().md) method returns `nil` if the function can’t reliably invert the matrix.

You can calculate the determinant using the following formula:

```swift
D = (m11 * m22) - (m12 * m21)
```

## See Also

- [func rotate(byDegrees: CGFloat)](affinetransform/rotate(bydegrees:).md)
  Mutates an affine transformation matrix to apply a rotation.
- [func rotate(byRadians: CGFloat)](affinetransform/rotate(byradians:).md)
  Mutates an affine transformation matrix to apply a rotation.
- [func scale(CGFloat)](affinetransform/scale(_:).md)
  Mutates an affine transformation matrix to apply scaling in both x and y dimensions.
- [func scale(x: CGFloat, y: CGFloat)](affinetransform/scale(x:y:).md)
  Mutates an affine transformation matrix to apply scaling in each of the x and y dimensions.
- [func translate(x: CGFloat, y: CGFloat)](affinetransform/translate(x:y:).md)
  Mutates an affine transformation matrix to perform the specified translation.
- [func append(AffineTransform)](affinetransform/append(_:).md)
  Mutates an affine transformation by appending another affine transform.
- [func prepend(AffineTransform)](affinetransform/prepend(_:).md)
  Mutates an affine transformation by prepending another affine transform.
- [func inverted() -> AffineTransform?](affinetransform/inverted.md)
  Returns an inverted version of the matrix, if possible, or nil if not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/affinetransform/invert())*