# cblas_zswap(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Exchanges the elements of two vectors (double-precision complex).

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
func cblas_zswap(_ N: __LAPACK_int, _ X: OpaquePointer?, _ INCX: __LAPACK_int, _ Y: OpaquePointer?, _ INCY: __LAPACK_int)
```

```c
void cblas_zswap(const __LAPACK_int N, __LAPACK_double_complex *X, const __LAPACK_int INCX, __LAPACK_double_complex *Y, const __LAPACK_int INCY);
```

#### Discussion

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 26, iPadOS 26, macOS 26, tvOS 26, visionOS 26, and watchOS 26, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings under Apple Clang - Preprocessing > Preprocessor Macros.

## Parameters

- `N`: Number of elements in vectors
- `X`: Vector `x`. On return, contains elements copied from vector `y`.
- `INCX`: Stride within `X`. For example, if `incX` is 7, every 7th element is used.
- `Y`: Vector `y`. On return, contains elements copied from vector `x`.
- `INCY`: Stride within `Y`. For example, if `incY` is 7, every 7th element is used.

## See Also

### Double-precision complex matrix functions
- [func cblas_dzasum(__LAPACK_int, OpaquePointer?, __LAPACK_int) -> Double](./cblas_dzasum%28_,_,_%29.md)
  Computes the sum of the absolute values of real and imaginary parts of elements in a vector (single-precision complex).
- [func cblas_dznrm2(__LAPACK_int, OpaquePointer?, __LAPACK_int) -> Double](./cblas_dznrm2%28_,_,_%29.md)
  Computes the unitary norm of a vector (double-precision complex).
- [func cblas_zaxpy(__LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](./cblas_zaxpy%28_,_,_,_,_,_%29.md)
  Computes a constant times a vector plus a vector (double-precision complex).
- [func cblas_zcopy(__LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](./cblas_zcopy%28_,_,_,_,_%29.md)
  Copies a vector to another vector (double-precision complex).
- [func cblas_zdrot(__LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, Double, Double)](./cblas_zdrot%28_,_,_,_,_,_,_%29.md)
  Applies a Givens rotation matrix to a pair of complex vectors.
- [func cblas_zdscal(__LAPACK_int, Double, OpaquePointer?, __LAPACK_int)](./cblas_zdscal%28_,_,_,_%29.md)
  Multiplies each element of a vector by a constant (double-precision complex).
- [func cblas_zgbmv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](./cblas_zgbmv%28_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Scales a general band matrix, then multiplies by a vector, then adds a vector (double-precision complex).
- [func cblas_zgemm(CBLAS_ORDER, CBLAS_TRANSPOSE, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](./cblas_zgemm%28_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Multiplies two matrices (double-precision complex).
- [func cblas_zgemv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](./cblas_zgemv%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Multiplies a matrix by a vector (double-precision complex).
- [func cblas_zgerc(CBLAS_ORDER, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](./cblas_zgerc%28_,_,_,_,_,_,_,_,_,_%29.md)
  Multiplies vector X by the conjugate transpose of vector Y, then adds matrix A (double-precision complex).
- [func cblas_zgeru(CBLAS_ORDER, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](./cblas_zgeru%28_,_,_,_,_,_,_,_,_,_%29.md)
  Multiplies vector X by the transpose of vector Y, then adds matrix A (double-precision complex).
- [func cblas_zhbmv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](./cblas_zhbmv%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Scales a Hermitian band matrix, then multiplies by a vector, then adds a vector (double-precision complex).
- [func cblas_zhemm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](./cblas_zhemm%28_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Multiplies two Hermitian matrices (double-precision complex).
- [func cblas_zhemv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](./cblas_zhemv%28_,_,_,_,_,_,_,_,_,_,_%29.md)
  Scales and multiplies a Hermitian matrix by a vector, then adds a second (scaled) vector.
- [func cblas_zher(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Double, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](./cblas_zher%28_,_,_,_,_,_,_,_%29.md)
  Adds the product of a scaling factor, vector `X`, and the conjugate transpose of `X` to matrix `A`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/cblas_zswap(_:_:_:_:_:))*