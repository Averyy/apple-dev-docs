# GLKVector4

**Framework**: GLKit

#### Overview

The `GLKVector4` type defines a `4`-component floating-point vector as well as many mathematical operations commonly used to manipulate vectors. Graphics programming uses vectors extensively to represent positions, normals, colors and other data structures.

The functions that manipulate `GLKVector4` structures treat the inputs as immutable, instead returning a new vector that represent the results of the operation.

## Topics

### Creating Vectors
- [func GLKVector4Make(Float, Float, Float, Float) -> GLKVector4](glkvector4make(_:_:_:_:).md)
  Returns a new four-component vector created from individual component values.
- [func GLKVector4MakeWithArray(UnsafeMutablePointer<Float>!) -> GLKVector4](glkvector4makewitharray(_:).md)
  Returns a new four-component vector created from an array of components.
- [func GLKVector4MakeWithVector3(GLKVector3, Float) -> GLKVector4](glkvector4makewithvector3(_:_:).md)
  Returns a new four-component vector created by combining a three-component vector with a scalar value.
### Retrieving Information About a Vector
- [func GLKVector4Length(GLKVector4) -> Float](glkvector4length(_:).md)
  Returns the length of a vector.
- [func GLKVector4Distance(GLKVector4, GLKVector4) -> Float](glkvector4distance(_:_:).md)
  Returns the distance between two points.
### Mathematical Operations Performed on Vectors
- [func GLKVector4Negate(GLKVector4) -> GLKVector4](glkvector4negate(_:).md)
  Returns a new vector created by negating the component values of another vector.
- [func GLKVector4Normalize(GLKVector4) -> GLKVector4](glkvector4normalize(_:).md)
  Returns a new vector created by normalizing an input vector to a length of `1.0`.
- [func GLKVector4AddScalar(GLKVector4, Float) -> GLKVector4](glkvector4addscalar(_:_:).md)
  Returns a new vector created by adding a scalar value to each component of a vector.
- [func GLKVector4SubtractScalar(GLKVector4, Float) -> GLKVector4](glkvector4subtractscalar(_:_:).md)
  Returns a new vector created by subtracting a scalar value from each component of a vector.
- [func GLKVector4MultiplyScalar(GLKVector4, Float) -> GLKVector4](glkvector4multiplyscalar(_:_:).md)
  Returns a new vector created by multiplying each component of a vector by a scalar value.
- [func GLKVector4DivideScalar(GLKVector4, Float) -> GLKVector4](glkvector4dividescalar(_:_:).md)
  Returns a new vector created by dividing each component of a vector by a scalar value.
- [func GLKVector4Add(GLKVector4, GLKVector4) -> GLKVector4](glkvector4add(_:_:).md)
  Returns the sum of two vectors.
- [func GLKVector4Subtract(GLKVector4, GLKVector4) -> GLKVector4](glkvector4subtract(_:_:).md)
  Returns the difference between two vectors.
- [func GLKVector4Multiply(GLKVector4, GLKVector4) -> GLKVector4](glkvector4multiply(_:_:).md)
  Returns the product of two vectors.
- [func GLKVector4Divide(GLKVector4, GLKVector4) -> GLKVector4](glkvector4divide(_:_:).md)
  Returns a new vector created by dividing one vector by another.
- [func GLKVector4DotProduct(GLKVector4, GLKVector4) -> Float](glkvector4dotproduct(_:_:).md)
  Returns the dot product of two vectors.
- [func GLKVector4CrossProduct(GLKVector4, GLKVector4) -> GLKVector4](glkvector4crossproduct(_:_:).md)
  Returns the cross product of two vectors.
- [func GLKVector4Lerp(GLKVector4, GLKVector4, Float) -> GLKVector4](glkvector4lerp(_:_:_:).md)
  Returns a new vector created by linearly interpreting between two vectors.
- [func GLKVector4Project(GLKVector4, GLKVector4) -> GLKVector4](glkvector4project(_:_:).md)
  Returns a new vector created by projecting a vector onto another vector.
- [func GLKVector4Maximum(GLKVector4, GLKVector4) -> GLKVector4](glkvector4maximum(_:_:).md)
  Returns a new vector whose component value at each position is the largest component value at the same position in the source vectors.
- [func GLKVector4Minimum(GLKVector4, GLKVector4) -> GLKVector4](glkvector4minimum(_:_:).md)
  Returns a new vector whose component value at each position is the smallest component value at the same position in the source vectors.
### Comparison Operations
- [func GLKVector4AllEqualToScalar(GLKVector4, Float) -> Bool](glkvector4allequaltoscalar(_:_:).md)
  Returns a Boolean value that states whether all the components of the source vector are equal to a scalar value.
- [func GLKVector4AllEqualToVector4(GLKVector4, GLKVector4) -> Bool](glkvector4allequaltovector4(_:_:).md)
  Returns a Boolean value that indicates whether each component of the first vector is equal to the corresponding component of a second vector.
- [func GLKVector4AllGreaterThanOrEqualToScalar(GLKVector4, Float) -> Bool](glkvector4allgreaterthanorequaltoscalar(_:_:).md)
  Returns a Boolean value that states whether all the components of the source vector are greater than or equal to a scalar value.
- [func GLKVector4AllGreaterThanOrEqualToVector4(GLKVector4, GLKVector4) -> Bool](glkvector4allgreaterthanorequaltovector4(_:_:).md)
  Returns a Boolean value that indicates whether each component of the first vector is greater than or equal to the corresponding component of a second vector.
- [func GLKVector4AllGreaterThanScalar(GLKVector4, Float) -> Bool](glkvector4allgreaterthanscalar(_:_:).md)
  Returns a Boolean value that states whether all the components of the source vector are greater than a scalar value.
- [func GLKVector4AllGreaterThanVector4(GLKVector4, GLKVector4) -> Bool](glkvector4allgreaterthanvector4(_:_:).md)
  Returns a Boolean value that indicates whether each component of the first vector is greater than the corresponding component of a second vector.
### Data Types
- [typealias GLKVector4](glkvector4.md)
  A representation of a 4-component vector.

## See Also

- [class GLKMatrixStack](glkmatrixstack.md)
  An opaque type that represents a stack of 4 x 4 matrices, providing support for hierarchical transform modeling and similar tasks.
- [GLKMatrix3](glkmatrix3-pcl.md)
- [GLKMatrix4](glkmatrix4-pce.md)
- [GLKVector2](glkvector2-pbj.md)
- [GLKVector3](glkvector3-pbt.md)
- [GLKQuaternion](glkquaternion-pc6.md)
- [GLKit Math Utilities](glkit-math-utilities.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkvector4-pbk)*