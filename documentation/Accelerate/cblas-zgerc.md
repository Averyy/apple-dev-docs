# cblas_zgerc(_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Multiplies vector X by the conjugate transpose of vector Y, then adds matrix A (double-precision complex).

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
func cblas_zgerc(_ ORDER: CBLAS_ORDER, _ M: __LAPACK_int, _ N: __LAPACK_int, _ ALPHA: OpaquePointer, _ X: OpaquePointer?, _ INCX: __LAPACK_int, _ Y: OpaquePointer?, _ INCY: __LAPACK_int, _ A: OpaquePointer?, _ LDA: __LAPACK_int)
```

#### Discussion

Computes `alpha*x*conjg(y') + A`.

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 26, iPadOS 26, macOS 26, tvOS 26, visionOS 26, and watchOS 26, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Parameters

- `ORDER`: Specifies row-major (C) or column-major (Fortran) data ordering.
- `M`: Number of rows in matrix  .
- `N`: Number of columns in matrix  .
- `ALPHA`: Scaling factor for vector  .
- `X`: Vector  .
- `INCX`: Stride within  . For example, if   is 7, every 7th element is used.
- `Y`: Vector  .
- `INCY`: Stride within  . For example, if   is 7, every 7th element is used.
- `A`: Matrix  .
- `LDA`: Leading dimension of array containing matrix  .

## See Also

- [func cblas_dzasum(__LAPACK_int, OpaquePointer?, __LAPACK_int) -> Double](cblas_dzasum(_:_:_:).md)
  Computes the sum of the absolute values of real and imaginary parts of elements in a vector (single-precision complex).
- [func cblas_dznrm2(__LAPACK_int, OpaquePointer?, __LAPACK_int) -> Double](cblas_dznrm2(_:_:_:).md)
  Computes the unitary norm of a vector (double-precision complex).
- [func cblas_zaxpy(__LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_zaxpy(_:_:_:_:_:_:).md)
  Computes a constant times a vector plus a vector (double-precision complex).
- [func cblas_zcopy(__LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_zcopy(_:_:_:_:_:).md)
  Copies a vector to another vector (double-precision complex).
- [func cblas_zdrot(__LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, Double, Double)](cblas_zdrot(_:_:_:_:_:_:_:).md)
  Applies a Givens rotation matrix to a pair of complex vectors.
- [func cblas_zdscal(__LAPACK_int, Double, OpaquePointer?, __LAPACK_int)](cblas_zdscal(_:_:_:_:).md)
  Multiplies each element of a vector by a constant (double-precision complex).
- [func cblas_zgbmv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_zgbmv(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales a general band matrix, then multiplies by a vector, then adds a vector (double-precision complex).
- [func cblas_zgemm(CBLAS_ORDER, CBLAS_TRANSPOSE, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_zgemm(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies two matrices (double-precision complex).
- [func cblas_zgemv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_zgemv(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies a matrix by a vector (double-precision complex).
- [func cblas_zgeru(CBLAS_ORDER, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_zgeru(_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies vector X by the transpose of vector Y, then adds matrix A (double-precision complex).
- [func cblas_zhbmv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_zhbmv(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales a Hermitian band matrix, then multiplies by a vector, then adds a vector (double-precision complex).
- [func cblas_zhemm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_zhemm(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies two Hermitian matrices (double-precision complex).
- [func cblas_zhemv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_zhemv(_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales and multiplies a Hermitian matrix by a vector, then adds a second (scaled) vector.
- [func cblas_zher(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Double, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_zher(_:_:_:_:_:_:_:_:).md)
  Adds the product of a scaling factor, vector `X`, and the conjugate transpose of `X` to matrix `A`.
- [func cblas_zher2(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_zher2(_:_:_:_:_:_:_:_:_:_:).md)
  Hermitian rank 2 update: adds the product of a scaling factor, vector `X`, and the conjugate transpose of vector `Y` to the product of the conjugate of the scaling factor, vector `Y`, and the conjugate transpose of vector `X`, and adds the result to matrix `A`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/cblas_zgerc(_:_:_:_:_:_:_:_:_:_:))*