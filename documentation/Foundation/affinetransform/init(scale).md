# init(scale:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates an affine transformation matrix from scaling a single value.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init(scale factor: CGFloat)
```

#### Discussion

The matrix takes the following form:

```swift
[ f  0  0 ]
[ 0  f  0 ]
[ 0  0  1 ]
```

## Parameters

- `factor`: The scale factor.

## See Also

### Creating Transforms
- [init()](./init%28%29.md)
  Creates an affine transformation matrix with identity values.
- [init(rotationByDegrees: CGFloat)](./init%28rotationbydegrees%29.md)
  Creates an affine transformation matrix from a rotation angle.
- [init(rotationByRadians: CGFloat)](./init%28rotationbyradians%29.md)
  Creates an affine transformation matrix from a rotation angle.
- [init(scaleByX: CGFloat, byY: CGFloat)](./init%28scalebyx,byy%29.md)
  Creates an affine transformation matrix from scaling values.
- [init(translationByX: CGFloat, byY: CGFloat)](./init%28translationbyx,byy%29.md)
  Creates an affine transformation matrix from translation values.
- [init(m11: CGFloat, m12: CGFloat, m21: CGFloat, m22: CGFloat, tX: CGFloat, tY: CGFloat)](./init%28m11,m12,m21,m22,tx,ty%29.md)
  Creates an affine transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/affinetransform/init(scale:))*