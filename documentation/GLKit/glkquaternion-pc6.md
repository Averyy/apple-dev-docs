# GLKQuaternion

**Framework**: GLKit

#### Overview

The `GLKQuaternion` type defines a structure that represents a quaternion. A quaternion is defined by a scalar component `s` and an XYZ vector `v`. Quaternions are often used in graphics programming as a compact representation of a rotation of an object in three dimensions.

The functions that manipulate `GLKQuaternion` structures treat the inputs as immutable, instead returning a new quaternion that represent the results of the operation.

## Topics

### Creating Quaternions
- [func GLKQuaternionMake(Float, Float, Float, Float) -> GLKQuaternion](glkquaternionmake(_:_:_:_:).md)
  Returns a quaternion created from its separate components.
- [func GLKQuaternionMakeWithArray(UnsafeMutablePointer<Float>!) -> GLKQuaternion](glkquaternionmakewitharray(_:).md)
  Returns a quaternion created from an array of components.
- [func GLKQuaternionMakeWithVector3(GLKVector3, Float) -> GLKQuaternion](glkquaternionmakewithvector3(_:_:).md)
  Returns a quaternion created from a vector and a scalar.
- [func GLKQuaternionMakeWithAngleAndAxis(Float, Float, Float, Float) -> GLKQuaternion](glkquaternionmakewithangleandaxis(_:_:_:_:).md)
  Creates a quaternion that represents a rotation around an axis.
- [func GLKQuaternionMakeWithAngleAndVector3Axis(Float, GLKVector3) -> GLKQuaternion](glkquaternionmakewithangleandvector3axis(_:_:).md)
  Creates a quaternion that represents a rotation around an axis.
- [func GLKQuaternionMakeWithMatrix3(GLKMatrix3) -> GLKQuaternion](glkquaternionmakewithmatrix3(_:).md)
  Creates a quaternion from a rotation matrix.
- [func GLKQuaternionMakeWithMatrix4(GLKMatrix4) -> GLKQuaternion](glkquaternionmakewithmatrix4(_:).md)
  Creates a quaternion from a rotation matrix.
### Retrieving Information About a Quaternion
- [func GLKQuaternionLength(GLKQuaternion) -> Float](glkquaternionlength(_:).md)
  Returns the length of a quaternion.
- [func GLKQuaternionAxis(GLKQuaternion) -> GLKVector3](glkquaternionaxis(_:).md)
  Returns the axis of rotation of a quaternion.
- [func GLKQuaternionAngle(GLKQuaternion) -> Float](glkquaternionangle(_:).md)
  Returns the rotation angle of a quaternion.
### Performing Mathematical Operations on Quaternions
- [func GLKQuaternionNormalize(GLKQuaternion) -> GLKQuaternion](glkquaternionnormalize(_:).md)
  Returns a normalized version of a quaternion.
- [func GLKQuaternionInvert(GLKQuaternion) -> GLKQuaternion](glkquaternioninvert(_:).md)
  Returns an inverse of a quaternion.
- [func GLKQuaternionConjugate(GLKQuaternion) -> GLKQuaternion](glkquaternionconjugate(_:).md)
  Returns the conjugate of a quaternion.
- [func GLKQuaternionAdd(GLKQuaternion, GLKQuaternion) -> GLKQuaternion](glkquaternionadd(_:_:).md)
  Returns the sum of two quaternions.
- [func GLKQuaternionSubtract(GLKQuaternion, GLKQuaternion) -> GLKQuaternion](glkquaternionsubtract(_:_:).md)
  Returns the difference between two quaternions.
- [func GLKQuaternionMultiply(GLKQuaternion, GLKQuaternion) -> GLKQuaternion](glkquaternionmultiply(_:_:).md)
  Returns the product of two quaternions.
- [func GLKQuaternionSlerp(GLKQuaternion, GLKQuaternion, Float) -> GLKQuaternion](glkquaternionslerp(_:_:_:).md)
  Returns the spherical linear interpolation of two quaternions.
### Applying Quaternions to Vectors
- [func GLKQuaternionRotateVector3(GLKQuaternion, GLKVector3) -> GLKVector3](glkquaternionrotatevector3(_:_:).md)
  Returns a new vector that is calculated by applying a quaternion rotation to a vector.
- [func GLKQuaternionRotateVector3Array(GLKQuaternion, UnsafeMutablePointer<GLKVector3>, Int)](glkquaternionrotatevector3array(_:_:_:).md)
  Applies a quaternion rotation to an array of vectors.
- [func GLKQuaternionRotateVector4(GLKQuaternion, GLKVector4) -> GLKVector4](glkquaternionrotatevector4(_:_:).md)
  Returns a new vector calculated by applying a quaternion rotation to a vector.
- [func GLKQuaternionRotateVector4Array(GLKQuaternion, UnsafeMutablePointer<GLKVector4>, Int)](glkquaternionrotatevector4array(_:_:_:).md)
  Applies a quaternion rotation to an array of vectors.
### Data Types
- [typealias GLKQuaternion](glkquaternion.md)
  A representation of a quaternion.
### Constants
- [let GLKQuaternionIdentity: GLKQuaternion](glkquaternionidentity.md)
  An identity quaternion.

## See Also

- [class GLKMatrixStack](glkmatrixstack.md)
  An opaque type that represents a stack of 4 x 4 matrices, providing support for hierarchical transform modeling and similar tasks.
- [GLKMatrix3](glkmatrix3-pcl.md)
- [GLKMatrix4](glkmatrix4-pce.md)
- [GLKVector2](glkvector2-pbj.md)
- [GLKVector3](glkvector3-pbt.md)
- [GLKVector4](glkvector4-pbk.md)
- [GLKit Math Utilities](glkit-math-utilities.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkquaternion-pc6)*