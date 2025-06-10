# cblas_xerbla

**Framework**: Accelerate  
**Kind**: func

The default error handler for BLAS routines.

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
void cblas_xerbla(__LAPACK_int p, char * rout, char * form, ...);
```

#### Discussion

Add any additional parameters required for the format string.

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 19, iPadOS 19, macOS 16, tvOS 19, watchOS 19, and visionOS 3, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Parameters

- `p`: The position of the invalid parameter
- `rout`: The name of the routine that generated this error.
- `form`: A format string describing the error.

## See Also

- [SetBLASParamErrorProc](setblasparamerrorproc.md)
  Sets an error handler function.
- [cblas_errprn](cblas_errprn.md)
  Prints an error message.
- [func cblas_icamax(__LAPACK_int, OpaquePointer?, __LAPACK_int) -> __LAPACK_int](cblas_icamax(_:_:_:).md)
  Returns the index of the element with the largest absolute value in a vector (single-precision complex).
- [func cblas_idamax(__LAPACK_int, UnsafePointer<Double>?, __LAPACK_int) -> __LAPACK_int](cblas_idamax(_:_:_:).md)
  Returns the index of the element with the largest absolute value in a vector (double-precision).
- [func cblas_isamax(__LAPACK_int, UnsafePointer<Float>?, __LAPACK_int) -> __LAPACK_int](cblas_isamax(_:_:_:).md)
  Returns the index of the element with the largest absolute value in a vector (single-precision).
- [func cblas_izamax(__LAPACK_int, OpaquePointer?, __LAPACK_int) -> __LAPACK_int](cblas_izamax(_:_:_:).md)
  Returns the index of the element with the largest absolute value in a vector (double-precision complex).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/cblas_xerbla)*