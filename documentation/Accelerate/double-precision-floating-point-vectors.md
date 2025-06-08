# Double-precision floating-point vectors

**Framework**: Accelerate

Perform operations on vectors that contain double-precision floating-point elements.

#### Overview

The simd library provides many functions in this group, in three variants:

- The default variant—for example, [`simd_rsqrt(_:)`](https://developer.apple.com/documentation/simd/simd_rsqrt(_:)-i5ka)
- The precise variant—for example, [`simd_precise_rsqrt(_:)`](https://developer.apple.com/documentation/simd/simd_precise_rsqrt(_:)-136bw)
- The fast variant—for example, [`simd_fast_rsqrt(_:)`](https://developer.apple.com/documentation/simd/simd_fast_rsqrt(_:)-8p6tk)

The precise variants are accurate to a few units in the last place (ULPs). The fast variants provide greater speed but may have as little as 22 bits of accuracy for double-precision functions.

The compiler flag defines the behavior of the default variant. Ordinarily, the compiler resolves the default variants to their precise counterparts. Set the `-ffast-math` compiler flag to specify that the default variants of the functions resolve to the fast variants.

## Topics

### Vector data types
- [typealias simd_double1](../simd/simd_double1.md)
  A vector of one 64-bit floating-point element.
- [typealias simd_double2](../simd/simd_double2.md)
  A vector of two 64-bit floating-point elements.
- [typealias simd_double3](../simd/simd_double3.md)
  A vector of three 64-bit floating-point elements.
- [typealias simd_double4](../simd/simd_double4.md)
  A vector of four 64-bit floating-point elements.
- [typealias simd_double8](../simd/simd_double8.md)
  A vector of eight 64-bit floating-point elements.
### Packed vector data types
- [typealias simd_packed_double2](../simd/simd_packed_double2.md)
  A packed vector of two 64-bit floating-point elements.
- [typealias simd_packed_double4](../simd/simd_packed_double4.md)
  A packed vector of four 64-bit floating-point elements.
- [typealias simd_packed_double8](../simd/simd_packed_double8.md)
  A packed vector of eight 64-bit floating-point elements.

## See Also

- [Working with Vectors](working-with-vectors.md)
  Use vectors to calculate geometric values, calculate dot products and cross products, and interpolate between values.
- [Half-precision floating-point vectors](half-precision-floating-point-vectors.md)
  Perform operations on vectors that contain half-precision floating-point elements.
- [Single-precision floating-point vectors](single-precision-floating-point-vectors.md)
  Perform operations on vectors that contain single-precision floating-point elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/double-precision-floating-point-vectors)*