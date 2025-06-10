# cblas_drotmg(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Generates a modified Givens rotation matrix.

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
func cblas_drotmg(_ D1: UnsafeMutablePointer<Double>, _ D2: UnsafeMutablePointer<Double>, _ B1: UnsafeMutablePointer<Double>, _ B2: Double, _ P: UnsafeMutablePointer<Double>)
```

#### Discussion

The resulting matrix zeroes the second component of the vector `(sqrt(D1)*B1, sqrt(SD2)*B2)`.

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 19, iPadOS 19, macOS 16, tvOS 19, watchOS 19, and visionOS 3, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Parameters

- `D1`: Scaling factor  .
- `D2`: Scaling factor  .
- `B1`: Scaling factor  .
- `B2`: Scaling factor  .
- `P`: :   and   are obtained from matrix  .   is 1.0.   is -1.0.

## See Also

- [func cblas_dasum(__LAPACK_int, UnsafePointer<Double>?, __LAPACK_int) -> Double](cblas_dasum(_:_:_:).md)
  Computes the sum of the absolute values of elements in a vector (double-precision).
- [func cblas_daxpy(__LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_daxpy(_:_:_:_:_:_:).md)
  Computes a constant times a vector plus a vector (double-precision).
- [func cblas_dcopy(__LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dcopy(_:_:_:_:_:).md)
  Copies a vector to another vector (double-precision).
- [func cblas_dgbmv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dgbmv(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales a general band matrix, then multiplies by a vector, then adds a vector (double precision).
- [func cblas_dgemm(CBLAS_ORDER, CBLAS_TRANSPOSE, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dgemm(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies two matrices (double-precision).
- [func cblas_dgemv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dgemv(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies a matrix by a vector (double precision).
- [func cblas_dger(CBLAS_ORDER, __LAPACK_int, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dger(_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies vector X by the transpose of vector Y, then adds matrix A (double precison).
- [func cblas_dnrm2(__LAPACK_int, UnsafePointer<Double>?, __LAPACK_int) -> Double](cblas_dnrm2(_:_:_:).md)
  Computes the L2 norm (Euclidian length) of a vector (double precision).
- [func cblas_drot(__LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int, Double, Double)](cblas_drot(_:_:_:_:_:_:_:).md)
  Applies a Givens rotation matrix to a pair of vectors.
- [func cblas_drotg(UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>)](cblas_drotg(_:_:_:_:).md)
  Constructs a Givens rotation matrix.
- [func cblas_drotm(__LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int, UnsafePointer<Double>)](cblas_drotm(_:_:_:_:_:_:).md)
  Applies a modified Givens transformation (single precision).
- [func cblas_dsbmv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dsbmv(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales a symmetric band matrix, then multiplies by a vector, then adds a vector (double precision).
- [func cblas_dscal(__LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dscal(_:_:_:_:).md)
  Multiplies each element of a vector by a constant (double-precision).
- [func cblas_dspmv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Double, UnsafePointer<Double>?, UnsafePointer<Double>?, __LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dspmv(_:_:_:_:_:_:_:_:_:_:).md)
  Scales a packed symmetric matrix, then multiplies by a vector, then scales and adds another vector (double precision).
- [func cblas_dspr(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?)](cblas_dspr(_:_:_:_:_:_:_:).md)
  Rank one update: adds a packed symmetric matrix to the product of a scaling factor, a vector, and its transpose (double precision).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/cblas_drotmg(_:_:_:_:_:))*