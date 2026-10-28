# GLKMatrix4Subtract(_:_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns a new `4x4` matrix created by performing a component-wise subtraction of two matrices.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrix4Subtract(_ matrixLeft: GLKMatrix4, _ matrixRight: GLKMatrix4) -> GLKMatrix4
```

```c
static GLKMatrix4 GLKMatrix4Subtract(GLKMatrix4 matrixLeft, GLKMatrix4 matrixRight);
```

## Return Value

A new matrix whose components each represent the difference between the components found in the same positions of the two source matrices.

## Parameters

- `matrixLeft`: The starting matrix.
- `matrixRight`: The matrix to subtract.

## See Also

### Performing Mathematical Operations on Matrices
- [func GLKMatrix4Invert(GLKMatrix4, UnsafeMutablePointer<Bool>?) -> GLKMatrix4](./glkmatrix4invert%28_,_%29.md)
  Returns the inverse of a matrix.
- [func GLKMatrix4Transpose(GLKMatrix4) -> GLKMatrix4](./glkmatrix4transpose%28_%29.md)
  Returns the transpose of a matrix.
- [func GLKMatrix4InvertAndTranspose(GLKMatrix4, UnsafeMutablePointer<Bool>?) -> GLKMatrix4](./glkmatrix4invertandtranspose%28_,_%29.md)
  Returns the inverse transpose of a matrix.
- [func GLKMatrix4Multiply(GLKMatrix4, GLKMatrix4) -> GLKMatrix4](./glkmatrix4multiply%28_,_%29.md)
  Returns the product of two matrices.
- [func GLKMatrix4Rotate(GLKMatrix4, Float, Float, Float, Float) -> GLKMatrix4](./glkmatrix4rotate%28_,_,_,_,_%29.md)
  Returns a new `4x4` matrix created by concatenating a matrix with a rotation around a vector.
- [func GLKMatrix4RotateWithVector3(GLKMatrix4, Float, GLKVector3) -> GLKMatrix4](./glkmatrix4rotatewithvector3%28_,_,_%29.md)
  Returns a new `4x4` matrix created by concatenating a matrix with a rotation around a vector.
- [func GLKMatrix4RotateWithVector4(GLKMatrix4, Float, GLKVector4) -> GLKMatrix4](./glkmatrix4rotatewithvector4%28_,_,_%29.md)
  Returns a new `4x4` matrix created by concatenating a matrix with a rotation around a vector.
- [func GLKMatrix4RotateX(GLKMatrix4, Float) -> GLKMatrix4](./glkmatrix4rotatex%28_,_%29.md)
  Returns a new `4x4` matrix created by concatenating a matrix with a rotation around the x-axis.
- [func GLKMatrix4RotateY(GLKMatrix4, Float) -> GLKMatrix4](./glkmatrix4rotatey%28_,_%29.md)
  Returns a new `4x4` matrix created by concatenating a matrix with a rotation around the y-axis.
- [func GLKMatrix4RotateZ(GLKMatrix4, Float) -> GLKMatrix4](./glkmatrix4rotatez%28_,_%29.md)
  Returns a new `4x4` matrix created by concatenating a matrix with a rotation around the z-axis.
- [func GLKMatrix4Scale(GLKMatrix4, Float, Float, Float) -> GLKMatrix4](./glkmatrix4scale%28_,_,_,_%29.md)
  Returns a new `4x4` matrix created by concatenating a matrix with a scaling transform.
- [func GLKMatrix4ScaleWithVector3(GLKMatrix4, GLKVector3) -> GLKMatrix4](./glkmatrix4scalewithvector3%28_,_%29.md)
  Returns a new `4x4` matrix created by concatenating a matrix with a scaling transform defined by a vector.
- [func GLKMatrix4ScaleWithVector4(GLKMatrix4, GLKVector4) -> GLKMatrix4](./glkmatrix4scalewithvector4%28_,_%29.md)
  Returns a new `4x4` matrix created by concatenating a matrix with a scaling transform defined by a vector.
- [func GLKMatrix4Translate(GLKMatrix4, Float, Float, Float) -> GLKMatrix4](./glkmatrix4translate%28_,_,_,_%29.md)
  Returns a new `4x4` matrix created by concatenating a matrix with a translation transform.
- [func GLKMatrix4TranslateWithVector3(GLKMatrix4, GLKVector3) -> GLKMatrix4](./glkmatrix4translatewithvector3%28_,_%29.md)
  Returns a new `4x4` matrix created by concatenating a matrix with a translation transform defined by a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix4subtract(_:_:))*