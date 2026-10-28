# invert()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Inverts the transformation matrix, if possible.

**Availability**:
- macOS 10.10+

## Declaration

```swift
mutating func invert()
```

## Discussion

Matrices with a determinant less than the smallest valid representation of a double value and greater than zero are invalid for representing as an inverse. If this can potentially happen to the input transform, use the [`inverted()`](./inverted%28%29.md) method instead. The [`inverted()`](./inverted%28%29.md) method returns `nil` if the function can’t reliably invert the matrix.

You can calculate the determinant using the following formula:

```swift
D = (m11 * m22) - (m12 * m21)
```

## See Also

### Accumulating Tranformations
- [func rotate(byDegrees: CGFloat)](./rotate%28bydegrees%29.md)
  Mutates an affine transformation matrix to apply a rotation.
- [func rotate(byRadians: CGFloat)](./rotate%28byradians%29.md)
  Mutates an affine transformation matrix to apply a rotation.
- [func scale(CGFloat)](./scale%28_%29.md)
  Mutates an affine transformation matrix to apply scaling in both x and y dimensions.
- [func scale(x: CGFloat, y: CGFloat)](./scale%28x,y%29.md)
  Mutates an affine transformation matrix to apply scaling in each of the x and y dimensions.
- [func translate(x: CGFloat, y: CGFloat)](./translate%28x,y%29.md)
  Mutates an affine transformation matrix to perform the specified translation.
- [func append(AffineTransform)](./append%28_%29.md)
  Mutates an affine transformation by appending another affine transform.
- [func prepend(AffineTransform)](./prepend%28_%29.md)
  Mutates an affine transformation by prepending another affine transform.
- [func inverted() -> AffineTransform?](./inverted%28%29.md)
  Returns an inverted version of the matrix, if possible, or nil if not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/affinetransform/invert())*