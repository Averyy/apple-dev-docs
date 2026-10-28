# GLKVector3

**Framework**: GLKit  
**Role**: API Collection

## Overview

The `GLKVector3` type defines a `3`-component floating-point vector as well as many mathematical operations commonly used to manipulate vectors. Graphics programming uses vectors extensively to represent positions, normals, colors and other data structures.

The functions that manipulate `GLKVector3` structures treat the inputs as immutable, instead returning a new vector that represent the results of the operation.

## Topics

### Creating Vectors
- [func GLKVector3Make(Float, Float, Float) -> GLKVector3](./glkvector3make%28_,_,_%29.md)
  Returns a new three-component vector created from individual component values.
- [func GLKVector3MakeWithArray(UnsafeMutablePointer<Float>!) -> GLKVector3](./glkvector3makewitharray%28_%29.md)
  Returns a new three-component vector created from an array of components.
### Retrieving Information About a Vector
- [func GLKVector3Length(GLKVector3) -> Float](./glkvector3length%28_%29.md)
  Returns the length of a vector.
- [func GLKVector3Distance(GLKVector3, GLKVector3) -> Float](./glkvector3distance%28_,_%29.md)
  Returns the distance between two points.
### Mathematical Operations Performed on Vectors
- [func GLKVector3Negate(GLKVector3) -> GLKVector3](./glkvector3negate%28_%29.md)
  Returns a new vector created by negating the component values of another vector.
- [func GLKVector3Normalize(GLKVector3) -> GLKVector3](./glkvector3normalize%28_%29.md)
  Returns a new vector created by normalizing the input vector to a length of `1.0`.
- [func GLKVector3AddScalar(GLKVector3, Float) -> GLKVector3](./glkvector3addscalar%28_,_%29.md)
  Returns a new vector created by adding a scalar value to each component of a vector.
- [func GLKVector3SubtractScalar(GLKVector3, Float) -> GLKVector3](./glkvector3subtractscalar%28_,_%29.md)
  Returns a new vector created by subtracting a scalar value from each component of a vector.
- [func GLKVector3MultiplyScalar(GLKVector3, Float) -> GLKVector3](./glkvector3multiplyscalar%28_,_%29.md)
  Returns a new vector created by multiplying each component of a vector by a scalar value.
- [func GLKVector3DivideScalar(GLKVector3, Float) -> GLKVector3](./glkvector3dividescalar%28_,_%29.md)
  Returns a new vector created by dividing each component of a vector by a scalar value.
- [func GLKVector3Add(GLKVector3, GLKVector3) -> GLKVector3](./glkvector3add%28_,_%29.md)
  Returns the sum of two vectors.
- [func GLKVector3Subtract(GLKVector3, GLKVector3) -> GLKVector3](./glkvector3subtract%28_,_%29.md)
  Returns the difference between two vectors.
- [func GLKVector3Multiply(GLKVector3, GLKVector3) -> GLKVector3](./glkvector3multiply%28_,_%29.md)
  Returns the product of two vectors.
- [func GLKVector3Divide(GLKVector3, GLKVector3) -> GLKVector3](./glkvector3divide%28_,_%29.md)
  Returns a new vector created by dividing one vector by another.
- [func GLKVector3DotProduct(GLKVector3, GLKVector3) -> Float](./glkvector3dotproduct%28_,_%29.md)
  Returns the dot product of two vectors.
- [func GLKVector3CrossProduct(GLKVector3, GLKVector3) -> GLKVector3](./glkvector3crossproduct%28_,_%29.md)
  Returns the cross product of two vectors.
- [func GLKVector3Lerp(GLKVector3, GLKVector3, Float) -> GLKVector3](./glkvector3lerp%28_,_,_%29.md)
  Returns a new vector created by linearly interpreting between two vectors.
- [func GLKVector3Project(GLKVector3, GLKVector3) -> GLKVector3](./glkvector3project%28_,_%29.md)
  Returns a new vector created by projecting a vector onto another vector.
- [func GLKVector3Maximum(GLKVector3, GLKVector3) -> GLKVector3](./glkvector3maximum%28_,_%29.md)
  Returns a new vector whose component value at each position is the largest component value at the same position in the source vectors.
- [func GLKVector3Minimum(GLKVector3, GLKVector3) -> GLKVector3](./glkvector3minimum%28_,_%29.md)
  Returns a new vector whose component value at each position is the smallest component value at the same position in the source vectors.
### Comparison Operations
- [func GLKVector3AllEqualToScalar(GLKVector3, Float) -> Bool](./glkvector3allequaltoscalar%28_,_%29.md)
  Returns a Boolean value that states whether all the components of the source vector are equal to a scalar value.
- [func GLKVector3AllEqualToVector3(GLKVector3, GLKVector3) -> Bool](./glkvector3allequaltovector3%28_,_%29.md)
  Returns a Boolean value that indicates whether each component of the first vector is equal to the corresponding component of a second vector.
- [func GLKVector3AllGreaterThanOrEqualToScalar(GLKVector3, Float) -> Bool](./glkvector3allgreaterthanorequaltoscalar%28_,_%29.md)
  Returns a Boolean value that states whether all the components of the source vector are greater than or equal to a scalar value.
- [func GLKVector3AllGreaterThanOrEqualToVector3(GLKVector3, GLKVector3) -> Bool](./glkvector3allgreaterthanorequaltovector3%28_,_%29.md)
  Returns a Boolean value that indicates whether each component of the first vector is greater than or equal to the corresponding component of a second vector.
- [func GLKVector3AllGreaterThanScalar(GLKVector3, Float) -> Bool](./glkvector3allgreaterthanscalar%28_,_%29.md)
  Returns a Boolean value that states whether all the components of the source vector are greater than a scalar value.
- [func GLKVector3AllGreaterThanVector3(GLKVector3, GLKVector3) -> Bool](./glkvector3allgreaterthanvector3%28_,_%29.md)
  Returns a Boolean value that indicates whether each component of the first vector is greater than the corresponding component of a second vector.
### Data Types
- [typealias GLKVector3](./glkvector3.md)
  A representation of a 3-component vector.

## See Also

### Math Utilties
- [class GLKMatrixStack](./glkmatrixstack.md)
  An opaque type that represents a stack of 4 x 4 matrices, providing support for hierarchical transform modeling and similar tasks.
- [GLKMatrix3](./glkmatrix3-pcl.md)
- [GLKMatrix4](./glkmatrix4-pce.md)
- [GLKVector2](./glkvector2-pbj.md)
- [GLKVector4](./glkvector4-pbk.md)
- [GLKQuaternion](./glkquaternion-pc6.md)
- [GLKit Math Utilities](./glkit-math-utilities.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkvector3-pbt)*