# GLKQuaternionAxis(_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns the axis of rotation of a quaternion.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKQuaternionAxis(_ quaternion: GLKQuaternion) -> GLKVector3
```

```c
GLKVector3 GLKQuaternionAxis(GLKQuaternion quaternion);
```

## Return Value

The axis of rotation.

## Parameters

- `quaternion`: A quaternion.

## See Also

### Retrieving Information About a Quaternion
- [func GLKQuaternionLength(GLKQuaternion) -> Float](./glkquaternionlength%28_%29.md)
  Returns the length of a quaternion.
- [func GLKQuaternionAngle(GLKQuaternion) -> Float](./glkquaternionangle%28_%29.md)
  Returns the rotation angle of a quaternion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkquaternionaxis(_:))*