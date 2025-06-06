# init(rotationByRadians:)

**Framework**: Foundation  
**Kind**: init

Creates an affine transformation matrix from a rotation angle.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- macOS 10.10+
- tvOS 9.0+
- watchOS 2.0+

## Declaration

```swift
init(rotationByRadians angle: CGFloat)
```

#### Discussion

The matrix takes the following form:

```swift
[  cos α   sin α  0 ]
[ -sin α   cos α  0 ]
[    0       0    1 ]
```

## Parameters

- `angle`: The rotation angle in radians.

## See Also

- [init()](affinetransform/init.md)
  Creates an affine transformation matrix with identity values.
- [init(rotationByDegrees: CGFloat)](affinetransform/init(rotationbydegrees:).md)
  Creates an affine transformation matrix from a rotation angle.
- [init(scale: CGFloat)](affinetransform/init(scale:).md)
  Creates an affine transformation matrix from scaling a single value.
- [init(scaleByX: CGFloat, byY: CGFloat)](affinetransform/init(scalebyx:byy:).md)
  Creates an affine transformation matrix from scaling values.
- [init(translationByX: CGFloat, byY: CGFloat)](affinetransform/init(translationbyx:byy:).md)
  Creates an affine transformation matrix from translation values.
- [init(m11: CGFloat, m12: CGFloat, m21: CGFloat, m22: CGFloat, tX: CGFloat, tY: CGFloat)](affinetransform/init(m11:m12:m21:m22:tx:ty:).md)
  Creates an affine transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/affinetransform/init(rotationbyradians:))*