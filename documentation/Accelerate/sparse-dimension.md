# sparse_dimension

**Framework**: Accelerate  
**Kind**: typealias

The dimension type.

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
typealias sparse_dimension = UInt64
```

#### Discussion

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 19, iPadOS 19, macOS 16, tvOS 19, watchOS 19, and visionOS 3, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## See Also

- [typealias sparse_index](sparse_index.md)
  The index type.
- [typealias sparse_matrix_double](sparse_matrix_double.md)
  Sparse matrix opaque type for double.
- [typealias sparse_matrix_float](sparse_matrix_float.md)
  Sparse matrix opaque type for float.
- [struct sparse_status](sparse_status.md)
  The type reflecting the status of an operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_dimension)*