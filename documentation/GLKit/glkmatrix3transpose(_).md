# GLKMatrix3Transpose(_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns the transpose of a matrix.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrix3Transpose(_ matrix: GLKMatrix3) -> GLKMatrix3
```

```c
static GLKMatrix3 GLKMatrix3Transpose(GLKMatrix3 matrix);
```

## Return Value

The transpose of the matrix.

## Parameters

- `matrix`: A matrix.

## See Also

### Performing Mathematical Operations on Matrices
- [func GLKMatrix3Invert(GLKMatrix3, UnsafeMutablePointer<Bool>!) -> GLKMatrix3](./glkmatrix3invert%28_,_%29.md)
  Returns the inverse of a matrix.
- [func GLKMatrix3InvertAndTranspose(GLKMatrix3, UnsafeMutablePointer<Bool>!) -> GLKMatrix3](./glkmatrix3invertandtranspose%28_,_%29.md)
  Returns the inverse transpose of a matrix.
- [func GLKMatrix3Multiply(GLKMatrix3, GLKMatrix3) -> GLKMatrix3](./glkmatrix3multiply%28_,_%29.md)
  Returns the product of two matrices.
- [func GLKMatrix3Rotate(GLKMatrix3, Float, Float, Float, Float) -> GLKMatrix3](./glkmatrix3rotate%28_,_,_,_,_%29.md)
  Returns a new `3x3` matrix created by concatenating a matrix with a rotation around a vector.
- [func GLKMatrix3RotateWithVector3(GLKMatrix3, Float, GLKVector3) -> GLKMatrix3](./glkmatrix3rotatewithvector3%28_,_,_%29.md)
  Returns a new `3x3` matrix created by concatenating a matrix with a rotation around a vector.
- [func GLKMatrix3RotateWithVector4(GLKMatrix3, Float, GLKVector4) -> GLKMatrix3](./glkmatrix3rotatewithvector4%28_,_,_%29.md)
  Returns a new `3x3` matrix created by concatenating a matrix with a rotation around a vector.
- [func GLKMatrix3RotateX(GLKMatrix3, Float) -> GLKMatrix3](./glkmatrix3rotatex%28_,_%29.md)
  Returns a new `3x3` matrix created by concatenating a matrix with a rotation around the x-axis.
- [func GLKMatrix3RotateY(GLKMatrix3, Float) -> GLKMatrix3](./glkmatrix3rotatey%28_,_%29.md)
  Returns a new `3x3` matrix created by concatenating a matrix with a rotation around the y-axis.
- [func GLKMatrix3RotateZ(GLKMatrix3, Float) -> GLKMatrix3](./glkmatrix3rotatez%28_,_%29.md)
  Returns a new `3x3` matrix created by concatenating a matrix with a rotation around the z-axis.
- [func GLKMatrix3Scale(GLKMatrix3, Float, Float, Float) -> GLKMatrix3](./glkmatrix3scale%28_,_,_,_%29.md)
  Returns a new `3x3` matrix created by concatenating a matrix with a scaling transform.
- [func GLKMatrix3ScaleWithVector3(GLKMatrix3, GLKVector3) -> GLKMatrix3](./glkmatrix3scalewithvector3%28_,_%29.md)
  Returns a new `3x3` matrix created by concatenating a matrix with a scaling transform defined by a vector.
- [func GLKMatrix3ScaleWithVector4(GLKMatrix3, GLKVector4) -> GLKMatrix3](./glkmatrix3scalewithvector4%28_,_%29.md)
  Returns a new `3x3` matrix created by concatenating a matrix with a scaling transform defined by a vector.
- [func GLKMatrix3Add(GLKMatrix3, GLKMatrix3) -> GLKMatrix3](./glkmatrix3add%28_,_%29.md)
  Returns a new `3x3` matrix created by performing a component-wise addition of two matrices.
- [func GLKMatrix3Subtract(GLKMatrix3, GLKMatrix3) -> GLKMatrix3](./glkmatrix3subtract%28_,_%29.md)
  Returns a new `3x3` matrix created by performing a component-wise subtraction of two matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix3transpose(_:))*