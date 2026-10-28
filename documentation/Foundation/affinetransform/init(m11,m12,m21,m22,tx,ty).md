# init(m11:m12:m21:m22:tX:tY:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates an affine transformation.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init(m11: CGFloat, m12: CGFloat, m21: CGFloat, m22: CGFloat, tX: CGFloat, tY: CGFloat)
```

## Discussion

Create an affine tranform by directly specifying the key values of the transform matrix.

```swift
[ m11 m12  0 ]
[ m21 m22  0 ]
[  tX  tY  1 ]
```

## See Also

### Creating Transforms
- [init()](./init%28%29.md)
  Creates an affine transformation matrix with identity values.
- [init(rotationByDegrees: CGFloat)](./init%28rotationbydegrees%29.md)
  Creates an affine transformation matrix from a rotation angle.
- [init(rotationByRadians: CGFloat)](./init%28rotationbyradians%29.md)
  Creates an affine transformation matrix from a rotation angle.
- [init(scale: CGFloat)](./init%28scale%29.md)
  Creates an affine transformation matrix from scaling a single value.
- [init(scaleByX: CGFloat, byY: CGFloat)](./init%28scalebyx,byy%29.md)
  Creates an affine transformation matrix from scaling values.
- [init(translationByX: CGFloat, byY: CGFloat)](./init%28translationbyx,byy%29.md)
  Creates an affine transformation matrix from translation values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/affinetransform/init(m11:m12:m21:m22:tx:ty:))*