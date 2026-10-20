# appleblas_sgeadd(_:_:_:_:_:_:_:_:_:_:_:_:_:)

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
func appleblas_sgeadd(_ ORDER: CBLAS_ORDER, _ TRANSA: CBLAS_TRANSPOSE, _ TRANSB: CBLAS_TRANSPOSE, _ M: __LAPACK_int, _ N: __LAPACK_int, _ ALPHA: Float, _ A: UnsafePointer<Float>?, _ LDA: __LAPACK_int, _ BETA: Float, _ B: UnsafePointer<Float>?, _ LDB: __LAPACK_int, _ C: UnsafeMutablePointer<Float>, _ LDC: __LAPACK_int)
```

```c
extern void appleblas_sgeadd(const enum CBLAS_ORDER ORDER, const enum CBLAS_TRANSPOSE TRANSA, const enum CBLAS_TRANSPOSE TRANSB, const __LAPACK_int M, const __LAPACK_int N, const float ALPHA, const float *A, const __LAPACK_int LDA, const float BETA, const float *B, const __LAPACK_int LDB, float *C, const __LAPACK_int LDC);
```

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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/appleblas_sgeadd(_:_:_:_:_:_:_:_:_:_:_:_:_:))*