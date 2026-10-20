# cblas_ssyr(_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

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

```c
void cblas_ssyr(const enum CBLAS_ORDER ORDER, const enum CBLAS_UPLO UPLO, const __LAPACK_int N, const float ALPHA, const float *X, const __LAPACK_int INCX, float *A, const __LAPACK_int LDA);
```

#### Discussion

Calculates `A + alpha*x*x` and stores the result in `A`.

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 26, iPadOS 26, macOS 26, tvOS 26, visionOS 26, and watchOS 26, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings under Apple Clang - Preprocessing > Preprocessor Macros.

## Parameters

- `ORDER`: Specifies row-major (C) or column-major (Fortran) data ordering.
- `UPLO`: Specifies whether to use the upper or lower triangle from the matrix. Valid values are `'U'` or `'L'`.
- `N`: Order of matrix `A`; number of elements in vector `x`.
- `ALPHA`: Scaling factor to multiply `x` by.
- `X`: Vector `x`.
- `INCX`: Stride within `X`. For example, if `incX` is 7, every 7th element is used.
- `A`: Matrix `A`.
- `LDA`: Leading dimension of array containing matrix `A`.

## See Also

### Single-precision float matrix functions
- [func cblas_sasum(__LAPACK_int, UnsafePointer<Float>?, __LAPACK_int) -> Float](./cblas_sasum%28_,_,_%29.md)
  Computes the sum of the absolute values of elements in a vector (single-precision).
- [func cblas_saxpy(__LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int)](./cblas_saxpy%28_,_,_,_,_,_%29.md)
  Computes a constant times a vector plus a vector (single-precision).
- [func cblas_scopy(__LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int)](./cblas_scopy%28_,_,_,_,_%29.md)
  Copies a vector to another vector (single-precision).
- [func cblas_sgbmv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](./cblas_sgbmv%28_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Scales a general band matrix, then multiplies by a vector, then adds a vector (single precision).
- [func cblas_sgemm(CBLAS_ORDER, CBLAS_TRANSPOSE, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](./cblas_sgemm%28_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Multiplies two matrices (single-precision).
- [func cblas_sgemv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](./cblas_sgemv%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Multiplies a single-precision matrix by a vector.
- [func cblas_sger(CBLAS_ORDER, __LAPACK_int, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int)](./cblas_sger%28_,_,_,_,_,_,_,_,_,_%29.md)
  Multiplies vector X by the transpose of vector Y, then adds matrix A (single precison).
- [func cblas_snrm2(__LAPACK_int, UnsafePointer<Float>?, __LAPACK_int) -> Float](./cblas_snrm2%28_,_,_%29.md)
  Computes the L2 norm (Euclidian length) of a vector (single precision).
- [func cblas_srot(__LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int, Float, Float)](./cblas_srot%28_,_,_,_,_,_,_%29.md)
  Applies a Givens rotation matrix to a pair of vectors.
- [func cblas_srotg(UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>)](./cblas_srotg%28_,_,_,_%29.md)
  Constructs a Givens rotation matrix.
- [func cblas_srotm(__LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int, UnsafePointer<Float>)](./cblas_srotm%28_,_,_,_,_,_%29.md)
  Applies a modified Givens transformation (single precision).
- [func cblas_srotmg(UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, Float, UnsafeMutablePointer<Float>)](./cblas_srotmg%28_,_,_,_,_%29.md)
  Generates a modified Givens rotation matrix.
- [func cblas_ssbmv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](./cblas_ssbmv%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Scales a symmetric band matrix, then multiplies by a vector, then adds a vector (single-precision).
- [func cblas_sscal(__LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](./cblas_sscal%28_,_,_,_%29.md)
  Multiplies each element of a vector by a constant (single-precision).
- [func cblas_sspmv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Float, UnsafePointer<Float>?, UnsafePointer<Float>?, __LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](./cblas_sspmv%28_,_,_,_,_,_,_,_,_,_%29.md)
  Scales a packed symmetric matrix, then multiplies by a vector, then scales and adds another vector (single precision).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/cblas_ssyr(_:_:_:_:_:_:_:_:))*