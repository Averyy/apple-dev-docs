# cblas_chemm(_:_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Multiplies two Hermitian matrices (single-precision complex), then adds a third (with scaling).

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
func cblas_chemm(_ ORDER: CBLAS_ORDER, _ SIDE: CBLAS_SIDE, _ UPLO: CBLAS_UPLO, _ M: __LAPACK_int, _ N: __LAPACK_int, _ ALPHA: OpaquePointer, _ A: OpaquePointer?, _ LDA: __LAPACK_int, _ B: OpaquePointer?, _ LDB: __LAPACK_int, _ BETA: OpaquePointer, _ C: OpaquePointer?, _ LDC: __LAPACK_int)
```

```c
void cblas_chemm(const enum CBLAS_ORDER ORDER, const enum CBLAS_SIDE SIDE, const enum CBLAS_UPLO UPLO, const __LAPACK_int M, const __LAPACK_int N, const __LAPACK_float_complex *ALPHA, const __LAPACK_float_complex *A, const __LAPACK_int LDA, const __LAPACK_float_complex *B, const __LAPACK_int LDB, const __LAPACK_float_complex *BETA, __LAPACK_float_complex *C, const __LAPACK_int LDC);
```

## Discussion

This function multiplies `A * B` or `B * A` (depending on the value of `Side`) and multiplies the resulting matrix by `alpha`. It then multiplies matrix `C` by `beta`. It stores the sum of these two products in matrix `C`.

Thus, it calculates either

`C←αAB + βC`

or

`C←αBA + βC`

where

`A = A`

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 26, iPadOS 26, macOS 26, tvOS 26, visionOS 26, and watchOS 26, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings under Apple Clang - Preprocessing > Preprocessor Macros.

``

## Parameters

- `ORDER`: Specifies row-major (C) or column-major (Fortran) data ordering.
- `SIDE`: Determines the order in which the matrices should be multiplied.
- `UPLO`: Specifies whether to use the upper or lower triangle from the matrix. Valid values are `'U'` or `'L'`.
- `M`: The number of rows in matrices `A` and `C`.
- `N`: The number of columns in matrices `B` and `C`.
- `ALPHA`: Scaling factor for the product of matrices A and B.
- `A`: Matrix A.
- `LDA`: The size of the first dimension of matrix `A`; if you are passing a matrix `A[m][n]`, the value should be `m`.
- `B`: Matrix B.
- `LDB`: The size of the first dimension of matrix `B`; if you are passing a matrix `B[m][n]`, the value should be `m`.
- `BETA`: Scaling factor for matrix C.
- `C`: Matrix C.
- `LDC`: The size of the first dimension of matrix `C`; if you are passing a matrix `C[m][n]`, the value should be `m`.

## See Also

### Single-precision complex matrix functions
- [func cblas_caxpy(__LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](./cblas_caxpy%28_,_,_,_,_,_%29.md)
  Computes a constant times a vector plus a vector (single-precision complex).
- [func cblas_ccopy(__LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](./cblas_ccopy%28_,_,_,_,_%29.md)
  Copies a vector to another vector (single-precision complex).
- [func cblas_cgbmv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](./cblas_cgbmv%28_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Scales a general band matrix, then multiplies by a vector, then adds a vector (single-precision complex).
- [func cblas_cgemm(CBLAS_ORDER, CBLAS_TRANSPOSE, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](./cblas_cgemm%28_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Multiplies two matrices (single-precision complex).
- [func cblas_cgemv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](./cblas_cgemv%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Multiplies a matrix by a vector (single-precision complex).
- [func cblas_cgerc(CBLAS_ORDER, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](./cblas_cgerc%28_,_,_,_,_,_,_,_,_,_%29.md)
  Multiplies vector X by the conjugate transpose of vector Y, then adds matrix A (single-precision complex).
- [func cblas_cgeru(CBLAS_ORDER, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](./cblas_cgeru%28_,_,_,_,_,_,_,_,_,_%29.md)
  Multiplies vector X by the transpose of vector Y, then adds matrix A (single-precision complex).
- [func cblas_chbmv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](./cblas_chbmv%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Scales a Hermitian band matrix, then multiplies by a vector, then adds a vector (single-precision complex).
- [func cblas_chemv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](./cblas_chemv%28_,_,_,_,_,_,_,_,_,_,_%29.md)
  Scales and multiplies a Hermitian matrix by a vector, then adds a second (scaled) vector.
- [func cblas_cher(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Float, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](./cblas_cher%28_,_,_,_,_,_,_,_%29.md)
  Hermitian rank 1 update: adds the product of a scaling factor, vector `X`, and the conjugate transpose of `X` to matrix `A`.
- [func cblas_cher2(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](./cblas_cher2%28_,_,_,_,_,_,_,_,_,_%29.md)
  Hermitian rank 2 update: adds the product of a scaling factor, vector `X`, and the conjugate transpose of vector `Y` to the product of the conjugate of the scaling factor, vector `Y`, and the conjugate transpose of vector `X`, and adds the result to matrix `A`.
- [func cblas_cher2k(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, Float, OpaquePointer?, __LAPACK_int)](./cblas_cher2k%28_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Performs a rank-2k update of a complex Hermitian matrix (single-precision complex).
- [func cblas_cherk(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, Float, OpaquePointer?, __LAPACK_int, Float, OpaquePointer?, __LAPACK_int)](./cblas_cherk%28_,_,_,_,_,_,_,_,_,_,_%29.md)
  Rank-k update—multiplies a Hermitian matrix by its transpose and adds a second matrix (single precision).
- [func cblas_chpmv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, OpaquePointer, OpaquePointer?, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](./cblas_chpmv%28_,_,_,_,_,_,_,_,_,_%29.md)
  Scales a packed hermitian matrix, multiplies it by a vector, and adds a scaled vector.
- [func cblas_chpr(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Float, OpaquePointer?, __LAPACK_int, OpaquePointer?)](./cblas_chpr%28_,_,_,_,_,_,_%29.md)
  Scales and multiplies a vector times its conjugate transpose, then adds a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/cblas_chemm(_:_:_:_:_:_:_:_:_:_:_:_:_:))*