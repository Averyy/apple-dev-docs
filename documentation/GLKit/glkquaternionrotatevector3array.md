# GLKQuaternionRotateVector3Array(_:_:_:)

**Framework**: GLKit  
**Kind**: func

Applies a quaternion rotation to an array of vectors.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKQuaternionRotateVector3Array(_ quaternion: GLKQuaternion, _ vectors: UnsafeMutablePointer<GLKVector3>, _ vectorCount: Int)
```

## Parameters

- `quaternion`: A quaternion.
- `vectors`: On entry, an array of input vectors. On return, an array of output vectors.
- `vectorCount`: The number of vectors in the array.

## See Also

- [func GLKQuaternionRotateVector3(GLKQuaternion, GLKVector3) -> GLKVector3](glkquaternionrotatevector3(_:_:).md)
  Returns a new vector that is calculated by applying a quaternion rotation to a vector.
- [func GLKQuaternionRotateVector4(GLKQuaternion, GLKVector4) -> GLKVector4](glkquaternionrotatevector4(_:_:).md)
  Returns a new vector calculated by applying a quaternion rotation to a vector.
- [func GLKQuaternionRotateVector4Array(GLKQuaternion, UnsafeMutablePointer<GLKVector4>, Int)](glkquaternionrotatevector4array(_:_:_:).md)
  Applies a quaternion rotation to an array of vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkquaternionrotatevector3array(_:_:_:))*