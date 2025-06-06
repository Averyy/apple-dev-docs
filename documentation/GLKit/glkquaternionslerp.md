# GLKQuaternionSlerp(_:_:_:)

**Framework**: GLKit  
**Kind**: func

Returns the spherical linear interpolation of two quaternions.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKQuaternionSlerp(_ quaternionStart: GLKQuaternion, _ quaternionEnd: GLKQuaternion, _ t: Float) -> GLKQuaternion
```

#### Return Value

A new quaternion. When `t=0`, the result is the start quaternion. When `t=1.0`, the result is the end quaternion. For any other value of `t`, the result is a spherical linear interpolation between the two quaternions.

## Parameters

- `quaternionStart`: The starting point.
- `quaternionEnd`: The ending point.
- `t`: The interpolation factor.

## See Also

- [func GLKQuaternionNormalize(GLKQuaternion) -> GLKQuaternion](glkquaternionnormalize(_:).md)
  Returns a normalized version of a quaternion.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkquaternionslerp(_:_:_:))*