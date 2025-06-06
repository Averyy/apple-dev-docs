# GLKMatrix3RotateWithVector4(_:_:_:)

**Framework**: GLKit  
**Kind**: func

Returns a new `3x3` matrix created by concatenating a matrix with a rotation around a vector.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrix3RotateWithVector4(_ matrix: GLKMatrix3, _ radians: Float, _ axisVector: GLKVector4) -> GLKMatrix3
```

#### Return Value

A new matrix.

#### Discussion

The w-component of the `axisVector` parameter is ignored.

## Parameters

- `matrix`: The source matrix.
- `radians`: The angle of the rotation (a positive angle is counterclockwise).
- `axisVector`: The axis to perform the rotation around.

## See Also

- [func GLKMatrix3Invert(GLKMatrix3, UnsafeMutablePointer<Bool>!) -> GLKMatrix3](glkmatrix3invert(_:_:).md)
  Returns the inverse of a matrix.
- [func GLKMatrix3Transpose(GLKMatrix3) -> GLKMatrix3](glkmatrix3transpose(_:).md)
  Returns the transpose of a matrix.
- [func GLKMatrix3InvertAndTranspose(GLKMatrix3, UnsafeMutablePointer<Bool>!) -> GLKMatrix3](glkmatrix3invertandtranspose(_:_:).md)
  Returns the inverse transpose of a matrix.
- [func GLKMatrix3Multiply(GLKMatrix3, GLKMatrix3) -> GLKMatrix3](glkmatrix3multiply(_:_:).md)
  Returns the product of two matrices.
- [func GLKMatrix3Rotate(GLKMatrix3, Float, Float, Float, Float) -> GLKMatrix3](glkmatrix3rotate(_:_:_:_:_:).md)
  Returns a new `3x3` matrix created by concatenating a matrix with a rotation around a vector.
- [func GLKMatrix3RotateWithVector3(GLKMatrix3, Float, GLKVector3) -> GLKMatrix3](glkmatrix3rotatewithvector3(_:_:_:).md)
  Returns a new `3x3` matrix created by concatenating a matrix with a rotation around a vector.
- [func GLKMatrix3RotateX(GLKMatrix3, Float) -> GLKMatrix3](glkmatrix3rotatex(_:_:).md)
  Returns a new `3x3` matrix created by concatenating a matrix with a rotation around the x-axis.
- [func GLKMatrix3RotateY(GLKMatrix3, Float) -> GLKMatrix3](glkmatrix3rotatey(_:_:).md)
  Returns a new `3x3` matrix created by concatenating a matrix with a rotation around the y-axis.
- [func GLKMatrix3RotateZ(GLKMatrix3, Float) -> GLKMatrix3](glkmatrix3rotatez(_:_:).md)
  Returns a new `3x3` matrix created by concatenating a matrix with a rotation around the z-axis.
- [func GLKMatrix3Scale(GLKMatrix3, Float, Float, Float) -> GLKMatrix3](glkmatrix3scale(_:_:_:_:).md)
  Returns a new `3x3` matrix created by concatenating a matrix with a scaling transform.
- [func GLKMatrix3ScaleWithVector3(GLKMatrix3, GLKVector3) -> GLKMatrix3](glkmatrix3scalewithvector3(_:_:).md)
  Returns a new `3x3` matrix created by concatenating a matrix with a scaling transform defined by a vector.
- [func GLKMatrix3ScaleWithVector4(GLKMatrix3, GLKVector4) -> GLKMatrix3](glkmatrix3scalewithvector4(_:_:).md)
  Returns a new `3x3` matrix created by concatenating a matrix with a scaling transform defined by a vector.
- [func GLKMatrix3Add(GLKMatrix3, GLKMatrix3) -> GLKMatrix3](glkmatrix3add(_:_:).md)
  Returns a new `3x3` matrix created by performing a component-wise addition of two matrices.
- [func GLKMatrix3Subtract(GLKMatrix3, GLKMatrix3) -> GLKMatrix3](glkmatrix3subtract(_:_:).md)
  Returns a new `3x3` matrix created by performing a component-wise subtraction of two matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix3rotatewithvector4(_:_:_:))*