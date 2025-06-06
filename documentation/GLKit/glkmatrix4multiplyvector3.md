# GLKMatrix4MultiplyVector3(_:_:)

**Framework**: GLKit  
**Kind**: func

Multiplies a `4x4` matrix by a `3`-component vector.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrix4MultiplyVector3(_ matrixLeft: GLKMatrix4, _ vectorRight: GLKVector3) -> GLKVector3
```

#### Return Value

A new vector created by multiplying the matrix by the vector.

#### Discussion

The input vector is treated as it were a 4-component vector with a `w`-component of `0.0`.

## Parameters

- `matrixLeft`: The matrix multiplicand.
- `vectorRight`: The vector multiplier.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix4multiplyvector3(_:_:))*