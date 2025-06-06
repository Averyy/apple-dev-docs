# GLKQuaternionSubtract(_:_:)

**Framework**: GLKit  
**Kind**: func

Returns the difference between two quaternions.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKQuaternionSubtract(_ quaternionLeft: GLKQuaternion, _ quaternionRight: GLKQuaternion) -> GLKQuaternion
```

#### Return Value

A new quaternion.

## Parameters

- `quaternionLeft`: The minuend.
- `quaternionRight`: The subtrahend.

## See Also

- [func GLKQuaternionNormalize(GLKQuaternion) -> GLKQuaternion](glkquaternionnormalize(_:).md)
  Returns a normalized version of a quaternion.
- [func GLKQuaternionInvert(GLKQuaternion) -> GLKQuaternion](glkquaternioninvert(_:).md)
  Returns an inverse of a quaternion.
- [func GLKQuaternionConjugate(GLKQuaternion) -> GLKQuaternion](glkquaternionconjugate(_:).md)
  Returns the conjugate of a quaternion.
- [func GLKQuaternionAdd(GLKQuaternion, GLKQuaternion) -> GLKQuaternion](glkquaternionadd(_:_:).md)
  Returns the sum of two quaternions.
- [func GLKQuaternionMultiply(GLKQuaternion, GLKQuaternion) -> GLKQuaternion](glkquaternionmultiply(_:_:).md)
  Returns the product of two quaternions.
- [func GLKQuaternionSlerp(GLKQuaternion, GLKQuaternion, Float) -> GLKQuaternion](glkquaternionslerp(_:_:_:).md)
  Returns the spherical linear interpolation of two quaternions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkquaternionsubtract(_:_:))*