# GLKMatrix3MultiplyVector3(_:_:)

**Framework**: GLKit  
**Kind**: func

Multiplies a `3x3` matrix by a vector.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKMatrix3MultiplyVector3(_ matrixLeft: GLKMatrix3, _ vectorRight: GLKVector3) -> GLKVector3
```

#### Return Value

A new vector created by multiplying the matrix by the vector.

## Parameters

- `matrixLeft`: The matrix multiplicand.
- `vectorRight`: The vector multiplier.

## See Also

- [func GLKMatrix3MultiplyVector3Array(GLKMatrix3, UnsafeMutablePointer<GLKVector3>, Int)](glkmatrix3multiplyvector3array(_:_:_:).md)
  Multiplies a `3x3` matrix by an array of vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix3multiplyvector3(_:_:))*