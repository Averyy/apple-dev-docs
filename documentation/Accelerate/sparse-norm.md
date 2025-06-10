# sparse_norm

**Framework**: Accelerate  
**Kind**: struct

The norm specifier.

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
struct sparse_norm
```

#### Overview

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 19, iPadOS 19, macOS 16, tvOS 19, watchOS 19, and visionOS 3, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Topics

### Constants
- [var SPARSE_NORM_ONE: sparse_norm](sparse_norm_one.md)
  Norm One
- [var SPARSE_NORM_TWO: sparse_norm](sparse_norm_two.md)
  Norm Two
- [var SPARSE_NORM_INF: sparse_norm](sparse_norm_inf.md)
  Norm Inf
- [var SPARSE_NORM_R1: sparse_norm](sparse_norm_r1.md)
  Norm R1
### Initializers
- [init(UInt32)](sparse_norm/init(_:).md)
- [init(rawValue: UInt32)](sparse_norm/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](sparse_norm/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias sparse_matrix_double](sparse_matrix_double.md)
  Sparse matrix opaque type for double.
- [typealias sparse_matrix_float](sparse_matrix_float.md)
  Sparse matrix opaque type for float.
- [struct sparse_status](sparse_status.md)
  The type reflecting the status of an operations.
- [typealias sparse_dimension](sparse_dimension.md)
  The dimension type.
- [typealias sparse_index](sparse_index.md)
  The index type.
- [typealias sparse_stride](sparse_stride.md)
  The stride type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_norm)*