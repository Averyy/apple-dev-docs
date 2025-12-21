# sparse_insert_block_float(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Inserts a dense block of entries into a single-precision matrix.

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
func sparse_insert_block_float(_ A: sparse_matrix_float!, _ val: UnsafePointer<Float>!, _ row_stride: sparse_dimension, _ col_stride: sparse_dimension, _ bi: sparse_index, _ bj: sparse_index) -> sparse_status
```

#### Return Value

On successful insertion, `A` has been updated with the value and [`SPARSE_SUCCESS`](sparse_success.md) is returned. If `A` creation requirements are not met, [`SPARSE_ILLEGAL_PARAMETER`](sparse_illegal_parameter.md) is returned and `A` is unchanged.

#### Discussion

Use to build a sparse matrix by providing a dense block for entry at block location `A[bi,bj]`. Block size is determined at object creation time. Given a block dimension of `k * l` and for location `bi,bj`, update as: `A[bi,bj][i,j] = val[i*row_stride + j*col_stride]` for each `i` in `k` and each `j` in `l`.

Note that matrix properties cannot be modified after value insertion begins.This includes properties such as specifying a triangular matrix.Insertion can be expensive, generally speaking it is best to do a batch update. Inserted values may be temporarily held internally within the object and only inserted into the sparse format when a later computation triggers a need to insert.

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 26, iPadOS 26, macOS 26, tvOS 26, visionOS 26, and watchOS 26, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Parameters

- `A`: The sparse matrix,  ,_ _which must have been created with   or  .   is returned if not met.   holds block dimensions (fixed or variable) set with matrix object creation routine.
- `val`: Pointer to block to be inserted at block index location  . The block is of dimension   where   and   are set for   at object creation time. The strides between elements for rows and columns are provided in   and  .
- `row_stride`: The row stride in number of elements to move from one row to the next for the block  .
- `col_stride`: The column stride in number of elements to move from one column to the next for the block  .
- `bi`: The block row index where   is to be inserted. Indexing is zero based, the first block is located at  .  Index is assumed to be within the bounds of the matrix object, undefined behavior if not met.
- `bj`: The block column index where   is to be inserted. Indexing is zero based, the first block is located at  .  Index is assumed to be within the bounds of the matrix object, undefined behavior if not met.

## See Also

- [func sparse_matrix_block_create_double(sparse_dimension, sparse_dimension, sparse_dimension, sparse_dimension) -> sparse_matrix_double!](sparse_matrix_block_create_double(_:_:_:_:).md)
  Returns a double-precision sparse matrix object that is stored in block-entry format with a fixed block size.
- [func sparse_matrix_block_create_float(sparse_dimension, sparse_dimension, sparse_dimension, sparse_dimension) -> sparse_matrix_float!](sparse_matrix_block_create_float(_:_:_:_:).md)
  Returns a single-precision sparse matrix object that is stored in block-entry format with a fixed block size.
- [func sparse_matrix_variable_block_create_double(sparse_dimension, sparse_dimension, UnsafePointer<sparse_dimension>!, UnsafePointer<sparse_dimension>!) -> sparse_matrix_double!](sparse_matrix_variable_block_create_double(_:_:_:_:).md)
  Returns a double-precision sparse matrix object that is stored in block-entry format with a variable block size.
- [func sparse_matrix_variable_block_create_float(sparse_dimension, sparse_dimension, UnsafePointer<sparse_dimension>!, UnsafePointer<sparse_dimension>!) -> sparse_matrix_float!](sparse_matrix_variable_block_create_float(_:_:_:_:).md)
  Returns a single-precision sparse matrix object that is stored in block-entry format with a variable block size.
- [func sparse_insert_block_double(sparse_matrix_double!, UnsafePointer<Double>!, sparse_dimension, sparse_dimension, sparse_index, sparse_index) -> sparse_status](sparse_insert_block_double(_:_:_:_:_:_:).md)
  Inserts a dense block of entries into a double-precision matrix.
- [func sparse_matrix_block_create_double_complex(sparse_dimension, sparse_dimension, sparse_dimension, sparse_dimension) -> sparse_matrix_double_complex!](sparse_matrix_block_create_double_complex(_:_:_:_:).md)
- [func sparse_matrix_block_create_float_complex(sparse_dimension, sparse_dimension, sparse_dimension, sparse_dimension) -> sparse_matrix_float_complex!](sparse_matrix_block_create_float_complex(_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_insert_block_float(_:_:_:_:_:_:))*