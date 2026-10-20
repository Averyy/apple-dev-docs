# cblas_crotg(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Constructs a complex Givens rotation.

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
func cblas_crotg(_ A: OpaquePointer, _ B: OpaquePointer, _ C: UnsafeMutablePointer<Float>, _ S: OpaquePointer)
```

```c
void cblas_crotg(__LAPACK_float_complex *A, __LAPACK_float_complex *B, float *C, __LAPACK_float_complex *S);
```

#### Discussion

Given a vertical matrix containing `a` and `b`, computes the values of `cos θ` and `sin θ` that zero the lower value (`b`). Returns the value of `sin θ` in `s`, the value of `cos θ` in `c`, and the upper value (`r`) in `a`.

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 26, iPadOS 26, macOS 26, tvOS 26, visionOS 26, and watchOS 26, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings under Apple Clang - Preprocessing > Preprocessor Macros.

## Parameters

- `A`: Complex value `a`. Overwritten on output.
- `B`: Complex value `a`.
- `C`: Real value `c`. Unused on entry. Overwritten on return with the value `cos(θ)`.
- `S`: Complex value `s`. Unused on entry. Overwritten on return with the value `sin(θ)`.

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
- [func cblas_chemm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](./cblas_chemm%28_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Multiplies two Hermitian matrices (single-precision complex), then adds a third (with scaling).
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/cblas_crotg(_:_:_:_:))*