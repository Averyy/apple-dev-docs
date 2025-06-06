# GLKMatrix4MultiplyVector3ArrayWithTranslation(_:_:_:)

**Framework**: GLKit  
**Kind**: func

Multiplies a `4x4` matrix by an array of `3`-component vectors, applying translation.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrix4MultiplyVector3ArrayWithTranslation(_ matrix: GLKMatrix4, _ vectors: UnsafeMutablePointer<GLKVector3>, _ vectorCount: Int)
```

#### Discussion

The input vectors are treated as they were 4-component vectors with a `w`-component of `1.0`.

## Parameters

- `matrix`: The matrix multiplicand.
- `vectors`: On entry, an array of input vectors. On return, an array of output vectors.
- `vectorCount`: The number of vectors in the array.

## See Also

- [func GLKMatrix4MultiplyVector3(GLKMatrix4, GLKVector3) -> GLKVector3](glkmatrix4multiplyvector3(_:_:).md)
  Multiplies a `4x4` matrix by a `3`-component vector.
- [func GLKMatrix4MultiplyVector3Array(GLKMatrix4, UnsafeMutablePointer<GLKVector3>, Int)](glkmatrix4multiplyvector3array(_:_:_:).md)
  Multiplies a `4x4` matrix by an array of `3`-component vectors.
- [func GLKMatrix4MultiplyVector3WithTranslation(GLKMatrix4, GLKVector3) -> GLKVector3](glkmatrix4multiplyvector3withtranslation(_:_:).md)
  Multiplies a `4x4` matrix by a `3`-component vector, applying translation.
- [func GLKMatrix4MultiplyVector4(GLKMatrix4, GLKVector4) -> GLKVector4](glkmatrix4multiplyvector4(_:_:).md)
  Multiplies a `4x4` matrix by a `4`-component vector.
- [func GLKMatrix4MultiplyVector4Array(GLKMatrix4, UnsafeMutablePointer<GLKVector4>, Int)](glkmatrix4multiplyvector4array(_:_:_:).md)
  Multiplies a `4x4` matrix by an array of `4`-component vectors.
- [func GLKMatrix4MultiplyAndProjectVector3(GLKMatrix4, GLKVector3) -> GLKVector3](glkmatrix4multiplyandprojectvector3(_:_:).md)
  Multiplies a `4x4` matrix by a position vector to create a vector in homogenous coordinates, then projects the result to a `3`-component vector.
- [func GLKMatrix4MultiplyAndProjectVector3Array(GLKMatrix4, UnsafeMutablePointer<GLKVector3>, Int)](glkmatrix4multiplyandprojectvector3array(_:_:_:).md)
  Multiplies a `4x4` matrix by an array of `3`-component vectors. Each result is projected back to `3`-component vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix4multiplyvector3arraywithtranslation(_:_:_:))*