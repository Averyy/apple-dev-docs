# GLKQuaternionSlerp(_:_:_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

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

```c
GLKQuaternion GLKQuaternionSlerp(GLKQuaternion quaternionStart, GLKQuaternion quaternionEnd, float t);
```

## Return Value

A new quaternion. When `t=0`, the result is the start quaternion. When `t=1.0`, the result is the end quaternion. For any other value of `t`, the result is a spherical linear interpolation between the two quaternions.

## Parameters

- `quaternionStart`: The starting point.
- `quaternionEnd`: The ending point.
- `t`: The interpolation factor.

## See Also

### Performing Mathematical Operations on Quaternions
- [func GLKQuaternionNormalize(GLKQuaternion) -> GLKQuaternion](./glkquaternionnormalize%28_%29.md)
  Returns a normalized version of a quaternion.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkquaternionslerp(_:_:_:))*