# SIMD Vector Types

**Framework**: Swift

Work with fixed-width vectors of fixed-width numeric types of different sizes.

## Topics

### SIMD Vectors
- [struct SIMD2](simd2.md)
  A vector of two scalar values.
- [struct SIMD3](simd3.md)
  A vector of three scalar values.
- [struct SIMD4](simd4.md)
  A vector of four scalar values.
- [struct SIMD8](simd8.md)
  A vector of eight scalar values.
- [struct SIMD16](simd16.md)
  A vector of 16 scalar values.
- [struct SIMD32](simd32.md)
  A vector of 32 scalar values.
- [struct SIMD64](simd64.md)
  A vector of 64 scalar values.
### Supporting Types
- [protocol SIMD](simd.md)
  A SIMD vector of a fixed number of elements.
- [protocol SIMDScalar](simdscalar.md)
  A type that can be used as an element in a SIMD vector.
- [protocol SIMDStorage](simdstorage.md)
  A type that can function as storage for a SIMD vector type.
- [struct SIMDMask](simdmask.md)
### Supporting Functions
- [func all<Storage>(SIMDMask<Storage>) -> Bool](all(_:).md)
  True if every lane of mask is true.
- [func any<Storage>(SIMDMask<Storage>) -> Bool](any(_:).md)
  True if any lane of mask is true.
- [func pointwiseMax<T>(T, T) -> T](pointwisemax(_:_:)-29hn2.md)
  The lanewise maximum of two vectors.
- [func pointwiseMax<T>(T, T) -> T](pointwisemax(_:_:)-2k6er.md)
  The lanewise maximum of two vectors.
- [func pointwiseMin<T>(T, T) -> T](pointwisemin(_:_:)-39txi.md)
  The lanewise minimum of two vectors.
- [func pointwiseMin<T>(T, T) -> T](pointwisemin(_:_:)-8v95p.md)
  The lanewise minimum of two vectors.

## See Also

- [Numeric Protocols](numeric-protocols.md)
  Write generic code that works with any numeric type.
- [Special-Use Numeric Types](special-use-numeric-types.md)
  Work with fixed-width numeric types of different sizes.
- [Global Numeric Functions](global-numeric-functions.md)
  Use these functions with numeric values and other comparable types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd-vector-types)*