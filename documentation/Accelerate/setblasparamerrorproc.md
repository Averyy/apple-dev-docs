# SetBLASParamErrorProc

**Framework**: Accelerate  
**Kind**: func

Sets an error handler function.

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
void SetBLASParamErrorProc(BLASParamErrorProc __ErrorProc);
```

#### Discussion

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 19, iPadOS 19, macOS 16, tvOS 19, watchOS 19, and visionOS 3, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Parameters

- `__ErrorProc`: The handler function BLAS should call when an error occurs (because of an invalid input, for example).

## See Also

- [cblas_errprn](cblas_errprn.md)
  Prints an error message.
- [cblas_errprn](cblas_errprn.md)
  Prints an error message.
- [cblas_xerbla](cblas_xerbla.md)
  The default error handler for BLAS routines.
- [func cblas_icamax(__LAPACK_int, OpaquePointer?, __LAPACK_int) -> __LAPACK_int](cblas_icamax(_:_:_:).md)
  Returns the index of the element with the largest absolute value in a vector (single-precision complex).
- [func cblas_idamax(__LAPACK_int, UnsafePointer<Double>?, __LAPACK_int) -> __LAPACK_int](cblas_idamax(_:_:_:).md)
  Returns the index of the element with the largest absolute value in a vector (double-precision).
- [func cblas_isamax(__LAPACK_int, UnsafePointer<Float>?, __LAPACK_int) -> __LAPACK_int](cblas_isamax(_:_:_:).md)
  Returns the index of the element with the largest absolute value in a vector (single-precision).
- [func cblas_izamax(__LAPACK_int, OpaquePointer?, __LAPACK_int) -> __LAPACK_int](cblas_izamax(_:_:_:).md)
  Returns the index of the element with the largest absolute value in a vector (double-precision complex).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/setblasparamerrorproc)*