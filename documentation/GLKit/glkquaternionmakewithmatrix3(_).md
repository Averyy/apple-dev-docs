# GLKQuaternionMakeWithMatrix3(_:)

**Framework**: GLKit  
**Kind**: func

Creates a quaternion from a rotation matrix.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKQuaternionMakeWithMatrix3(_ matrix: GLKMatrix3) -> GLKQuaternion
```

#### Return Value

A new quaternion.

## Parameters

- `matrix`: A rotation matrix to convert into a quaternion.

## See Also

- [func GLKQuaternionMake(Float, Float, Float, Float) -> GLKQuaternion](glkquaternionmake(_:_:_:_:).md)
  Returns a quaternion created from its separate components.
- [func GLKQuaternionMakeWithArray(UnsafeMutablePointer<Float>!) -> GLKQuaternion](glkquaternionmakewitharray(_:).md)
  Returns a quaternion created from an array of components.
- [func GLKQuaternionMakeWithVector3(GLKVector3, Float) -> GLKQuaternion](glkquaternionmakewithvector3(_:_:).md)
  Returns a quaternion created from a vector and a scalar.
- [func GLKQuaternionMakeWithAngleAndAxis(Float, Float, Float, Float) -> GLKQuaternion](glkquaternionmakewithangleandaxis(_:_:_:_:).md)
  Creates a quaternion that represents a rotation around an axis.
- [func GLKQuaternionMakeWithAngleAndVector3Axis(Float, GLKVector3) -> GLKQuaternion](glkquaternionmakewithangleandvector3axis(_:_:).md)
  Creates a quaternion that represents a rotation around an axis.
- [func GLKQuaternionMakeWithMatrix4(GLKMatrix4) -> GLKQuaternion](glkquaternionmakewithmatrix4(_:).md)
  Creates a quaternion from a rotation matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkquaternionmakewithmatrix3(_:))*