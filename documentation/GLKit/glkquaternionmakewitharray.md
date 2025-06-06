# GLKQuaternionMakeWithArray(_:)

**Framework**: GLKit  
**Kind**: func

Returns a quaternion created from an array of components.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKQuaternionMakeWithArray(_ values: UnsafeMutablePointer<Float>!) -> GLKQuaternion
```

#### Return Value

A new quaternion.

## Parameters

- `values`: The four components that comprise the new quaternion.

## See Also

- [func GLKQuaternionMake(Float, Float, Float, Float) -> GLKQuaternion](glkquaternionmake(_:_:_:_:).md)
  Returns a quaternion created from its separate components.
- [func GLKQuaternionMakeWithVector3(GLKVector3, Float) -> GLKQuaternion](glkquaternionmakewithvector3(_:_:).md)
  Returns a quaternion created from a vector and a scalar.
- [func GLKQuaternionMakeWithAngleAndAxis(Float, Float, Float, Float) -> GLKQuaternion](glkquaternionmakewithangleandaxis(_:_:_:_:).md)
  Creates a quaternion that represents a rotation around an axis.
- [func GLKQuaternionMakeWithAngleAndVector3Axis(Float, GLKVector3) -> GLKQuaternion](glkquaternionmakewithangleandvector3axis(_:_:).md)
  Creates a quaternion that represents a rotation around an axis.
- [func GLKQuaternionMakeWithMatrix3(GLKMatrix3) -> GLKQuaternion](glkquaternionmakewithmatrix3(_:).md)
  Creates a quaternion from a rotation matrix.
- [func GLKQuaternionMakeWithMatrix4(GLKMatrix4) -> GLKQuaternion](glkquaternionmakewithmatrix4(_:).md)
  Creates a quaternion from a rotation matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkquaternionmakewitharray(_:))*