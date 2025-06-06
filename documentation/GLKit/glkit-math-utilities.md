# GLKit Math Utilities

**Framework**: GLKit

#### Overview

Math routines without a specific type associated with them.

## Topics

### Converting Angles
- [func GLKMathDegreesToRadians(Float) -> Float](glkmathdegreestoradians(_:).md)
  Converts an angle measured in degrees to radians.
- [func GLKMathRadiansToDegrees(Float) -> Float](glkmathradianstodegrees(_:).md)
  Converts an angle measured in radians to degrees.
### Projecting Vectors
- [func GLKMathProject(GLKVector3, GLKMatrix4, GLKMatrix4, UnsafeMutablePointer<Int32>) -> GLKVector3](glkmathproject(_:_:_:_:).md)
  Projects a point in object space into the window coordinate system.
- [func GLKMathUnproject(GLKVector3, GLKMatrix4, GLKMatrix4, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Bool>?) -> GLKVector3](glkmathunproject(_:_:_:_:_:).md)
  Projects a point in view space into object space.
### Obtaining String Descriptions
- [func NSStringFromGLKMatrix2(GLKMatrix2) -> String](nsstringfromglkmatrix2(_:).md)
  Returns a string that represents the contents of a matrix.
- [func NSStringFromGLKMatrix3(GLKMatrix3) -> String](nsstringfromglkmatrix3(_:).md)
  Returns a string that represents the contents of a matrix.
- [func NSStringFromGLKMatrix4(GLKMatrix4) -> String](nsstringfromglkmatrix4(_:).md)
  Returns a string that represents the contents of a matrix.
- [func NSStringFromGLKVector2(GLKVector2) -> String](nsstringfromglkvector2(_:).md)
  Returns a string that represents the contents of a vector.
- [func NSStringFromGLKVector3(GLKVector3) -> String](nsstringfromglkvector3(_:).md)
  Returns a string that represents the contents of a vector.
- [func NSStringFromGLKVector4(GLKVector4) -> String](nsstringfromglkvector4(_:).md)
  Returns a string that represents the contents of a vector.
- [func NSStringFromGLKQuaternion(GLKQuaternion) -> String](nsstringfromglkquaternion(_:).md)
  Returns a string that represents the contents of a quaternion.

## See Also

- [class GLKMatrixStack](glkmatrixstack.md)
  An opaque type that represents a stack of 4 x 4 matrices, providing support for hierarchical transform modeling and similar tasks.
- [GLKMatrix3](glkmatrix3-pcl.md)
- [GLKMatrix4](glkmatrix4-pce.md)
- [GLKVector2](glkvector2-pbj.md)
- [GLKVector3](glkvector3-pbt.md)
- [GLKVector4](glkvector4-pbk.md)
- [GLKQuaternion](glkquaternion-pc6.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkit-math-utilities)*