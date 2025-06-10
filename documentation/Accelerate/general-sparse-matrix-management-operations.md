# General Sparse Matrix Management Operations

**Framework**: Accelerate

Manage and work with the properties of a sparse matrix.

## Topics

### General Sparse Matrix Management Operations
- [func sparse_commit(UnsafeMutableRawPointer!) -> sparse_status](sparse_commit(_:).md)
  Puts values that you recently added to the matrix into the internal sparse storage format.
- [func sparse_matrix_destroy(UnsafeMutableRawPointer!) -> sparse_status](sparse_matrix_destroy(_:).md)
  Releases any memory associated with the matrix object.
- [func sparse_set_matrix_property(UnsafeMutableRawPointer!, sparse_matrix_property) -> sparse_status](sparse_set_matrix_property(_:_:).md)
  Sets the given property for a matrix object.
- [func sparse_get_matrix_property(UnsafeMutableRawPointer!, sparse_matrix_property) -> Int](sparse_get_matrix_property(_:_:).md)
  Returns the value of the given property name.
- [func sparse_get_matrix_number_of_rows(UnsafeMutableRawPointer!) -> sparse_dimension](sparse_get_matrix_number_of_rows(_:).md)
  Returns the number of rows of a matrix.
- [func sparse_get_matrix_number_of_columns(UnsafeMutableRawPointer!) -> sparse_dimension](sparse_get_matrix_number_of_columns(_:).md)
  Returns the number of columns of a matrix.
- [func sparse_get_matrix_nonzero_count(UnsafeMutableRawPointer!) -> Int](sparse_get_matrix_nonzero_count(_:).md)
  Returns the number of nonzero values of a matrix.
- [func sparse_get_matrix_nonzero_count_for_row(UnsafeMutableRawPointer!, sparse_index) -> Int](sparse_get_matrix_nonzero_count_for_row(_:_:).md)
  Returns the number of nonzero values in a row of a matrix.
- [func sparse_get_matrix_nonzero_count_for_column(UnsafeMutableRawPointer!, sparse_index) -> Int](sparse_get_matrix_nonzero_count_for_column(_:_:).md)
  Returns the number of nonzero values in a column of a matrix.
### Supporting Types
- [typealias sparse_dimension](sparse_dimension.md)
  The dimension type.
- [typealias sparse_index](sparse_index.md)
  The index type.
- [struct sparse_matrix_property](sparse_matrix_property.md)
  The matrix property type.

## See Also

- [Matrix and Vector Operations](matrix-and-vector-operations.md)
  Perform computations with matrices and vectors.
- [Pointwise Matrix Operations](pointwise-matrix-operations.md)
  Create, insert values into, and extract values from a pointwise sparse matrix.
- [Blockwise Matrix Operations](blockwise-matrix-operations.md)
  Create, insert values into, and extract values from a blockwise sparse matrix.
- [Sparse Vector Utility Operations](sparse-vector-utility-operations.md)
  Create and work with sparse vector structures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/general-sparse-matrix-management-operations)*