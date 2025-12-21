# catlas_cset(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Modifies a vector (single-precision complex) in place, setting each element to a given value.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
func catlas_cset(_ N: __LAPACK_int, _ ALPHA: OpaquePointer, _ X: OpaquePointer, _ INCX: __LAPACK_int)
```

#### Discussion

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 26, iPadOS 26, macOS 26, tvOS 26, visionOS 26, and watchOS 26, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Parameters

- `N`: The number of elements in the vector.
- `ALPHA`: The new value.
- `X`: The vector to modify.
- `INCX`: Stride within  . For example, if   is 7, every 7th element is used.

## See Also

- [func catlas_caxpby(__LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](catlas_caxpby(_:_:_:_:_:_:_:).md)
  Computes the product of two vectors, scaling each one separately (single-precision complex).
- [func catlas_daxpby(__LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](catlas_daxpby(_:_:_:_:_:_:_:).md)
  Computes the sum of two vectors, scaling each one separately (double-precision).
- [func catlas_dset(__LAPACK_int, Double, UnsafeMutablePointer<Double>, __LAPACK_int)](catlas_dset(_:_:_:_:).md)
  Modifies a vector (double-precision) in place, setting each element to a given value.
- [func catlas_saxpby(__LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](catlas_saxpby(_:_:_:_:_:_:_:).md)
  Computes the sum of two vectors, scaling each one separately (single-precision).
- [func catlas_sset(__LAPACK_int, Float, UnsafeMutablePointer<Float>, __LAPACK_int)](catlas_sset(_:_:_:_:).md)
  Modifies a vector (single-precision) in place, setting each element to a given value.
- [func catlas_zaxpby(__LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](catlas_zaxpby(_:_:_:_:_:_:_:).md)
  Computes the sum of two vectors, scaling each one separately (double-precision complex).
- [func catlas_zset(__LAPACK_int, OpaquePointer, OpaquePointer, __LAPACK_int)](catlas_zset(_:_:_:_:).md)
  Modifies a vector (double-precision complex) in place, setting each element to a given value.
- [func cblas_sdot(__LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int) -> Float](cblas_sdot(_:_:_:_:_:).md)
  Computes the dot product of two vectors (single-precision).
- [func cblas_sdsdot(__LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int) -> Float](cblas_sdsdot(_:_:_:_:_:_:).md)
  Computes the dot product of two single-precision vectors plus an initial single-precision value.
- [func cblas_cdotc_sub(__LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer)](cblas_cdotc_sub(_:_:_:_:_:_:).md)
  Calculates the dot product of the complex conjugate of a single-precision complex vector with a second single-precision complex vector.
- [func cblas_cdotu_sub(__LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer)](cblas_cdotu_sub(_:_:_:_:_:_:).md)
  Computes the dot product of two single-precision complex vectors.
- [func cblas_ddot(__LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int) -> Double](cblas_ddot(_:_:_:_:_:).md)
  Computes the dot product of two vectors (double-precision).
- [func cblas_dsdot(__LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int) -> Double](cblas_dsdot(_:_:_:_:_:).md)
  Computes the double-precision dot product of a pair of single-precision vectors.
- [func cblas_zdotc_sub(__LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer)](cblas_zdotc_sub(_:_:_:_:_:_:).md)
  Calculates the dot product of the complex conjugate of a double-precision complex vector with a second double-precision complex vector.
- [func cblas_zdotu_sub(__LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer)](cblas_zdotu_sub(_:_:_:_:_:_:).md)
  Computes the dot product of two double-precision complex vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/catlas_cset(_:_:_:_:))*