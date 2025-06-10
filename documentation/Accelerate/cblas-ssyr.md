# cblas_ssyr(_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Rank one update: adds a symmetric matrix to the product of a scaling factor, a vector, and its transpose (single precision).

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
func cblas_ssyr(_ ORDER: CBLAS_ORDER, _ UPLO: CBLAS_UPLO, _ N: __LAPACK_int, _ ALPHA: Float, _ X: UnsafePointer<Float>?, _ INCX: __LAPACK_int, _ A: UnsafeMutablePointer<Float>?, _ LDA: __LAPACK_int)
```

#### Discussion

Calculates `A + alpha*x*x` and stores the result in `A`.

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 19, iPadOS 19, macOS 16, tvOS 19, watchOS 19, and visionOS 3, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Parameters

- `ORDER`: Specifies row-major (C) or column-major (Fortran) data ordering.
- `UPLO`: Specifies whether to use the upper or lower triangle from the matrix. Valid values are   or  .
- `N`: Order of matrix  ; number of elements in vector  .
- `ALPHA`: Scaling factor to multiply   by.
- `X`: Vector  .
- `INCX`: Stride within  . For example, if   is 7, every 7th element is used.
- `A`: Matrix  .
- `LDA`: Leading dimension of array containing matrix  .

## See Also

- [func cblas_sasum(__LAPACK_int, UnsafePointer<Float>?, __LAPACK_int) -> Float](cblas_sasum(_:_:_:).md)
  Computes the sum of the absolute values of elements in a vector (single-precision).
- [func cblas_saxpy(__LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_saxpy(_:_:_:_:_:_:).md)
  Computes a constant times a vector plus a vector (single-precision).
- [func cblas_scopy(__LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_scopy(_:_:_:_:_:).md)
  Copies a vector to another vector (single-precision).
- [func cblas_sgbmv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_sgbmv(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales a general band matrix, then multiplies by a vector, then adds a vector (single precision).
- [func cblas_sgemm(CBLAS_ORDER, CBLAS_TRANSPOSE, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_sgemm(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies two matrices (single-precision).
- [func cblas_sgemv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_sgemv(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies a single-precision matrix by a vector.
- [func cblas_sger(CBLAS_ORDER, __LAPACK_int, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_sger(_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies vector X by the transpose of vector Y, then adds matrix A (single precison).
- [func cblas_snrm2(__LAPACK_int, UnsafePointer<Float>?, __LAPACK_int) -> Float](cblas_snrm2(_:_:_:).md)
  Computes the L2 norm (Euclidian length) of a vector (single precision).
- [func cblas_srot(__LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int, Float, Float)](cblas_srot(_:_:_:_:_:_:_:).md)
  Applies a Givens rotation matrix to a pair of vectors.
- [func cblas_srotg(UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>)](cblas_srotg(_:_:_:_:).md)
  Constructs a Givens rotation matrix.
- [func cblas_srotm(__LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int, UnsafePointer<Float>)](cblas_srotm(_:_:_:_:_:_:).md)
  Applies a modified Givens transformation (single precision).
- [func cblas_srotmg(UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, Float, UnsafeMutablePointer<Float>)](cblas_srotmg(_:_:_:_:_:).md)
  Generates a modified Givens rotation matrix.
- [func cblas_ssbmv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_ssbmv(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales a symmetric band matrix, then multiplies by a vector, then adds a vector (single-precision).
- [func cblas_sscal(__LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_sscal(_:_:_:_:).md)
  Multiplies each element of a vector by a constant (single-precision).
- [func cblas_sspmv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Float, UnsafePointer<Float>?, UnsafePointer<Float>?, __LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_sspmv(_:_:_:_:_:_:_:_:_:_:).md)
  Scales a packed symmetric matrix, then multiplies by a vector, then scales and adds another vector (single precision).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/cblas_ssyr(_:_:_:_:_:_:_:_:))*