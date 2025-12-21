# sparse_matrix_variable_block_create_double(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a double-precision sparse matrix object that is stored in block-entry format with a variable block size.

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
func sparse_matrix_variable_block_create_double(_ Mb: sparse_dimension, _ Nb: sparse_dimension, _ K: UnsafePointer<sparse_dimension>!, _ L: UnsafePointer<sparse_dimension>!) -> sparse_matrix_double!
```

#### Return Value

A matrix object that is ready for receiving entries.  If an error occurs, `nil` is returned.

#### Discussion

Create a sparse matrix object that is stored in block-entry format and is ready to receive values from the various block insert routines. Blocks are are of variable dimension where the `i,j`’th block index has a dimension `K[i] * L[j]`. Block-entry format means blocks of dense regions will be stored at block indices `i,j`. For point wise format use non block version of create. See the various insert routines for details on inserting values into this matrix object.

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 26, iPadOS 26, macOS 26, tvOS 26, visionOS 26, and watchOS 26, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Parameters

- `Mb`: The number of rows in terms of blocks of the matrix.  Must be greater than 0.
- `Nb`: The number of columns in terms of blocks of the matrix.  Must be greater than 0.
- `K`: Array containing row dimensions of the blocks.  The  ’th row in terms of blocks will have a dimension  .   is expected to hold   elements. All values of   are expected to be greater than 0.
- `L`: Array containing column dimensions of the blocks.  The  ’th column in terms of blocks will have a dimension  .   is expected to hold Nb elements. All values of   are expected to be greater than 0.

## See Also

- [func sparse_matrix_block_create_double(sparse_dimension, sparse_dimension, sparse_dimension, sparse_dimension) -> sparse_matrix_double!](sparse_matrix_block_create_double(_:_:_:_:).md)
  Returns a double-precision sparse matrix object that is stored in block-entry format with a fixed block size.
- [func sparse_matrix_block_create_float(sparse_dimension, sparse_dimension, sparse_dimension, sparse_dimension) -> sparse_matrix_float!](sparse_matrix_block_create_float(_:_:_:_:).md)
  Returns a single-precision sparse matrix object that is stored in block-entry format with a fixed block size.
- [func sparse_matrix_variable_block_create_float(sparse_dimension, sparse_dimension, UnsafePointer<sparse_dimension>!, UnsafePointer<sparse_dimension>!) -> sparse_matrix_float!](sparse_matrix_variable_block_create_float(_:_:_:_:).md)
  Returns a single-precision sparse matrix object that is stored in block-entry format with a variable block size.
- [func sparse_insert_block_double(sparse_matrix_double!, UnsafePointer<Double>!, sparse_dimension, sparse_dimension, sparse_index, sparse_index) -> sparse_status](sparse_insert_block_double(_:_:_:_:_:_:).md)
  Inserts a dense block of entries into a double-precision matrix.
- [func sparse_insert_block_float(sparse_matrix_float!, UnsafePointer<Float>!, sparse_dimension, sparse_dimension, sparse_index, sparse_index) -> sparse_status](sparse_insert_block_float(_:_:_:_:_:_:).md)
  Inserts a dense block of entries into a single-precision matrix.
- [func sparse_matrix_block_create_double_complex(sparse_dimension, sparse_dimension, sparse_dimension, sparse_dimension) -> sparse_matrix_double_complex!](sparse_matrix_block_create_double_complex(_:_:_:_:).md)
- [func sparse_matrix_block_create_float_complex(sparse_dimension, sparse_dimension, sparse_dimension, sparse_dimension) -> sparse_matrix_float_complex!](sparse_matrix_block_create_float_complex(_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_matrix_variable_block_create_double(_:_:_:_:))*