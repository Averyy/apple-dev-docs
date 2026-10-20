# GLKQuaternionNormalize(_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns a normalized version of a quaternion.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKQuaternionNormalize(_ quaternion: GLKQuaternion) -> GLKQuaternion
```

```c
static GLKQuaternion GLKQuaternionNormalize(GLKQuaternion quaternion);
```

#### Return Value

A new quaternion, normalized to have a length of `1.0`.

## Parameters

- `quaternion`: A quaternion.

## See Also

### Performing Mathematical Operations on Quaternions
- [func GLKQuaternionInvert(GLKQuaternion) -> GLKQuaternion](./glkquaternioninvert%28_%29.md)
  Returns an inverse of a quaternion.
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

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkquaternionnormalize(_:))*