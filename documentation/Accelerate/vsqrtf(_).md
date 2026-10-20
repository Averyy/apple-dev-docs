# vsqrtf(_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

For each vector element, calculates the square root of `X`.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func vsqrtf(_: vFloat) -> vFloat
```

```c
extern vFloat vsqrtf(vFloat );
```

## See Also

### Floating-Point Arithmetic and Auxiliary Functions (from vfp.h)
- [func vceilf(vFloat) -> vFloat](./vceilf%28_%29.md)
  Computes the ceiling of values in a vector of floating-point values.
- [func vcopysignf(vFloat, vFloat) -> vFloat](./vcopysignf%28_,_%29.md)
  For each vector element, produces a value with the magnitude of `arg2` and sign `arg1`.  Note that the order of the arguments matches the recommendation of the IEEE 754 floating-point standard, which is opposite from the SANE copysign function.
- [func vdivf(vFloat, vFloat) -> vFloat](./vdivf%28_,_%29.md)
  For each vector element, calculates `A`/`B`.
- [func vfabf(vFloat) -> vFloat](./vfabf%28_%29.md)
  For each vector element, calculates the absolute value of `v`.
- [func vfabsf(vFloat) -> vFloat](./vfabsf%28_%29.md)
- [func vfloorf(vFloat) -> vFloat](./vfloorf%28_%29.md)
  Computes the floor of values in a vector of floating-point values.
- [func vintf(vFloat) -> vFloat](./vintf%28_%29.md)
  Truncates the decimal portion of a vector of floating-point values.
- [func vnintf(vFloat) -> vFloat](./vnintf%28_%29.md)
  Rounds to the nearest integer (nearest even for ties).
- [func vnextafterf(vFloat, vFloat) -> vFloat](./vnextafterf%28_,_%29.md)
  For each vector element, calculates the next representable value after `x` in the direction of `y`.  If `x` is equal to `y`, then `y` is returned.
- [func vrecf(vFloat) -> vFloat](./vrecf%28_%29.md)
  Computes the reciprocal of values in a vector.
- [func vrsqrtf(vFloat) -> vFloat](./vrsqrtf%28_%29.md)
  For each vector element, calculates the inverse of the square root of `X`.
- [func vtablelookup(vSInt32, UnsafeMutablePointer<UInt32>) -> vUInt32](./vtablelookup%28_,_%29.md)
  For each vector element of `Index_Vect`, returns the corresponding value from `Table`.
- [func vtruncf(vFloat) -> vFloat](./vtruncf%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vsqrtf(_:))*