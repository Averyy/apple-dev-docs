# GLKMatrix4

**Framework**: GLKit

#### Overview

The [`GLKMatrix4`](glkmatrix4.md) type defines a `4x4` floating-point matrix as well as many mathematical operations commonly used to manipulate matrices. 3D graphics programming uses matrices extensively as a convenient way to represent a graphical transformation between different coordinate systems. These transformations include translation, scaling, rotation and projection; through matrix multiplication, multiple transformations can be concatenated into a single transformation matrix.

The functions that manipulate [`GLKMatrix4`](glkmatrix4.md) structures treat the inputs as immutable, instead returning a new matrix that represent the results of the operation.

## Topics

### Creating Matrices
- [func GLKMatrix4Make(Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float) -> GLKMatrix4](glkmatrix4make(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Returns a `4x4` matrix created from individual component values.
- [func GLKMatrix4MakeAndTranspose(Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float) -> GLKMatrix4](glkmatrix4makeandtranspose(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Returns a `4x4` transposed matrix created from individual component values.
- [func GLKMatrix4MakeWithArray(UnsafeMutablePointer<Float>!) -> GLKMatrix4](glkmatrix4makewitharray(_:).md)
  Returns a `4x4` matrix created from an array of component values.
- [func GLKMatrix4MakeWithArrayAndTranspose(UnsafeMutablePointer<Float>!) -> GLKMatrix4](glkmatrix4makewitharrayandtranspose(_:).md)
  Returns a `4x4` transposed matrix created from an array of component values.
- [func GLKMatrix4MakeWithColumns(GLKVector4, GLKVector4, GLKVector4, GLKVector4) -> GLKMatrix4](glkmatrix4makewithcolumns(_:_:_:_:).md)
  Returns a `4x4` matrix created from four column vectors.
- [func GLKMatrix4MakeWithRows(GLKVector4, GLKVector4, GLKVector4, GLKVector4) -> GLKMatrix4](glkmatrix4makewithrows(_:_:_:_:).md)
  Returns a `4x4` matrix created from four row vectors.
- [func GLKMatrix4MakeRotation(Float, Float, Float, Float) -> GLKMatrix4](glkmatrix4makerotation(_:_:_:_:).md)
  Returns a `4x4` matrix that performs a rotation around an arbitrary vector.
- [func GLKMatrix4MakeXRotation(Float) -> GLKMatrix4](glkmatrix4makexrotation(_:).md)
  Returns a `4x4` matrix that performs a rotation around the positive x-axis.
- [func GLKMatrix4MakeYRotation(Float) -> GLKMatrix4](glkmatrix4makeyrotation(_:).md)
  Returns a `4x4` matrix that performs a rotation around the positive y-axis.
- [func GLKMatrix4MakeZRotation(Float) -> GLKMatrix4](glkmatrix4makezrotation(_:).md)
  Returns a `4x4` matrix that performs a rotation around the positive z-axis.
- [func GLKMatrix4MakeWithQuaternion(GLKQuaternion) -> GLKMatrix4](glkmatrix4makewithquaternion(_:).md)
  Returns a `4x4` matrix that performs a rotation based on a quaternion.
- [func GLKMatrix4MakeScale(Float, Float, Float) -> GLKMatrix4](glkmatrix4makescale(_:_:_:).md)
  Returns a `4x4` matrix that performs a scaling transformation.
- [func GLKMatrix4MakeTranslation(Float, Float, Float) -> GLKMatrix4](glkmatrix4maketranslation(_:_:_:).md)
  Returns a `4x4` matrix that performs a translation.
- [func GLKMatrix4MakeLookAt(Float, Float, Float, Float, Float, Float, Float, Float, Float) -> GLKMatrix4](glkmatrix4makelookat(_:_:_:_:_:_:_:_:_:).md)
  Returns a `4x4` matrix that transforms world coordinates to eye coordinates.
- [func GLKMatrix4MakeOrtho(Float, Float, Float, Float, Float, Float) -> GLKMatrix4](glkmatrix4makeortho(_:_:_:_:_:_:).md)
  Returns a `4x4` orthographic projection matrix.
- [func GLKMatrix4MakePerspective(Float, Float, Float, Float) -> GLKMatrix4](glkmatrix4makeperspective(_:_:_:_:).md)
  Returns a `4x4` perspective projection matrix.
- [func GLKMatrix4MakeFrustum(Float, Float, Float, Float, Float, Float) -> GLKMatrix4](glkmatrix4makefrustum(_:_:_:_:_:_:).md)
  Returns a `4x4` perspective projection matrix.
### Working With Parts of a Matrix
- [func GLKMatrix4GetMatrix2(GLKMatrix4) -> GLKMatrix2](glkmatrix4getmatrix2(_:).md)
  Returns the upper-left `2x2` section of a `4x4` matrix.
- [func GLKMatrix4GetMatrix3(GLKMatrix4) -> GLKMatrix3](glkmatrix4getmatrix3(_:).md)
  Returns the upper-left `3x3` section of a `4x4` matrix.
- [func GLKMatrix4GetColumn(GLKMatrix4, Int32) -> GLKVector4](glkmatrix4getcolumn(_:_:).md)
  Retrieves a column from a `4x4` matrix.
- [func GLKMatrix4GetRow(GLKMatrix4, Int32) -> GLKVector4](glkmatrix4getrow(_:_:).md)
  Retrieves a row from a `4x4` matrix.
- [func GLKMatrix4SetColumn(GLKMatrix4, Int32, GLKVector4) -> GLKMatrix4](glkmatrix4setcolumn(_:_:_:).md)
  Returns a new `4x4` matrix with one column replaced by a new vector.
- [func GLKMatrix4SetRow(GLKMatrix4, Int32, GLKVector4) -> GLKMatrix4](glkmatrix4setrow(_:_:_:).md)
  Returns a new `4x4` matrix with one row replaced by a new vector.
### Performing Mathematical Operations on Matrices
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
- [func GLKMatrix4TranslateWithVector3(GLKMatrix4, GLKVector3) -> GLKMatrix4](glkmatrix4translatewithvector3(_:_:).md)
  Returns a new `4x4` matrix created by concatenating a matrix with a translation transform defined by a vector.
- [func GLKMatrix4TranslateWithVector4(GLKMatrix4, GLKVector4) -> GLKMatrix4](glkmatrix4translatewithvector4(_:_:).md)
  Returns a new `4x4` matrix created by concatenating a matrix with a translation transform defined by a vector.
- [func GLKMatrix4Add(GLKMatrix4, GLKMatrix4) -> GLKMatrix4](glkmatrix4add(_:_:).md)
  Returns a new `4x4` matrix created by performing a component-wise addition of two matrices.
- [func GLKMatrix4Subtract(GLKMatrix4, GLKMatrix4) -> GLKMatrix4](glkmatrix4subtract(_:_:).md)
  Returns a new `4x4` matrix created by performing a component-wise subtraction of two matrices.
### Performing Mathematical Operations on Vectors
- [func GLKMatrix4MultiplyVector3(GLKMatrix4, GLKVector3) -> GLKVector3](glkmatrix4multiplyvector3(_:_:).md)
  Multiplies a `4x4` matrix by a `3`-component vector.
- [func GLKMatrix4MultiplyVector3Array(GLKMatrix4, UnsafeMutablePointer<GLKVector3>, Int)](glkmatrix4multiplyvector3array(_:_:_:).md)
  Multiplies a `4x4` matrix by an array of `3`-component vectors.
- [func GLKMatrix4MultiplyVector3WithTranslation(GLKMatrix4, GLKVector3) -> GLKVector3](glkmatrix4multiplyvector3withtranslation(_:_:).md)
  Multiplies a `4x4` matrix by a `3`-component vector, applying translation.
- [func GLKMatrix4MultiplyVector3ArrayWithTranslation(GLKMatrix4, UnsafeMutablePointer<GLKVector3>, Int)](glkmatrix4multiplyvector3arraywithtranslation(_:_:_:).md)
  Multiplies a `4x4` matrix by an array of `3`-component vectors, applying translation.
- [func GLKMatrix4MultiplyVector4(GLKMatrix4, GLKVector4) -> GLKVector4](glkmatrix4multiplyvector4(_:_:).md)
  Multiplies a `4x4` matrix by a `4`-component vector.
- [func GLKMatrix4MultiplyVector4Array(GLKMatrix4, UnsafeMutablePointer<GLKVector4>, Int)](glkmatrix4multiplyvector4array(_:_:_:).md)
  Multiplies a `4x4` matrix by an array of `4`-component vectors.
- [func GLKMatrix4MultiplyAndProjectVector3(GLKMatrix4, GLKVector3) -> GLKVector3](glkmatrix4multiplyandprojectvector3(_:_:).md)
  Multiplies a `4x4` matrix by a position vector to create a vector in homogenous coordinates, then projects the result to a `3`-component vector.
- [func GLKMatrix4MultiplyAndProjectVector3Array(GLKMatrix4, UnsafeMutablePointer<GLKVector3>, Int)](glkmatrix4multiplyandprojectvector3array(_:_:_:).md)
  Multiplies a `4x4` matrix by an array of `3`-component vectors. Each result is projected back to `3`-component vector.
### Data Types
- [typealias GLKMatrix4](glkmatrix4.md)
  A `4x4` matrix.
### Constants
- [let GLKMatrix4Identity: GLKMatrix4](glkmatrix4identity.md)
  A `4x4` identity matrix.

## See Also

- [class GLKMatrixStack](glkmatrixstack.md)
  An opaque type that represents a stack of 4 x 4 matrices, providing support for hierarchical transform modeling and similar tasks.
- [GLKMatrix3](glkmatrix3-pcl.md)
- [GLKVector2](glkvector2-pbj.md)
- [GLKVector3](glkvector3-pbt.md)
- [GLKVector4](glkvector4-pbk.md)
- [GLKQuaternion](glkquaternion-pc6.md)
- [GLKit Math Utilities](glkit-math-utilities.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix4-pce)*