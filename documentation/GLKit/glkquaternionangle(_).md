# GLKQuaternionAngle(_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns the rotation angle of a quaternion.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKQuaternionAngle(_ quaternion: GLKQuaternion) -> Float
```

```c
float GLKQuaternionAngle(GLKQuaternion quaternion);
```

#### Return Value

The angle of the rotation in radians (a positive angle is counterclockwise).

## Parameters

- `quaternion`: A quaternion.

## See Also

### Retrieving Information About a Quaternion
- [func GLKQuaternionLength(GLKQuaternion) -> Float](./glkquaternionlength%28_%29.md)
  Returns the length of a quaternion.
- [func GLKQuaternionAxis(GLKQuaternion) -> GLKVector3](./glkquaternionaxis%28_%29.md)
  Returns the axis of rotation of a quaternion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkquaternionangle(_:))*