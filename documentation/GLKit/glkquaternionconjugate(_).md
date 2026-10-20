# GLKQuaternionConjugate(_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns the conjugate of a quaternion.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKQuaternionConjugate(_ quaternion: GLKQuaternion) -> GLKQuaternion
```

```c
static GLKQuaternion GLKQuaternionConjugate(GLKQuaternion quaternion);
```

#### Return Value

A new quaternion that is the conjugate of the source quaternion.

#### Discussion

The conjugate of a quaternion has the same scalar value, but the signs of the vector components are flipped.

## Parameters

- `quaternion`: A quaternion.

## See Also

### Performing Mathematical Operations on Quaternions
- [func GLKQuaternionNormalize(GLKQuaternion) -> GLKQuaternion](./glkquaternionnormalize%28_%29.md)
  Returns a normalized version of a quaternion.
- [func GLKQuaternionInvert(GLKQuaternion) -> GLKQuaternion](./glkquaternioninvert%28_%29.md)
  Returns an inverse of a quaternion.
- [func GLKQuaternionAdd(GLKQuaternion, GLKQuaternion) -> GLKQuaternion](./glkquaternionadd%28_,_%29.md)
  Returns the sum of two quaternions.
- [func GLKQuaternionSubtract(GLKQuaternion, GLKQuaternion) -> GLKQuaternion](./glkquaternionsubtract%28_,_%29.md)
  Returns the difference between two quaternions.
- [func GLKQuaternionMultiply(GLKQuaternion, GLKQuaternion) -> GLKQuaternion](./glkquaternionmultiply%28_,_%29.md)
  Returns the product of two quaternions.
- [func GLKQuaternionSlerp(GLKQuaternion, GLKQuaternion, Float) -> GLKQuaternion](./glkquaternionslerp%28_,_,_%29.md)
  Returns the spherical linear interpolation of two quaternions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkquaternionconjugate(_:))*