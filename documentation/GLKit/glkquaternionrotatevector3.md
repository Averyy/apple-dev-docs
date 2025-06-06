# GLKQuaternionRotateVector3(_:_:)

**Framework**: GLKit  
**Kind**: func

Returns a new vector that is calculated by applying a quaternion rotation to a vector.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKQuaternionRotateVector3(_ quaternion: GLKQuaternion, _ vector: GLKVector3) -> GLKVector3
```

#### Return Value

A new vector.

## Parameters

- `quaternion`: A quaternion.
- `vector`: A source vector.

## See Also

- [func GLKQuaternionRotateVector3Array(GLKQuaternion, UnsafeMutablePointer<GLKVector3>, Int)](glkquaternionrotatevector3array(_:_:_:).md)
  Applies a quaternion rotation to an array of vectors.
- [func GLKQuaternionRotateVector4(GLKQuaternion, GLKVector4) -> GLKVector4](glkquaternionrotatevector4(_:_:).md)
  Returns a new vector calculated by applying a quaternion rotation to a vector.
- [func GLKQuaternionRotateVector4Array(GLKQuaternion, UnsafeMutablePointer<GLKVector4>, Int)](glkquaternionrotatevector4array(_:_:_:).md)
  Applies a quaternion rotation to an array of vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkquaternionrotatevector3(_:_:))*