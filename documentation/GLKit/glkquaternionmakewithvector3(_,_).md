# GLKQuaternionMakeWithVector3(_:_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns a quaternion created from a vector and a scalar.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKQuaternionMakeWithVector3(_ vector: GLKVector3, _ scalar: Float) -> GLKQuaternion
```

```c
static GLKQuaternion GLKQuaternionMakeWithVector3(GLKVector3 vector, float scalar);
```

## Return Value

A new quaternion.

## Parameters

- `vector`: The vector portion of the new quaternion.
- `scalar`: The scalar portion of the new quaternion.

## See Also

### Creating Quaternions
- [func GLKQuaternionMake(Float, Float, Float, Float) -> GLKQuaternion](./glkquaternionmake%28_,_,_,_%29.md)
  Returns a quaternion created from its separate components.
- [func GLKQuaternionMakeWithArray(UnsafeMutablePointer<Float>!) -> GLKQuaternion](./glkquaternionmakewitharray%28_%29.md)
  Returns a quaternion created from an array of components.
- [func GLKQuaternionMakeWithAngleAndAxis(Float, Float, Float, Float) -> GLKQuaternion](./glkquaternionmakewithangleandaxis%28_,_,_,_%29.md)
  Creates a quaternion that represents a rotation around an axis.
- [func GLKQuaternionMakeWithAngleAndVector3Axis(Float, GLKVector3) -> GLKQuaternion](./glkquaternionmakewithangleandvector3axis%28_,_%29.md)
  Creates a quaternion that represents a rotation around an axis.
- [func GLKQuaternionMakeWithMatrix3(GLKMatrix3) -> GLKQuaternion](./glkquaternionmakewithmatrix3%28_%29.md)
  Creates a quaternion from a rotation matrix.
- [func GLKQuaternionMakeWithMatrix4(GLKMatrix4) -> GLKQuaternion](./glkquaternionmakewithmatrix4%28_%29.md)
  Creates a quaternion from a rotation matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkquaternionmakewithvector3(_:_:))*