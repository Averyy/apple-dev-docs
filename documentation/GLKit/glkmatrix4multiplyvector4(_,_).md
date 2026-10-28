# GLKMatrix4MultiplyVector4(_:_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Multiplies a `4x4` matrix by a `4`-component vector.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrix4MultiplyVector4(_ matrixLeft: GLKMatrix4, _ vectorRight: GLKVector4) -> GLKVector4
```

```c
static GLKVector4 GLKMatrix4MultiplyVector4(GLKMatrix4 matrixLeft, GLKVector4 vectorRight);
```

## Return Value

A new vector created by multiplying the matrix by the vector.

## Parameters

- `matrixLeft`: The matrix multiplicand.
- `vectorRight`: The vector multiplier.

## See Also

### Performing Mathematical Operations on Vectors
- [func GLKMatrix4MultiplyVector3(GLKMatrix4, GLKVector3) -> GLKVector3](./glkmatrix4multiplyvector3%28_,_%29.md)
  Multiplies a `4x4` matrix by a `3`-component vector.
- [func GLKMatrix4MultiplyVector3Array(GLKMatrix4, UnsafeMutablePointer<GLKVector3>, Int)](./glkmatrix4multiplyvector3array%28_,_,_%29.md)
  Multiplies a `4x4` matrix by an array of `3`-component vectors.
- [func GLKMatrix4MultiplyVector3WithTranslation(GLKMatrix4, GLKVector3) -> GLKVector3](./glkmatrix4multiplyvector3withtranslation%28_,_%29.md)
  Multiplies a `4x4` matrix by a `3`-component vector, applying translation.
- [func GLKMatrix4MultiplyVector3ArrayWithTranslation(GLKMatrix4, UnsafeMutablePointer<GLKVector3>, Int)](./glkmatrix4multiplyvector3arraywithtranslation%28_,_,_%29.md)
  Multiplies a `4x4` matrix by an array of `3`-component vectors, applying translation.
- [func GLKMatrix4MultiplyVector4Array(GLKMatrix4, UnsafeMutablePointer<GLKVector4>, Int)](./glkmatrix4multiplyvector4array%28_,_,_%29.md)
  Multiplies a `4x4` matrix by an array of `4`-component vectors.
- [func GLKMatrix4MultiplyAndProjectVector3(GLKMatrix4, GLKVector3) -> GLKVector3](./glkmatrix4multiplyandprojectvector3%28_,_%29.md)
  Multiplies a `4x4` matrix by a position vector to create a vector in homogenous coordinates, then projects the result to a `3`-component vector.
- [func GLKMatrix4MultiplyAndProjectVector3Array(GLKMatrix4, UnsafeMutablePointer<GLKVector3>, Int)](./glkmatrix4multiplyandprojectvector3array%28_,_,_%29.md)
  Multiplies a `4x4` matrix by an array of `3`-component vectors. Each result is projected back to `3`-component vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix4multiplyvector4(_:_:))*