# Blockwise Matrix Operations

**Framework**: Accelerate

Create, insert values into, and extract values from a blockwise sparse matrix.

## Topics

### Matrix creation and population
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
- [func sparse_insert_block_float(sparse_matrix_float!, UnsafePointer<Float>!, sparse_dimension, sparse_dimension, sparse_index, sparse_index) -> sparse_status](sparse_insert_block_float(_:_:_:_:_:_:).md)
  Inserts a dense block of entries into a single-precision matrix.
- [func sparse_matrix_block_create_double_complex(sparse_dimension, sparse_dimension, sparse_dimension, sparse_dimension) -> sparse_matrix_double_complex!](sparse_matrix_block_create_double_complex(_:_:_:_:).md)
- [func sparse_matrix_block_create_float_complex(sparse_dimension, sparse_dimension, sparse_dimension, sparse_dimension) -> sparse_matrix_float_complex!](sparse_matrix_block_create_float_complex(_:_:_:_:).md)
### Complex matrix creation and population
- [func sparse_matrix_variable_block_create_double_complex(sparse_dimension, sparse_dimension, UnsafePointer<sparse_dimension>!, UnsafePointer<sparse_dimension>!) -> sparse_matrix_double_complex!](sparse_matrix_variable_block_create_double_complex(_:_:_:_:).md)
- [func sparse_matrix_variable_block_create_float_complex(sparse_dimension, sparse_dimension, UnsafePointer<sparse_dimension>!, UnsafePointer<sparse_dimension>!) -> sparse_matrix_float_complex!](sparse_matrix_variable_block_create_float_complex(_:_:_:_:).md)
### Value insertion
- [func sparse_insert_block_double_complex(sparse_matrix_double_complex!, OpaquePointer!, sparse_dimension, sparse_dimension, sparse_index, sparse_index) -> sparse_status](sparse_insert_block_double_complex(_:_:_:_:_:_:).md)
- [func sparse_insert_block_float_complex(sparse_matrix_float_complex!, OpaquePointer!, sparse_dimension, sparse_dimension, sparse_index, sparse_index) -> sparse_status](sparse_insert_block_float_complex(_:_:_:_:_:_:).md)
### Value extraction
- [func sparse_extract_block_double(sparse_matrix_double!, sparse_index, sparse_index, sparse_dimension, sparse_dimension, UnsafeMutablePointer<Double>!) -> sparse_status](sparse_extract_block_double(_:_:_:_:_:_:).md)
  Extracts values from a specified block of a double-precision matrix.
- [func sparse_extract_block_float(sparse_matrix_float!, sparse_index, sparse_index, sparse_dimension, sparse_dimension, UnsafeMutablePointer<Float>!) -> sparse_status](sparse_extract_block_float(_:_:_:_:_:_:).md)
  Extracts values from a specified block of a single-precision matrix.
- [func sparse_extract_block_double_complex(sparse_matrix_double_complex!, sparse_index, sparse_index, sparse_dimension, sparse_dimension, OpaquePointer!) -> sparse_status](sparse_extract_block_double_complex(_:_:_:_:_:_:).md)
- [func sparse_extract_block_float_complex(sparse_matrix_float_complex!, sparse_index, sparse_index, sparse_dimension, sparse_dimension, OpaquePointer!) -> sparse_status](sparse_extract_block_float_complex(_:_:_:_:_:_:).md)
### Block dimension queries
- [func sparse_get_block_dimension_for_row(UnsafeMutableRawPointer!, sparse_index) -> Int](sparse_get_block_dimension_for_row(_:_:).md)
  Returns the dimension of the block for a specified row of a double-precision matrix.
- [func sparse_get_block_dimension_for_col(UnsafeMutableRawPointer!, sparse_index) -> Int](sparse_get_block_dimension_for_col(_:_:).md)
  Returns the dimension of the block for a specified column of a single-precision matrix.
### Supporting types
- [typealias sparse_dimension](sparse_dimension.md)
  The dimension type.
- [typealias sparse_index](sparse_index.md)
  The index type.
- [typealias sparse_matrix_double](sparse_matrix_double.md)
  Sparse matrix opaque type for double.
- [typealias sparse_matrix_float](sparse_matrix_float.md)
  Sparse matrix opaque type for float.
- [struct sparse_status](sparse_status.md)
  The type reflecting the status of an operations.

## See Also

- [Matrix and Vector Operations](matrix-and-vector-operations.md)
  Perform computations with matrices and vectors.
- [Pointwise Matrix Operations](pointwise-matrix-operations.md)
  Create, insert values into, and extract values from a pointwise sparse matrix.
- [General Sparse Matrix Management Operations](general-sparse-matrix-management-operations.md)
  Manage and work with the properties of a sparse matrix.
- [Sparse Vector Utility Operations](sparse-vector-utility-operations.md)
  Create and work with sparse vector structures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/blockwise-matrix-operations)*