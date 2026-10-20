# appleblas_dgeadd(_:_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

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
func appleblas_dgeadd(_ ORDER: CBLAS_ORDER, _ TRANSA: CBLAS_TRANSPOSE, _ TRANSB: CBLAS_TRANSPOSE, _ M: __LAPACK_int, _ N: __LAPACK_int, _ ALPHA: Double, _ A: UnsafePointer<Double>?, _ LDA: __LAPACK_int, _ BETA: Double, _ B: UnsafePointer<Double>?, _ LDB: __LAPACK_int, _ C: UnsafeMutablePointer<Double>, _ LDC: __LAPACK_int)
```

```c
extern void appleblas_dgeadd(const enum CBLAS_ORDER ORDER, const enum CBLAS_TRANSPOSE TRANSA, const enum CBLAS_TRANSPOSE TRANSB, const __LAPACK_int M, const __LAPACK_int N, const double ALPHA, const double *A, const __LAPACK_int LDA, const double BETA, const double *B, const __LAPACK_int LDB, double *C, const __LAPACK_int LDC);
```

## See Also

### Double-precision float matrix functions
- [func cblas_dasum(__LAPACK_int, UnsafePointer<Double>?, __LAPACK_int) -> Double](./cblas_dasum%28_,_,_%29.md)
  Computes the sum of the absolute values of elements in a vector (double-precision).
- [func cblas_daxpy(__LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int)](./cblas_daxpy%28_,_,_,_,_,_%29.md)
  Computes a constant times a vector plus a vector (double-precision).
- [func cblas_dcopy(__LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int)](./cblas_dcopy%28_,_,_,_,_%29.md)
  Copies a vector to another vector (double-precision).
- [func cblas_dgbmv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](./cblas_dgbmv%28_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Scales a general band matrix, then multiplies by a vector, then adds a vector (double precision).
- [func cblas_dgemm(CBLAS_ORDER, CBLAS_TRANSPOSE, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](./cblas_dgemm%28_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Multiplies two matrices (double-precision).
- [func cblas_dgemv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](./cblas_dgemv%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Multiplies a matrix by a vector (double precision).
- [func cblas_dger(CBLAS_ORDER, __LAPACK_int, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int)](./cblas_dger%28_,_,_,_,_,_,_,_,_,_%29.md)
  Multiplies vector X by the transpose of vector Y, then adds matrix A (double precison).
- [func cblas_dnrm2(__LAPACK_int, UnsafePointer<Double>?, __LAPACK_int) -> Double](./cblas_dnrm2%28_,_,_%29.md)
  Computes the L2 norm (Euclidian length) of a vector (double precision).
- [func cblas_drot(__LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int, Double, Double)](./cblas_drot%28_,_,_,_,_,_,_%29.md)
  Applies a Givens rotation matrix to a pair of vectors.
- [func cblas_drotg(UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>)](./cblas_drotg%28_,_,_,_%29.md)
  Constructs a Givens rotation matrix.
- [func cblas_drotm(__LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int, UnsafePointer<Double>)](./cblas_drotm%28_,_,_,_,_,_%29.md)
  Applies a modified Givens transformation (single precision).
- [func cblas_drotmg(UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, Double, UnsafeMutablePointer<Double>)](./cblas_drotmg%28_,_,_,_,_%29.md)
  Generates a modified Givens rotation matrix.
- [func cblas_dsbmv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](./cblas_dsbmv%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Scales a symmetric band matrix, then multiplies by a vector, then adds a vector (double precision).
- [func cblas_dscal(__LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](./cblas_dscal%28_,_,_,_%29.md)
  Multiplies each element of a vector by a constant (double-precision).
- [func cblas_dspmv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Double, UnsafePointer<Double>?, UnsafePointer<Double>?, __LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](./cblas_dspmv%28_,_,_,_,_,_,_,_,_,_%29.md)
  Scales a packed symmetric matrix, then multiplies by a vector, then scales and adds another vector (double precision).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/appleblas_dgeadd(_:_:_:_:_:_:_:_:_:_:_:_:_:))*