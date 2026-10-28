# cblas_icamax(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns the index of the element with the largest absolute value in a vector (single-precision complex).

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
func cblas_icamax(_ N: __LAPACK_int, _ X: OpaquePointer?, _ INCX: __LAPACK_int) -> __LAPACK_int
```

```c
__LAPACK_int cblas_icamax(const __LAPACK_int N, const __LAPACK_float_complex *X, const __LAPACK_int INCX);
```

## Return Value

Returns an index in the range 0..N-1 corresponding with the element with the largest absolute value.

## Discussion

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 26, iPadOS 26, macOS 26, tvOS 26, visionOS 26, and watchOS 26, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings under Apple Clang - Preprocessing > Preprocessor Macros.

## Parameters

- `N`: Number of elements in the vector.
- `X`: The vector.
- `INCX`: Stride within `X`. For example, if `incX` is 7, every 7th element is used.

## See Also

### General functions
- [func cblas_idamax(__LAPACK_int, UnsafePointer<Double>?, __LAPACK_int) -> __LAPACK_int](./cblas_idamax%28_,_,_%29.md)
  Returns the index of the element with the largest absolute value in a vector (double-precision).
- [func cblas_isamax(__LAPACK_int, UnsafePointer<Float>?, __LAPACK_int) -> __LAPACK_int](./cblas_isamax%28_,_,_%29.md)
  Returns the index of the element with the largest absolute value in a vector (single-precision).
- [func cblas_izamax(__LAPACK_int, OpaquePointer?, __LAPACK_int) -> __LAPACK_int](./cblas_izamax%28_,_,_%29.md)
  Returns the index of the element with the largest absolute value in a vector (double-precision complex).
- [SetBLASParamErrorProc](./setblasparamerrorproc.md)
  Sets an error handler function.
- [cblas_errprn](./cblas_errprn.md)
  Prints an error message.
- [cblas_xerbla](./cblas_xerbla.md)
  The default error handler for BLAS routines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/cblas_icamax(_:_:_:))*