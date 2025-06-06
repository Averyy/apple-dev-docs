# rotate(byDegrees:)

**Framework**: Foundation  
**Kind**: method

Mutates an affine transformation matrix to apply a rotation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- macOS 10.10+
- tvOS 9.0+
- watchOS 2.0+

## Declaration

```swift
mutating func rotate(byDegrees angle: CGFloat)
```

#### Discussion

The matrix takes the following form:

```swift
[  cos α   sin α  0 ]
[ -sin α   cos α  0 ]
[    0       0    1 ]
```

## Parameters

- `angle`: The rotation angle in degrees.

## See Also

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
- [func invert()](affinetransform/invert.md)
  Inverts the transformation matrix, if possible.
- [func inverted() -> AffineTransform?](affinetransform/inverted.md)
  Returns an inverted version of the matrix, if possible, or nil if not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/affinetransform/rotate(bydegrees:))*