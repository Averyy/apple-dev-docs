# GLKMatrix4TranslateWithVector3(_:_:)

**Framework**: GLKit  
**Kind**: func

Returns a new `4x4` matrix created by concatenating a matrix with a translation transform defined by a vector.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrix4TranslateWithVector3(_ matrix: GLKMatrix4, _ translationVector: GLKVector3) -> GLKMatrix4
```

#### Return Value

A new matrix.

## Parameters

- `matrix`: A matrix.
- `translationVector`: A vector whose  ,   and   components are used to translate the matrix.

## See Also

- [func GLKMatrix4Invert(GLKMatrix4, UnsafeMutablePointer<Bool>?) -> GLKMatrix4](glkmatrix4invert(_:_:).md)
  Returns the inverse of a matrix.
- [func GLKMatrix4Transpose(GLKMatrix4) -> GLKMatrix4](glkmatrix4transpose(_:).md)
  Returns the transpose of a matrix.
- [func GLKMatrix4InvertAndTranspose(GLKMatrix4, UnsafeMutablePointer<Bool>?) -> GLKMatrix4](glkmatrix4invertandtranspose(_:_:).md)
  Returns the inverse transpose of a matrix.
- [func GLKMatrix4Multiply(GLKMatrix4, GLKMatrix4) -> GLKMatrix4](glkmatrix4multiply(_:_:).md)
  Returns the product of two matrices.
- [func GLKMatrix4Rotate(GLKMatrix4, Float, Float, Float, Float) -> GLKMatrix4](glkmatrix4rotate(_:_:_:_:_:).md)
  Returns a new `4x4` matrix created by concatenating a matrix with a rotation around a vector.
- [func GLKMatrix4RotateWithVector3(GLKMatrix4, Float, GLKVector3) -> GLKMatrix4](glkmatrix4rotatewithvector3(_:_:_:).md)
  Returns a new `4x4` matrix created by concatenating a matrix with a rotation around a vector.
- [func GLKMatrix4RotateWithVector4(GLKMatrix4, Float, GLKVector4) -> GLKMatrix4](glkmatrix4rotatewithvector4(_:_:_:).md)
  Returns a new `4x4` matrix created by concatenating a matrix with a rotation around a vector.
- [func GLKMatrix4RotateX(GLKMatrix4, Float) -> GLKMatrix4](glkmatrix4rotatex(_:_:).md)
  Returns a new `4x4` matrix created by concatenating a matrix with a rotation around the x-axis.
- [func GLKMatrix4RotateY(GLKMatrix4, Float) -> GLKMatrix4](glkmatrix4rotatey(_:_:).md)
  Returns a new `4x4` matrix created by concatenating a matrix with a rotation around the y-axis.
- [func GLKMatrix4RotateZ(GLKMatrix4, Float) -> GLKMatrix4](glkmatrix4rotatez(_:_:).md)
  Returns a new `4x4` matrix created by concatenating a matrix with a rotation around the z-axis.
- [func GLKMatrix4Scale(GLKMatrix4, Float, Float, Float) -> GLKMatrix4](glkmatrix4scale(_:_:_:_:).md)
  Returns a new `4x4` matrix created by concatenating a matrix with a scaling transform.
- [func GLKMatrix4ScaleWithVector3(GLKMatrix4, GLKVector3) -> GLKMatrix4](glkmatrix4scalewithvector3(_:_:).md)
  Returns a new `4x4` matrix created by concatenating a matrix with a scaling transform defined by a vector.
- [func GLKMatrix4ScaleWithVector4(GLKMatrix4, GLKVector4) -> GLKMatrix4](glkmatrix4scalewithvector4(_:_:).md)
  Returns a new `4x4` matrix created by concatenating a matrix with a scaling transform defined by a vector.
- [func GLKMatrix4Translate(GLKMatrix4, Float, Float, Float) -> GLKMatrix4](glkmatrix4translate(_:_:_:_:).md)
  Returns a new `4x4` matrix created by concatenating a matrix with a translation transform.
- [func GLKMatrix4TranslateWithVector4(GLKMatrix4, GLKVector4) -> GLKMatrix4](glkmatrix4translatewithvector4(_:_:).md)
  Returns a new `4x4` matrix created by concatenating a matrix with a translation transform defined by a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix4translatewithvector3(_:_:))*