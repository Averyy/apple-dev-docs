# scale(x:y:)

**Framework**: Foundation  
**Kind**: method

Mutates an affine transformation matrix to apply scaling in each of the x and y dimensions.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- macOS 10.10+
- tvOS 9.0+
- watchOS 2.0+

## Declaration

```swift
mutating func scale(x: CGFloat, y: CGFloat)
```

## Parameters

- `x`: The horizontal scale factor.
- `y`: The vertical scale factor.

## See Also

- [func rotate(byDegrees: CGFloat)](affinetransform/rotate(bydegrees:).md)
  Mutates an affine transformation matrix to apply a rotation.
- [func rotate(byRadians: CGFloat)](affinetransform/rotate(byradians:).md)
  Mutates an affine transformation matrix to apply a rotation.
- [func scale(CGFloat)](affinetransform/scale(_:).md)
  Mutates an affine transformation matrix to apply scaling in both x and y dimensions.
- [func translate(x: CGFloat, y: CGFloat)](affinetransform/translate(x:y:).md)
  Mutates an affine transformation matrix to perform the specified translation.
- [func append(AffineTransform)](affinetransform/append(_:).md)
  Mutates an affine transformation by appending another affine transform.
- [func prepend(AffineTransform)](affinetransform/prepend(_:).md)
  Mutates an affine transformation by prepending another affine transform.
- [func invert()](affinetransform/invert.md)
  Inverts the transformation matrix, if possible.
- [func inverted() -> AffineTransform?](affinetransform/inverted.md)
  Returns an inverted version of the matrix, if possible, or nil if not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/affinetransform/scale(x:y:))*