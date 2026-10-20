# GLKQuaternionMultiply(_:_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns the product of two quaternions.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKQuaternionMultiply(_ quaternionLeft: GLKQuaternion, _ quaternionRight: GLKQuaternion) -> GLKQuaternion
```

```c
static GLKQuaternion GLKQuaternionMultiply(GLKQuaternion quaternionLeft, GLKQuaternion quaternionRight);
```

#### Return Value

A new quaternion.

## Parameters

- `quaternionLeft`: The first quaternion.
- `quaternionRight`: The second quaternion.

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
- [func GLKQuaternionSlerp(GLKQuaternion, GLKQuaternion, Float) -> GLKQuaternion](./glkquaternionslerp%28_,_,_%29.md)
  Returns the spherical linear interpolation of two quaternions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkquaternionmultiply(_:_:))*