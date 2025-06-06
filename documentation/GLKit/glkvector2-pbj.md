# GLKVector2

**Framework**: GLKit

#### Overview

The `GLKVector2` type defines a `2`-component floating-point vector as well as many mathematical operations commonly used to manipulate vectors. Graphics programming uses vectors extensively to represent positions, colors and other data structures.

The functions that manipulate `GLKVector2` structures treat the inputs as immutable, instead returning a new vector that represent the results of the operation.

## Topics

### Creating Vectors
- [func GLKVector2Make(Float, Float) -> GLKVector2](glkvector2make(_:_:).md)
  Returns a new two-component vector created from individual component values.
- [func GLKVector2MakeWithArray(UnsafeMutablePointer<Float>!) -> GLKVector2](glkvector2makewitharray(_:).md)
  Returns a new two-component vector created from an array of components.
### Retrieving Information About a Vector
- [func GLKVector2Length(GLKVector2) -> Float](glkvector2length(_:).md)
  Returns the length of a vector.
- [func GLKVector2Distance(GLKVector2, GLKVector2) -> Float](glkvector2distance(_:_:).md)
  Returns the distance between two points.
### Mathematical Operations Performed on Vectors
- [func GLKVector2Negate(GLKVector2) -> GLKVector2](glkvector2negate(_:).md)
  Returns a new vector created by negating the component values of another vector.
- [func GLKVector2Normalize(GLKVector2) -> GLKVector2](glkvector2normalize(_:).md)
  Returns a new vector created by normalizing an input vector to a length of `1.0`.
- [func GLKVector2AddScalar(GLKVector2, Float) -> GLKVector2](glkvector2addscalar(_:_:).md)
  Returns a new vector created by adding a scalar value to each component of a vector.
- [func GLKVector2SubtractScalar(GLKVector2, Float) -> GLKVector2](glkvector2subtractscalar(_:_:).md)
  Returns a new vector created by subtracting a scalar value from each component of a vector.
- [func GLKVector2MultiplyScalar(GLKVector2, Float) -> GLKVector2](glkvector2multiplyscalar(_:_:).md)
  Returns a new vector created by multiplying each component of a vector by a scalar value.
- [func GLKVector2DivideScalar(GLKVector2, Float) -> GLKVector2](glkvector2dividescalar(_:_:).md)
  Returns a new vector created by dividing each component of a vector by a scalar value.
- [func GLKVector2Add(GLKVector2, GLKVector2) -> GLKVector2](glkvector2add(_:_:).md)
  Returns the sum of two vectors.
- [func GLKVector2Subtract(GLKVector2, GLKVector2) -> GLKVector2](glkvector2subtract(_:_:).md)
  Returns the difference between two vectors.
- [func GLKVector2Multiply(GLKVector2, GLKVector2) -> GLKVector2](glkvector2multiply(_:_:).md)
  Returns a new vector created by multiplying one vector by another.
- [func GLKVector2Divide(GLKVector2, GLKVector2) -> GLKVector2](glkvector2divide(_:_:).md)
  Returns a new vector created by dividing one vector by another.
- [func GLKVector2DotProduct(GLKVector2, GLKVector2) -> Float](glkvector2dotproduct(_:_:).md)
  Returns the dot product of two vectors.
- [func GLKVector2Lerp(GLKVector2, GLKVector2, Float) -> GLKVector2](glkvector2lerp(_:_:_:).md)
  Returns a new vector created by linearly interpreting between two vectors.
- [func GLKVector2Project(GLKVector2, GLKVector2) -> GLKVector2](glkvector2project(_:_:).md)
  Returns a new vector created by projecting a vector onto another vector
- [func GLKVector2Maximum(GLKVector2, GLKVector2) -> GLKVector2](glkvector2maximum(_:_:).md)
  Returns a new vector whose component value at each position is the largest component value at the same position of the two source vectors.
- [func GLKVector2Minimum(GLKVector2, GLKVector2) -> GLKVector2](glkvector2minimum(_:_:).md)
  Returns a new vector whose component value at each position is the smallest component value at the same position of the two source vectors.
### Comparison Operations
- [func GLKVector2AllEqualToScalar(GLKVector2, Float) -> Bool](glkvector2allequaltoscalar(_:_:).md)
  Returns a Boolean value that states whether all the components of the source vector are equal to a scalar value.
- [func GLKVector2AllEqualToVector2(GLKVector2, GLKVector2) -> Bool](glkvector2allequaltovector2(_:_:).md)
  Returns a Boolean value that indicates whether each component of the first vector is equal to the corresponding component of a second vector.
- [func GLKVector2AllGreaterThanOrEqualToScalar(GLKVector2, Float) -> Bool](glkvector2allgreaterthanorequaltoscalar(_:_:).md)
  Returns a Boolean value that states whether all the components of the source vector are greater than or equal to a scalar value.
- [func GLKVector2AllGreaterThanOrEqualToVector2(GLKVector2, GLKVector2) -> Bool](glkvector2allgreaterthanorequaltovector2(_:_:).md)
  Returns a Boolean value that indicates whether each component of the first vector is greater than or equal to the corresponding component of a second vector.
- [func GLKVector2AllGreaterThanScalar(GLKVector2, Float) -> Bool](glkvector2allgreaterthanscalar(_:_:).md)
  Returns a Boolean value that states whether all the components of the source vector are greater than a scalar value.
- [func GLKVector2AllGreaterThanVector2(GLKVector2, GLKVector2) -> Bool](glkvector2allgreaterthanvector2(_:_:).md)
  Returns a Boolean value that indicates whether each component of the first vector is greater than the corresponding component of a second vector.
### Data Types
- [typealias GLKVector2](glkvector2.md)
  A representation of a 2-component vector.

## See Also

- [class GLKMatrixStack](glkmatrixstack.md)
  An opaque type that represents a stack of 4 x 4 matrices, providing support for hierarchical transform modeling and similar tasks.
- [GLKMatrix3](glkmatrix3-pcl.md)
- [GLKMatrix4](glkmatrix4-pce.md)
- [GLKVector3](glkvector3-pbt.md)
- [GLKVector4](glkvector4-pbk.md)
- [GLKQuaternion](glkquaternion-pc6.md)
- [GLKit Math Utilities](glkit-math-utilities.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkvector2-pbj)*