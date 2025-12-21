# sparse_extract_block_float(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Extracts values from a specified block of a single-precision matrix.

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
func sparse_extract_block_float(_ A: sparse_matrix_float!, _ bi: sparse_index, _ bj: sparse_index, _ row_stride: sparse_dimension, _ col_stride: sparse_dimension, _ val: UnsafeMutablePointer<Float>!) -> sparse_status
```

#### Return Value

On success [`SPARSE_SUCCESS`](sparse_success.md) is return and val has been updated with the block from block index `bi,bj`. If `A` creation requirements are not met, [`SPARSE_ILLEGAL_PARAMETER`](sparse_illegal_parameter.md) is returned and `val` is unchanged.

#### Discussion

Extract the `bi,bj`’th block from the sparse matrix `A`.

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 26, iPadOS 26, macOS 26, tvOS 26, visionOS 26, and watchOS 26, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Parameters

- `A`: The sparse matrix,  , which must have been created with   or  .   is returned if not met.   holds block dimensions (fixed or variable) set with matrix object creation routine.
- `bi`: The block row index for value extraction. Indices are 0 based (first block of matrix is  ).  Indices expected to be in the bounds of matrix dimensions, undefined behavior if not met.
- `bj`: The block column index for value extraction. Indices are 0 based (first block of matrix is  ).  Indices expected to be in the bounds of matrix dimensions, undefined behavior if not met.
- `row_stride`: The row stride in number of elements to move from one row to the next for the block  .
- `col_stride`: The column stride in number of elements to move from one column to the next for the block  .
- `val`: Pointer to dense block to place the extracted values.  Expected to be of size   where   is the block size for the matrix object at block index  . This dimensions is set at matrix object creation time.

## See Also

- [func sparse_extract_block_double(sparse_matrix_double!, sparse_index, sparse_index, sparse_dimension, sparse_dimension, UnsafeMutablePointer<Double>!) -> sparse_status](sparse_extract_block_double(_:_:_:_:_:_:).md)
  Extracts values from a specified block of a double-precision matrix.
- [func sparse_extract_block_double_complex(sparse_matrix_double_complex!, sparse_index, sparse_index, sparse_dimension, sparse_dimension, OpaquePointer!) -> sparse_status](sparse_extract_block_double_complex(_:_:_:_:_:_:).md)
- [func sparse_extract_block_float_complex(sparse_matrix_float_complex!, sparse_index, sparse_index, sparse_dimension, sparse_dimension, OpaquePointer!) -> sparse_status](sparse_extract_block_float_complex(_:_:_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_extract_block_float(_:_:_:_:_:_:))*