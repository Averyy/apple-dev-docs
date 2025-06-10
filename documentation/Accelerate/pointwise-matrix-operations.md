# Pointwise Matrix Operations

**Framework**: Accelerate

Create, insert values into, and extract values from a pointwise sparse matrix.

## Topics

### Matrix creation and population
- [func sparse_matrix_create_double(sparse_dimension, sparse_dimension) -> sparse_matrix_double!](sparse_matrix_create_double(_:_:).md)
  Returns a double-precision sparse matrix object.
- [func sparse_matrix_create_float(sparse_dimension, sparse_dimension) -> sparse_matrix_float!](sparse_matrix_create_float(_:_:).md)
  Returns a single-precision sparse matrix object.
- [func sparse_insert_entry_double(sparse_matrix_double!, Double, sparse_index, sparse_index) -> sparse_status](sparse_insert_entry_double(_:_:_:_:).md)
  Inserts a single scalar entry into a double-precision sparse matrix.
- [func sparse_insert_entry_float(sparse_matrix_float!, Float, sparse_index, sparse_index) -> sparse_status](sparse_insert_entry_float(_:_:_:_:).md)
  Inserts a single scalar entry into a single-precision sparse matrix.
- [func sparse_insert_entries_double(sparse_matrix_double!, sparse_dimension, UnsafePointer<Double>!, UnsafePointer<sparse_index>!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_entries_double(_:_:_:_:_:).md)
  Inserts a list of scalar entries into a double-precision sparse matrix.
- [func sparse_insert_entries_float(sparse_matrix_float!, sparse_dimension, UnsafePointer<Float>!, UnsafePointer<sparse_index>!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_entries_float(_:_:_:_:_:).md)
  Inserts a list of scalar entries into a single-precision sparse matrix.
- [func sparse_insert_col_double(sparse_matrix_double!, sparse_index, sparse_dimension, UnsafePointer<Double>!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_col_double(_:_:_:_:_:).md)
  Inserts a list of scalar entries into a single column of a double-precision sparse matrix.
- [func sparse_insert_col_float(sparse_matrix_float!, sparse_index, sparse_dimension, UnsafePointer<Float>!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_col_float(_:_:_:_:_:).md)
  Inserts a list of scalar entries into a single column of a single-precision sparse matrix.
- [func sparse_insert_row_double(sparse_matrix_double!, sparse_index, sparse_dimension, UnsafePointer<Double>!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_row_double(_:_:_:_:_:).md)
  Inserts a list of scalar entries into a single row of a double-precision sparse matrix.
- [func sparse_insert_row_float(sparse_matrix_float!, sparse_index, sparse_dimension, UnsafePointer<Float>!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_row_float(_:_:_:_:_:).md)
  Inserts a list of scalar entries into a single row of a single-precision sparse matrix.
### Complex matrix creation and population
- [func sparse_matrix_create_double_complex(sparse_dimension, sparse_dimension) -> sparse_matrix_double_complex!](sparse_matrix_create_double_complex(_:_:).md)
- [func sparse_matrix_create_float_complex(sparse_dimension, sparse_dimension) -> sparse_matrix_float_complex!](sparse_matrix_create_float_complex(_:_:).md)
### Value insertion
- [func sparse_insert_col_double_complex(sparse_matrix_double_complex!, sparse_index, sparse_dimension, OpaquePointer!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_col_double_complex(_:_:_:_:_:).md)
- [func sparse_insert_col_float_complex(sparse_matrix_float_complex!, sparse_index, sparse_dimension, OpaquePointer!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_col_float_complex(_:_:_:_:_:).md)
- [func sparse_insert_entries_double_complex(sparse_matrix_double_complex!, sparse_dimension, OpaquePointer!, UnsafePointer<sparse_index>!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_entries_double_complex(_:_:_:_:_:).md)
- [func sparse_insert_entries_float_complex(sparse_matrix_float_complex!, sparse_dimension, OpaquePointer!, UnsafePointer<sparse_index>!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_entries_float_complex(_:_:_:_:_:).md)
- [func sparse_insert_row_double_complex(sparse_matrix_double_complex!, sparse_index, sparse_dimension, OpaquePointer!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_row_double_complex(_:_:_:_:_:).md)
- [func sparse_insert_row_float_complex(sparse_matrix_float_complex!, sparse_index, sparse_dimension, OpaquePointer!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_row_float_complex(_:_:_:_:_:).md)
### Value extraction
- [func sparse_extract_sparse_row_double(sparse_matrix_double!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, UnsafeMutablePointer<Double>!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_row_double(_:_:_:_:_:_:_:).md)
  Extracts values from a specified row of a double-precision sparse matrix.
- [func sparse_extract_sparse_row_float(sparse_matrix_float!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_row_float(_:_:_:_:_:_:_:).md)
  Extracts values from a specified row of a single-precision sparse matrix.
- [func sparse_extract_sparse_column_double(sparse_matrix_double!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, UnsafeMutablePointer<Double>!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_column_double(_:_:_:_:_:_:_:).md)
  Extracts values from a specified column of a double-precision sparse matrix.
- [func sparse_extract_sparse_column_float(sparse_matrix_float!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_column_float(_:_:_:_:_:_:_:).md)
  Extracts values from a specified column of a single-precision sparse matrix.
- [func sparse_extract_sparse_column_double_complex(sparse_matrix_double_complex!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, OpaquePointer!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_column_double_complex(_:_:_:_:_:_:_:).md)
- [func sparse_extract_sparse_column_float_complex(sparse_matrix_float_complex!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, OpaquePointer!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_column_float_complex(_:_:_:_:_:_:_:).md)
- [func sparse_extract_sparse_row_float_complex(sparse_matrix_float_complex!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, OpaquePointer!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_row_float_complex(_:_:_:_:_:_:_:).md)
- [func sparse_extract_sparse_row_double_complex(sparse_matrix_double_complex!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, OpaquePointer!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_row_double_complex(_:_:_:_:_:_:_:).md)
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
- [Blockwise Matrix Operations](blockwise-matrix-operations.md)
  Create, insert values into, and extract values from a blockwise sparse matrix.
- [General Sparse Matrix Management Operations](general-sparse-matrix-management-operations.md)
  Manage and work with the properties of a sparse matrix.
- [Sparse Vector Utility Operations](sparse-vector-utility-operations.md)
  Create and work with sparse vector structures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/pointwise-matrix-operations)*