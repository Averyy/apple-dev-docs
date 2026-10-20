# GLKMatrix3MultiplyVector3Array(_:_:_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Multiplies a `3x3` matrix by an array of vectors.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrix3MultiplyVector3Array(_ matrix: GLKMatrix3, _ vectors: UnsafeMutablePointer<GLKVector3>, _ vectorCount: Int)
```

```c
static void GLKMatrix3MultiplyVector3Array(GLKMatrix3 matrix, GLKVector3 *vectors, size_t vectorCount);
```

## Parameters

- `matrix`: The matrix multiplicand.
- `vectors`: On entry, an array of input vectors. On return, an array of output vectors.
- `vectorCount`: The number of vectors in the array.

## See Also

### Performing Mathematical Operations on Vectors
- [func GLKMatrix3MultiplyVector3(GLKMatrix3, GLKVector3) -> GLKVector3](./glkmatrix3multiplyvector3%28_,_%29.md)
  Multiplies a `3x3` matrix by a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix3multiplyvector3array(_:_:_:))*