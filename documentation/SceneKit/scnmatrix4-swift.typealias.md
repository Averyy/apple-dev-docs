# SCNMatrix4

**Framework**: SceneKit  
**Kind**: typealias  
**Role**: Type Alias

A representation of a 4 x 4 matrix.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
typealias SCNMatrix4 = CATransform3D
```

```c
typedef CATransform3D SCNMatrix4;
```

#### Discussion

SceneKit uses matrices to represent coordinate space transformations, which in turn can represent the combined position, rotation or orientation, and scale of an object in three-dimensional space.

> ❗ **Important**:  In macOS, the fields in this structure are [`CGFloat`](../CoreFoundation/cgfloat-swift.struct.md) values. In iOS, tvOS, and watchOS, these fields are `float` values.

## Topics

### Creating Transform Matrices
- [func SCNMatrix4MakeTranslation(Float, Float, Float) -> SCNMatrix4](./scnmatrix4maketranslation%28_,_,_%29.md)
  Returns a matrix describing a translation transformation.
- [func SCNMatrix4MakeRotation(Float, Float, Float, Float) -> SCNMatrix4](./scnmatrix4makerotation%28_,_,_,_%29.md)
  Returns a matrix describing a rotation transformation.
- [func SCNMatrix4MakeScale(Float, Float, Float) -> SCNMatrix4](./scnmatrix4makescale%28_,_,_%29.md)
  Returns a matrix describing a scale transformation.
### Performing Matrix Operations
- [func SCNMatrix4Translate(SCNMatrix4, Float, Float, Float) -> SCNMatrix4](./scnmatrix4translate%28_,_,_,_%29.md)
  Returns a new matrix created by concatenating the specified matrix with a translation transformation.
- [func SCNMatrix4Rotate(SCNMatrix4, Float, Float, Float, Float) -> SCNMatrix4](./scnmatrix4rotate%28_,_,_,_,_%29.md)
  Returns a new matrix created by concatenating the specified matrix with a rotation transformation.
- [func SCNMatrix4Scale(SCNMatrix4, Float, Float, Float) -> SCNMatrix4](./scnmatrix4scale%28_,_,_,_%29.md)
  Returns a new matrix created by concatenating the specified matrix with a scale transformation.
- [func SCNMatrix4Invert(SCNMatrix4) -> SCNMatrix4](./scnmatrix4invert%28_%29.md)
  Returns the inverse of the specified matrix.
- [func SCNMatrix4Mult(SCNMatrix4, SCNMatrix4) -> SCNMatrix4](./scnmatrix4mult%28_,_%29.md)
  Returns the product of two matrices.
### Converting Matrix Types
- [func SCNMatrix4FromGLKMatrix4(GLKMatrix4) -> SCNMatrix4](./scnmatrix4fromglkmatrix4%28_%29.md)
  Returns a SceneKit matrix corresponding to a GLKit matrix.
- [func SCNMatrix4ToGLKMatrix4(SCNMatrix4) -> GLKMatrix4](./scnmatrix4toglkmatrix4%28_%29.md)
  Returns a GLKit matrix corresponding to a SceneKit matrix.
### Comparing Matrices
- [func SCNMatrix4EqualToMatrix4(SCNMatrix4, SCNMatrix4) -> Bool](./scnmatrix4equaltomatrix4%28_,_%29.md)
  Returns a Boolean value that indicates whether the corresponding elements of two matrices are equal.
- [func SCNMatrix4IsIdentity(SCNMatrix4) -> Bool](./scnmatrix4isidentity%28_%29.md)
  Returns a Boolean value that indicates whether the specified matrix is equal to the identity matrix.
### Identity Constant
- [let SCNMatrix4Identity: SCNMatrix4](./scnmatrix4identity.md)
  The 4 x 4 identity matrix.
### Matrix Elements
- [var m11: Float](./scnmatrix4-swift.struct/m11.md)
- [var m12: Float](./scnmatrix4-swift.struct/m12.md)
- [var m13: Float](./scnmatrix4-swift.struct/m13.md)
- [var m14: Float](./scnmatrix4-swift.struct/m14.md)
- [var m21: Float](./scnmatrix4-swift.struct/m21.md)
- [var m22: Float](./scnmatrix4-swift.struct/m22.md)
- [var m23: Float](./scnmatrix4-swift.struct/m23.md)
- [var m24: Float](./scnmatrix4-swift.struct/m24.md)
- [var m31: Float](./scnmatrix4-swift.struct/m31.md)
- [var m32: Float](./scnmatrix4-swift.struct/m32.md)
- [var m33: Float](./scnmatrix4-swift.struct/m33.md)
- [var m34: Float](./scnmatrix4-swift.struct/m34.md)
- [var m41: Float](./scnmatrix4-swift.struct/m41.md)
- [var m42: Float](./scnmatrix4-swift.struct/m42.md)
- [var m43: Float](./scnmatrix4-swift.struct/m43.md)
- [var m44: Float](./scnmatrix4-swift.struct/m44.md)

## See Also

### Transforms and Rotations
- [struct SCNMatrix4](./scnmatrix4-swift.struct.md)
  A representation of a 4 x 4 matrix.
- [typealias SCNQuaternion](./scnquaternion.md)
  A representation of a quaternion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmatrix4-swift.typealias)*