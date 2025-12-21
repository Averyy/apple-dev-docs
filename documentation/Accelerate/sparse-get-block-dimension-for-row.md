# sparse_get_block_dimension_for_row(_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns the dimension of the block for a specified row of a double-precision matrix.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func sparse_get_block_dimension_for_row(_ A: UnsafeMutableRawPointer!, _ i: sparse_index) -> Int
```

#### Return Value

The dimension of the block of the specified row.

#### Discussion

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 26, iPadOS 26, macOS 26, tvOS 26, visionOS 26, and watchOS 26, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Parameters

- `A`: The sparse matrix,  , which must have been created with  ,   ,  , or  . 0 is returned if not met.   holds block dimensions (fixed or variable) set with matrix object creation routine.
- `i`: The row to query.

## See Also

- [func sparse_get_block_dimension_for_col(UnsafeMutableRawPointer!, sparse_index) -> Int](sparse_get_block_dimension_for_col(_:_:).md)
  Returns the dimension of the block for a specified column of a single-precision matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_get_block_dimension_for_row(_:_:))*