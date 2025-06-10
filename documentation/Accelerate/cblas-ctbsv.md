# cblas_ctbsv(_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Solves a triangular banded system of equations.

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
func cblas_ctbsv(_ ORDER: CBLAS_ORDER, _ UPLO: CBLAS_UPLO, _ TRANSA: CBLAS_TRANSPOSE, _ DIAG: CBLAS_DIAG, _ N: __LAPACK_int, _ K: __LAPACK_int, _ A: OpaquePointer?, _ LDA: __LAPACK_int, _ X: OpaquePointer?, _ INCX: __LAPACK_int)
```

#### Discussion

Solves the system of equations `A*X=B` or `A'*X=B`, depending on the value of `TransA`.

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 19, iPadOS 19, macOS 16, tvOS 19, watchOS 19, and visionOS 3, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Parameters

- `ORDER`: Specifies row-major (C) or column-major (Fortran) data ordering.
- `UPLO`: Specifies whether to use the upper or lower triangle from the matrix. Valid values are   or  .
- `TRANSA`: Specifies whether to use matrix A (  or  ) or the transpose of A ( ,  ,  , or  ).
- `DIAG`: Specifies whether the matrix is unit triangular. Possible values are   (unit triangular) or   (not unit triangular).
- `N`: Order of matrix  .
- `K`: Number of superdiagonals or subdiagonals of matrix   (depending on the value of  ).
- `A`: Matrix  .
- `LDA`: The leading dimension of matrix  .
- `X`: Contains vector   on entry. Overwritten with vector   on return.
- `INCX`: Stride within  . For example, if   is 7, every 7th element is used.

## See Also

- [func cblas_caxpy(__LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_caxpy(_:_:_:_:_:_:).md)
  Computes a constant times a vector plus a vector (single-precision complex).
- [func cblas_ccopy(__LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_ccopy(_:_:_:_:_:).md)
  Copies a vector to another vector (single-precision complex).
- [func cblas_cgbmv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_cgbmv(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales a general band matrix, then multiplies by a vector, then adds a vector (single-precision complex).
- [func cblas_cgemm(CBLAS_ORDER, CBLAS_TRANSPOSE, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_cgemm(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies two matrices (single-precision complex).
- [func cblas_cgemv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_cgemv(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies a matrix by a vector (single-precision complex).
- [func cblas_cgerc(CBLAS_ORDER, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_cgerc(_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies vector X by the conjugate transpose of vector Y, then adds matrix A (single-precision complex).
- [func cblas_cgeru(CBLAS_ORDER, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_cgeru(_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies vector X by the transpose of vector Y, then adds matrix A (single-precision complex).
- [func cblas_chbmv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_chbmv(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales a Hermitian band matrix, then multiplies by a vector, then adds a vector (single-precision complex).
- [func cblas_chemm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_chemm(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies two Hermitian matrices (single-precision complex), then adds a third (with scaling).
- [func cblas_chemv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_chemv(_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales and multiplies a Hermitian matrix by a vector, then adds a second (scaled) vector.
- [func cblas_cher(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Float, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_cher(_:_:_:_:_:_:_:_:).md)
  Hermitian rank 1 update: adds the product of a scaling factor, vector `X`, and the conjugate transpose of `X` to matrix `A`.
- [func cblas_cher2(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_cher2(_:_:_:_:_:_:_:_:_:_:).md)
  Hermitian rank 2 update: adds the product of a scaling factor, vector `X`, and the conjugate transpose of vector `Y` to the product of the conjugate of the scaling factor, vector `Y`, and the conjugate transpose of vector `X`, and adds the result to matrix `A`.
- [func cblas_cher2k(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, Float, OpaquePointer?, __LAPACK_int)](cblas_cher2k(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Performs a rank-2k update of a complex Hermitian matrix (single-precision complex).
- [func cblas_cherk(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, Float, OpaquePointer?, __LAPACK_int, Float, OpaquePointer?, __LAPACK_int)](cblas_cherk(_:_:_:_:_:_:_:_:_:_:_:).md)
  Rank-k update—multiplies a Hermitian matrix by its transpose and adds a second matrix (single precision).
- [func cblas_chpmv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, OpaquePointer, OpaquePointer?, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_chpmv(_:_:_:_:_:_:_:_:_:_:).md)
  Scales a packed hermitian matrix, multiplies it by a vector, and adds a scaled vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/cblas_ctbsv(_:_:_:_:_:_:_:_:_:_:))*