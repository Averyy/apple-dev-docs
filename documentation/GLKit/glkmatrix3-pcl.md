# GLKMatrix3

**Framework**: GLKit

#### Overview

The `GLKMatrix3` type defines a `3x3` floating-point matrix as well as many mathematical operations commonly used to manipulate matrices. A `3x3` matrix is commonly used in graphics programming to represent scaling or rotation transformations to convert from one coordinate system to another.

The functions that manipulate `GLKMatrix3` structures treat the inputs as immutable, instead returning a new matrix that represent the results of the operation.

## Topics

### Creating Matrices
- [func GLKMatrix3Make(Float, Float, Float, Float, Float, Float, Float, Float, Float) -> GLKMatrix3](glkmatrix3make(_:_:_:_:_:_:_:_:_:).md)
  Returns a `3x3` matrix created from individual component values.
- [func GLKMatrix3MakeAndTranspose(Float, Float, Float, Float, Float, Float, Float, Float, Float) -> GLKMatrix3](glkmatrix3makeandtranspose(_:_:_:_:_:_:_:_:_:).md)
  Returns a `3x3` transposed matrix created from individual component values.
- [func GLKMatrix3MakeWithArray(UnsafeMutablePointer<Float>!) -> GLKMatrix3](glkmatrix3makewitharray(_:).md)
  Returns a `3x3` matrix created from an array of component values.
- [func GLKMatrix3MakeWithArrayAndTranspose(UnsafeMutablePointer<Float>!) -> GLKMatrix3](glkmatrix3makewitharrayandtranspose(_:).md)
  Returns a `3x3` transposed matrix created from an array of component values.
- [func GLKMatrix3MakeWithColumns(GLKVector3, GLKVector3, GLKVector3) -> GLKMatrix3](glkmatrix3makewithcolumns(_:_:_:).md)
  Returns a `3x3` matrix created from three column vectors.
- [func GLKMatrix3MakeWithRows(GLKVector3, GLKVector3, GLKVector3) -> GLKMatrix3](glkmatrix3makewithrows(_:_:_:).md)
  Returns a `3x3` matrix created from three row vectors.
- [func GLKMatrix3MakeRotation(Float, Float, Float, Float) -> GLKMatrix3](glkmatrix3makerotation(_:_:_:_:).md)
  Returns a `3x3` matrix that performs a rotation around an arbitrary vector.
- [func GLKMatrix3MakeXRotation(Float) -> GLKMatrix3](glkmatrix3makexrotation(_:).md)
  Returns a `3x3` matrix that performs a rotation around the positive x-axis.
- [func GLKMatrix3MakeYRotation(Float) -> GLKMatrix3](glkmatrix3makeyrotation(_:).md)
  Returns a `3x3` matrix that performs a rotation around the positive y-axis.
- [func GLKMatrix3MakeZRotation(Float) -> GLKMatrix3](glkmatrix3makezrotation(_:).md)
  Returns a `3x3` matrix that performs a rotation around the positive z-axis.
- [func GLKMatrix3MakeWithQuaternion(GLKQuaternion) -> GLKMatrix3](glkmatrix3makewithquaternion(_:).md)
  Returns a `3x3` matrix that performs a rotation based on a quaternion.
- [func GLKMatrix3MakeScale(Float, Float, Float) -> GLKMatrix3](glkmatrix3makescale(_:_:_:).md)
  Returns a `3x3` matrix that performs a scaling transformation.
### Working With Parts of a Matrix
- [func GLKMatrix3GetMatrix2(GLKMatrix3) -> GLKMatrix2](glkmatrix3getmatrix2(_:).md)
  Returns the upper-left `2x2` section of a `3x3` matrix.
- [func GLKMatrix3GetColumn(GLKMatrix3, Int32) -> GLKVector3](glkmatrix3getcolumn(_:_:).md)
  Retrieves a column from a `3x3` matrix.
- [func GLKMatrix3GetRow(GLKMatrix3, Int32) -> GLKVector3](glkmatrix3getrow(_:_:).md)
  Retrieves a row from a `3x3` matrix.
- [func GLKMatrix3SetColumn(GLKMatrix3, Int32, GLKVector3) -> GLKMatrix3](glkmatrix3setcolumn(_:_:_:).md)
  Returns a new `3x3` matrix with one column replaced by a new vector.
- [func GLKMatrix3SetRow(GLKMatrix3, Int32, GLKVector3) -> GLKMatrix3](glkmatrix3setrow(_:_:_:).md)
  Returns a new `3x3` matrix with one row replaced by a new vector.
### Performing Mathematical Operations on Matrices
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
- [func GLKMatrix3RotateWithVector4(GLKMatrix3, Float, GLKVector4) -> GLKMatrix3](glkmatrix3rotatewithvector4(_:_:_:).md)
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
### Performing Mathematical Operations on Vectors
- [func GLKMatrix3MultiplyVector3(GLKMatrix3, GLKVector3) -> GLKVector3](glkmatrix3multiplyvector3(_:_:).md)
  Multiplies a `3x3` matrix by a vector.
- [func GLKMatrix3MultiplyVector3Array(GLKMatrix3, UnsafeMutablePointer<GLKVector3>, Int)](glkmatrix3multiplyvector3array(_:_:_:).md)
  Multiplies a `3x3` matrix by an array of vectors.
### Data Types
- [typealias GLKMatrix2](glkmatrix2.md)
  A `2x2` matrix.
- [typealias GLKMatrix3](glkmatrix3.md)
  A `3x3` matrix stored in column-major order.
### Constants
- [let GLKMatrix3Identity: GLKMatrix3](glkmatrix3identity.md)
  A `3x3` identity matrix.

## See Also

- [class GLKMatrixStack](glkmatrixstack.md)
  An opaque type that represents a stack of 4 x 4 matrices, providing support for hierarchical transform modeling and similar tasks.
- [GLKMatrix4](glkmatrix4-pce.md)
- [GLKVector2](glkvector2-pbj.md)
- [GLKVector3](glkvector3-pbt.md)
- [GLKVector4](glkvector4-pbk.md)
- [GLKQuaternion](glkquaternion-pc6.md)
- [GLKit Math Utilities](glkit-math-utilities.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix3-pcl)*