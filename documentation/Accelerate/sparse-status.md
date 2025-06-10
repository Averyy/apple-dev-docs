# sparse_status

**Framework**: Accelerate  
**Kind**: struct

The type reflecting the status of an operations.

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
struct sparse_status
```

#### Overview

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 19, iPadOS 19, macOS 16, tvOS 19, watchOS 19, and visionOS 3, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Topics

### Constants
- [var SPARSE_SUCCESS: sparse_status](sparse_success.md)
  Operation was a success.
- [var SPARSE_ILLEGAL_PARAMETER: sparse_status](sparse_illegal_parameter.md)
  Operation was not completed because one or more of the arguments had an illegal value.
- [var SPARSE_CANNOT_SET_PROPERTY: sparse_status](sparse_cannot_set_property.md)
  A property was set after values were inserted into the matrix.
- [var SPARSE_SYSTEM_ERROR: sparse_status](sparse_system_error.md)
  An internal error has occured, such as non enough memory.
### Initializers
- [init(Int32)](sparse_status/init(_:).md)
- [init(rawValue: Int32)](sparse_status/init(rawvalue:).md)
### Instance Properties
- [var rawValue: Int32](sparse_status/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias sparse_dimension](sparse_dimension.md)
  The dimension type.
- [typealias sparse_index](sparse_index.md)
  The index type.
- [typealias sparse_matrix_double](sparse_matrix_double.md)
  Sparse matrix opaque type for double.
- [typealias sparse_matrix_float](sparse_matrix_float.md)
  Sparse matrix opaque type for float.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_status)*