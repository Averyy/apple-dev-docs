# GLKQuaternionInvert(_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns an inverse of a quaternion.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKQuaternionInvert(_ quaternion: GLKQuaternion) -> GLKQuaternion
```

```c
static GLKQuaternion GLKQuaternionInvert(GLKQuaternion quaternion);
```

## Return Value

A new quaternion that is the inverse of the source quaternion.

## Parameters

- `quaternion`: A quaternion.

## See Also

### Performing Mathematical Operations on Quaternions
- [func GLKQuaternionNormalize(GLKQuaternion) -> GLKQuaternion](./glkquaternionnormalize%28_%29.md)
  Returns a normalized version of a quaternion.
- [func GLKQuaternionConjugate(GLKQuaternion) -> GLKQuaternion](./glkquaternionconjugate%28_%29.md)
  Returns the conjugate of a quaternion.
- [func GLKQuaternionAdd(GLKQuaternion, GLKQuaternion) -> GLKQuaternion](./glkquaternionadd%28_,_%29.md)
  Returns the sum of two quaternions.
- [func GLKQuaternionSubtract(GLKQuaternion, GLKQuaternion) -> GLKQuaternion](./glkquaternionsubtract%28_,_%29.md)
  Returns the difference between two quaternions.
- [func GLKQuaternionMultiply(GLKQuaternion, GLKQuaternion) -> GLKQuaternion](./glkquaternionmultiply%28_,_%29.md)
  Returns the product of two quaternions.
- [func GLKQuaternionSlerp(GLKQuaternion, GLKQuaternion, Float) -> GLKQuaternion](./glkquaternionslerp%28_,_,_%29.md)
  Returns the spherical linear interpolation of two quaternions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkquaternioninvert(_:))*