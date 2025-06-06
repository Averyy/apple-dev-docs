# init(m11:m12:m21:m22:tX:tY:)

**Framework**: Foundation  
**Kind**: init

Creates an affine transformation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- macOS 10.10+
- tvOS 9.0+
- watchOS 2.0+

## Declaration

```swift
init(m11: CGFloat, m12: CGFloat, m21: CGFloat, m22: CGFloat, tX: CGFloat, tY: CGFloat)
```

#### Discussion

Create an affine tranform by directly specifying the key values of the transform matrix.

```swift
[ m11 m12  0 ]
[ m21 m22  0 ]
[  tX  tY  1 ]
```

## See Also

- [init()](affinetransform/init.md)
  Creates an affine transformation matrix with identity values.
- [init(rotationByDegrees: CGFloat)](affinetransform/init(rotationbydegrees:).md)
  Creates an affine transformation matrix from a rotation angle.
- [init(rotationByRadians: CGFloat)](affinetransform/init(rotationbyradians:).md)
  Creates an affine transformation matrix from a rotation angle.
- [init(scale: CGFloat)](affinetransform/init(scale:).md)
  Creates an affine transformation matrix from scaling a single value.
- [init(scaleByX: CGFloat, byY: CGFloat)](affinetransform/init(scalebyx:byy:).md)
  Creates an affine transformation matrix from scaling values.
- [init(translationByX: CGFloat, byY: CGFloat)](affinetransform/init(translationbyx:byy:).md)
  Creates an affine transformation matrix from translation values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/affinetransform/init(m11:m12:m21:m22:tx:ty:))*