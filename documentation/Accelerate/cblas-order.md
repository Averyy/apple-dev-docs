# CBLAS_ORDER

**Framework**: Accelerate  
**Kind**: struct

Indicates whether a matrix is in row-major or column-major order.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct CBLAS_ORDER
```

#### Overview

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 26, iPadOS 26, macOS 26, tvOS 26, visionOS 26, and watchOS 26, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings under Apple Clang - Preprocessing > Preprocessor Macros.

## Topics

### Initializers
- [init(UInt32)](cblas_order/init(_:).md)
- [init(rawValue: UInt32)](cblas_order/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](cblas_order/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct CBLAS_TRANSPOSE](cblas_transpose.md)
  Indicates transpose operation to perform on a matrix.
- [struct CBLAS_UPLO](cblas_uplo.md)
- [struct CBLAS_DIAG](cblas_diag.md)
  Indicates whether a triangular matrix is unit-diagonal (diagonal elements are all equal to 1).
- [struct CBLAS_SIDE](cblas_side.md)
  Indicates the order of a matrix multiplication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/cblas_order)*