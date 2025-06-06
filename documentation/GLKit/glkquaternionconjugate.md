# GLKQuaternionConjugate(_:)

**Framework**: GLKit  
**Kind**: func

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

#### Return Value

A new quaternion that is the conjugate of the source quaternion.

#### Discussion

The conjugate of a quaternion has the same scalar value, but the signs of the vector components are flipped.

## Parameters

- `quaternion`: A quaternion.

## See Also

- [func GLKQuaternionNormalize(GLKQuaternion) -> GLKQuaternion](glkquaternionnormalize(_:).md)
  Returns a normalized version of a quaternion.
- [func GLKQuaternionInvert(GLKQuaternion) -> GLKQuaternion](glkquaternioninvert(_:).md)
  Returns an inverse of a quaternion.
- [func GLKQuaternionAdd(GLKQuaternion, GLKQuaternion) -> GLKQuaternion](glkquaternionadd(_:_:).md)
  Returns the sum of two quaternions.
- [func GLKQuaternionSubtract(GLKQuaternion, GLKQuaternion) -> GLKQuaternion](glkquaternionsubtract(_:_:).md)
  Returns the difference between two quaternions.
- [func GLKQuaternionMultiply(GLKQuaternion, GLKQuaternion) -> GLKQuaternion](glkquaternionmultiply(_:_:).md)
  Returns the product of two quaternions.
- [func GLKQuaternionSlerp(GLKQuaternion, GLKQuaternion, Float) -> GLKQuaternion](glkquaternionslerp(_:_:_:).md)
  Returns the spherical linear interpolation of two quaternions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkquaternionconjugate(_:))*