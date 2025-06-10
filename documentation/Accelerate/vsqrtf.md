# vsqrtf(_:)

**Framework**: Accelerate  
**Kind**: func

For each vector element, calculates the square root of `X`.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func vsqrtf(_: vFloat) -> vFloat
```

## See Also

- [func vceilf(vFloat) -> vFloat](vceilf(_:).md)
  Computes the ceiling of values in a vector of floating-point values.
- [func vcopysignf(vFloat, vFloat) -> vFloat](vcopysignf(_:_:).md)
  For each vector element, produces a value with the magnitude of `arg2` and sign `arg1`.  Note that the order of the arguments matches the recommendation of the IEEE 754 floating-point standard, which is opposite from the SANE copysign function.
- [func vdivf(vFloat, vFloat) -> vFloat](vdivf(_:_:).md)
  For each vector element, calculates `A`/`B`.
- [func vfabf(vFloat) -> vFloat](vfabf(_:).md)
  For each vector element, calculates the absolute value of `v`.
- [func vfabsf(vFloat) -> vFloat](vfabsf(_:).md)
- [func vfloorf(vFloat) -> vFloat](vfloorf(_:).md)
  Computes the floor of values in a vector of floating-point values.
- [func vintf(vFloat) -> vFloat](vintf(_:).md)
  Truncates the decimal portion of a vector of floating-point values.
- [func vnintf(vFloat) -> vFloat](vnintf(_:).md)
  Rounds to the nearest integer (nearest even for ties).
- [func vnextafterf(vFloat, vFloat) -> vFloat](vnextafterf(_:_:).md)
  For each vector element, calculates the next representable value after `x` in the direction of `y`.  If `x` is equal to `y`, then `y` is returned.
- [func vrecf(vFloat) -> vFloat](vrecf(_:).md)
  Computes the reciprocal of values in a vector.
- [func vrsqrtf(vFloat) -> vFloat](vrsqrtf(_:).md)
  For each vector element, calculates the inverse of the square root of `X`.
- [func vtablelookup(vSInt32, UnsafeMutablePointer<UInt32>) -> vUInt32](vtablelookup(_:_:).md)
  For each vector element of `Index_Vect`, returns the corresponding value from `Table`.
- [func vtruncf(vFloat) -> vFloat](vtruncf(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vsqrtf(_:))*