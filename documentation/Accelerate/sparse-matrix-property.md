# sparse_matrix_property

**Framework**: Accelerate  
**Kind**: struct

The matrix property type.

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
struct sparse_matrix_property
```

#### Overview

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 19, iPadOS 19, macOS 16, tvOS 19, watchOS 19, and visionOS 3, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Topics

### Constants
- [var SPARSE_UPPER_TRIANGULAR: sparse_matrix_property](sparse_upper_triangular.md)
  An upper triangular matrix.
- [var SPARSE_LOWER_TRIANGULAR: sparse_matrix_property](sparse_lower_triangular.md)
  A lower triangular matrix.
- [var SPARSE_UPPER_SYMMETRIC: sparse_matrix_property](sparse_upper_symmetric.md)
  A symmetric matrix with values derived from the upper triangle.
- [var SPARSE_LOWER_SYMMETRIC: sparse_matrix_property](sparse_lower_symmetric.md)
  A symmetric matrix with values derived from the lower triangle.
### Initializers
- [init(UInt32)](sparse_matrix_property/init(_:).md)
- [init(rawValue: UInt32)](sparse_matrix_property/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](sparse_matrix_property/rawvalue.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_matrix_property)*