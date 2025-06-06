# GLKQuaternionNormalize(_:)

**Framework**: GLKit  
**Kind**: func

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

#### Return Value

A new quaternion, normalized to have a length of `1.0`.

## Parameters

- `quaternion`: A quaternion.

## See Also

- [func GLKQuaternionInvert(GLKQuaternion) -> GLKQuaternion](glkquaternioninvert(_:).md)
  Returns an inverse of a quaternion.
- [func GLKQuaternionConjugate(GLKQuaternion) -> GLKQuaternion](glkquaternionconjugate(_:).md)
  Returns the conjugate of a quaternion.
- [func GLKQuaternionAdd(GLKQuaternion, GLKQuaternion) -> GLKQuaternion](glkquaternionadd(_:_:).md)
  Returns the sum of two quaternions.
- [func GLKQuaternionSubtract(GLKQuaternion, GLKQuaternion) -> GLKQuaternion](glkquaternionsubtract(_:_:).md)
  Returns the difference between two quaternions.
- [func GLKQuaternionMultiply(GLKQuaternion, GLKQuaternion) -> GLKQuaternion](glkquaternionmultiply(_:_:).md)
  Returns the product of two quaternions.
- [func GLKQuaternionSlerp(GLKQuaternion, GLKQuaternion, Float) -> GLKQuaternion](glkquaternionslerp(_:_:_:).md)
  Returns the spherical linear interpolation of two quaternions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkquaternionnormalize(_:))*