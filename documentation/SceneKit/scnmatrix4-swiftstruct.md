# SCNMatrix4

**Framework**: SceneKit  
**Kind**: struct

A representation of a 4 x 4 matrix.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct SCNMatrix4
```

#### Overview

SceneKit uses matrices to represent coordinate space transformations, which in turn can represent the combined position, rotation or orientation, and scale of an object in three-dimensional space.

> ❗ **Important**:  In macOS, the fields in this structure are [`CGFloat`](https://developer.apple.com/documentation/CoreFoundation/CGFloat-swift.struct) values. In iOS, tvOS, and watchOS, these fields are [`Float`](https://developer.apple.com/documentation/Swift/Float) values.

## Topics

### Creating Transform Matrices
- [func SCNMatrix4MakeTranslation(Float, Float, Float) -> SCNMatrix4](scnmatrix4maketranslation(_:_:_:).md)
  Returns a matrix describing a translation transformation.
- [func SCNMatrix4MakeRotation(Float, Float, Float, Float) -> SCNMatrix4](scnmatrix4makerotation(_:_:_:_:).md)
  Returns a matrix describing a rotation transformation.
- [func SCNMatrix4MakeScale(Float, Float, Float) -> SCNMatrix4](scnmatrix4makescale(_:_:_:).md)
  Returns a matrix describing a scale transformation.
### Creating Matrices from Elements
- [init()](scnmatrix4-swift.struct/init.md)
- [init(double4x4)](scnmatrix4-swift.struct/init(_:)-bqz6.md)
- [init(_ m: double4x4)](../QuartzCore/CATransform3D/init(_:)-6euzs.md)
- [init(float4x4)](scnmatrix4-swift.struct/init(_:)-98ce8.md)
- [init(_ m: float4x4)](../QuartzCore/CATransform3D/init(_:)-6awvy.md)
- [init(m11: Float, m12: Float, m13: Float, m14: Float, m21: Float, m22: Float, m23: Float, m24: Float, m31: Float, m32: Float, m33: Float, m34: Float, m41: Float, m42: Float, m43: Float, m44: Float)](scnmatrix4-swift.struct/init(m11:m12:m13:m14:m21:m22:m23:m24:m31:m32:m33:m34:m41:m42:m43:m44:).md)
### Performing Matrix Operations
- [func SCNMatrix4Translate(SCNMatrix4, Float, Float, Float) -> SCNMatrix4](scnmatrix4translate(_:_:_:_:).md)
  Returns a new matrix created by concatenating the specified matrix with a translation transformation.
- [func SCNMatrix4Rotate(SCNMatrix4, Float, Float, Float, Float) -> SCNMatrix4](scnmatrix4rotate(_:_:_:_:_:).md)
  Returns a new matrix created by concatenating the specified matrix with a rotation transformation.
- [func SCNMatrix4Scale(SCNMatrix4, Float, Float, Float) -> SCNMatrix4](scnmatrix4scale(_:_:_:_:).md)
  Returns a new matrix created by concatenating the specified matrix with a scale transformation.
- [func SCNMatrix4Invert(SCNMatrix4) -> SCNMatrix4](scnmatrix4invert(_:).md)
  Returns the inverse of the specified matrix.
- [func SCNMatrix4Mult(SCNMatrix4, SCNMatrix4) -> SCNMatrix4](scnmatrix4mult(_:_:).md)
  Returns the product of two matrices.
### Converting Matrix Types
- [func SCNMatrix4FromGLKMatrix4(GLKMatrix4) -> SCNMatrix4](scnmatrix4fromglkmatrix4(_:).md)
  Returns a SceneKit matrix corresponding to a GLKit matrix.
- [func SCNMatrix4ToGLKMatrix4(SCNMatrix4) -> GLKMatrix4](scnmatrix4toglkmatrix4(_:).md)
  Returns a GLKit matrix corresponding to a SceneKit matrix.
### Comparing Matrices
- [func SCNMatrix4EqualToMatrix4(SCNMatrix4, SCNMatrix4) -> Bool](scnmatrix4equaltomatrix4(_:_:).md)
  Returns a Boolean value that indicates whether the corresponding elements of two matrices are equal.
- [func SCNMatrix4IsIdentity(SCNMatrix4) -> Bool](scnmatrix4isidentity(_:).md)
  Returns a Boolean value that indicates whether the specified matrix is equal to the identity matrix.
### Identity Constant
- [let SCNMatrix4Identity: SCNMatrix4](scnmatrix4identity.md)
  The 4 x 4 identity matrix.
### Matrix Elements
- [var m11: Float](scnmatrix4-swift.struct/m11.md)
- [var m12: Float](scnmatrix4-swift.struct/m12.md)
- [var m13: Float](scnmatrix4-swift.struct/m13.md)
- [var m14: Float](scnmatrix4-swift.struct/m14.md)
- [var m21: Float](scnmatrix4-swift.struct/m21.md)
- [var m22: Float](scnmatrix4-swift.struct/m22.md)
- [var m23: Float](scnmatrix4-swift.struct/m23.md)
- [var m24: Float](scnmatrix4-swift.struct/m24.md)
- [var m31: Float](scnmatrix4-swift.struct/m31.md)
- [var m32: Float](scnmatrix4-swift.struct/m32.md)
- [var m33: Float](scnmatrix4-swift.struct/m33.md)
- [var m34: Float](scnmatrix4-swift.struct/m34.md)
- [var m41: Float](scnmatrix4-swift.struct/m41.md)
- [var m42: Float](scnmatrix4-swift.struct/m42.md)
- [var m43: Float](scnmatrix4-swift.struct/m43.md)
- [var m44: Float](scnmatrix4-swift.struct/m44.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias SCNMatrix4](scnmatrix4-swift.typealias.md)
  A representation of a 4 x 4 matrix.
- [typealias SCNQuaternion](scnquaternion.md)
  A representation of a quaternion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmatrix4-swift.struct)*