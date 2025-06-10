# Matrix and Vector Operations

**Framework**: Accelerate

Perform computations with matrices and vectors.

## Topics

### Complex vector operations
- [func sparse_pack_vector_double_complex(sparse_dimension, sparse_dimension, OpaquePointer!, sparse_stride, OpaquePointer!, UnsafeMutablePointer<sparse_index>!) -> Int](sparse_pack_vector_double_complex(_:_:_:_:_:_:).md)
- [func sparse_pack_vector_float_complex(sparse_dimension, sparse_dimension, OpaquePointer!, sparse_stride, OpaquePointer!, UnsafeMutablePointer<sparse_index>!) -> Int](sparse_pack_vector_float_complex(_:_:_:_:_:_:).md)
- [func sparse_unpack_vector_double_complex(sparse_dimension, sparse_dimension, Bool, OpaquePointer!, UnsafePointer<sparse_index>!, OpaquePointer!, sparse_stride)](sparse_unpack_vector_double_complex(_:_:_:_:_:_:_:).md)
- [func sparse_unpack_vector_float_complex(sparse_dimension, sparse_dimension, Bool, OpaquePointer!, UnsafePointer<sparse_index>!, OpaquePointer!, sparse_stride)](sparse_unpack_vector_float_complex(_:_:_:_:_:_:_:).md)
- [func sparse_vector_norm_double_complex(sparse_dimension, OpaquePointer!, UnsafePointer<sparse_index>!, sparse_norm) -> Double](sparse_vector_norm_double_complex(_:_:_:_:).md)
- [func sparse_vector_norm_float_complex(sparse_dimension, OpaquePointer!, UnsafePointer<sparse_index>!, sparse_norm) -> Float](sparse_vector_norm_float_complex(_:_:_:_:).md)
### Complex matrix operations
- [func sparse_elementwise_norm_double_complex(sparse_matrix_double_complex!, sparse_norm) -> Double](sparse_elementwise_norm_double_complex(_:_:).md)
- [func sparse_elementwise_norm_float_complex(sparse_matrix_float_complex!, sparse_norm) -> Float](sparse_elementwise_norm_float_complex(_:_:).md)
- [func sparse_get_vector_nonzero_count_double_complex(sparse_dimension, OpaquePointer!, sparse_stride) -> Int](sparse_get_vector_nonzero_count_double_complex(_:_:_:).md)
- [func sparse_get_vector_nonzero_count_float_complex(sparse_dimension, OpaquePointer!, sparse_stride) -> Int](sparse_get_vector_nonzero_count_float_complex(_:_:_:).md)
- [func sparse_operator_norm_double_complex(sparse_matrix_double_complex!, sparse_norm) -> Double](sparse_operator_norm_double_complex(_:_:).md)
- [func sparse_operator_norm_float_complex(sparse_matrix_float_complex!, sparse_norm) -> Float](sparse_operator_norm_float_complex(_:_:).md)
- [func sparse_permute_cols_double_complex(sparse_matrix_double_complex!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_permute_cols_double_complex(_:_:).md)
- [func sparse_permute_cols_float_complex(sparse_matrix_float_complex!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_permute_cols_float_complex(_:_:).md)
- [func sparse_permute_rows_double_complex(sparse_matrix_double_complex!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_permute_rows_double_complex(_:_:).md)
- [func sparse_permute_rows_float_complex(sparse_matrix_float_complex!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_permute_rows_float_complex(_:_:).md)
- [func sparse_permute_rows_float_complex(sparse_matrix_float_complex!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_permute_rows_float_complex(_:_:).md)
### Matrix-Matrix Operations
- [func sparse_matrix_product_dense_double(CBLAS_ORDER, CBLAS_TRANSPOSE, sparse_dimension, Double, sparse_matrix_double!, UnsafePointer<Double>!, sparse_dimension, UnsafeMutablePointer<Double>!, sparse_dimension) -> sparse_status](sparse_matrix_product_dense_double(_:_:_:_:_:_:_:_:_:).md)
  Multiplies the dense matrix  by the sparse matrix  and adds the result to the dense matrix , all with double-precision values.
- [func sparse_matrix_product_dense_float(CBLAS_ORDER, CBLAS_TRANSPOSE, sparse_dimension, Float, sparse_matrix_float!, UnsafePointer<Float>!, sparse_dimension, UnsafeMutablePointer<Float>!, sparse_dimension) -> sparse_status](sparse_matrix_product_dense_float(_:_:_:_:_:_:_:_:_:).md)
  Multiplies the dense matrix  by the sparse matrix  and adds the result to the dense matrix , all with single-precision values.
- [func sparse_matrix_product_sparse_double(CBLAS_ORDER, CBLAS_TRANSPOSE, Double, sparse_matrix_double!, sparse_matrix_double!, UnsafeMutablePointer<Double>!, sparse_dimension) -> sparse_status](sparse_matrix_product_sparse_double(_:_:_:_:_:_:_:).md)
  Multiplies the sparse matrix  by the sparse matrix  and adds the result to the dense matrix , all with double-precision values.
- [func sparse_matrix_product_sparse_float(CBLAS_ORDER, CBLAS_TRANSPOSE, Float, sparse_matrix_float!, sparse_matrix_float!, UnsafeMutablePointer<Float>!, sparse_dimension) -> sparse_status](sparse_matrix_product_sparse_float(_:_:_:_:_:_:_:).md)
  Multiplies the sparse matrix  by the sparse matrix  and adds the result to the dense matrix , all with single-precision values.
- [func sparse_matrix_triangular_solve_dense_double(CBLAS_ORDER, CBLAS_TRANSPOSE, sparse_dimension, Double, sparse_matrix_double!, UnsafeMutablePointer<Double>!, sparse_dimension) -> sparse_status](sparse_matrix_triangular_solve_dense_double(_:_:_:_:_:_:_:).md)
  Solves the system of equations  for  where  is a dense matrix and  is a triangular sparse matrix, both with double-precision values.
- [func sparse_matrix_triangular_solve_dense_float(CBLAS_ORDER, CBLAS_TRANSPOSE, sparse_dimension, Float, sparse_matrix_float!, UnsafeMutablePointer<Float>!, sparse_dimension) -> sparse_status](sparse_matrix_triangular_solve_dense_float(_:_:_:_:_:_:_:).md)
  Solves the system of equations  for  where  is a dense matrix and  is a triangular sparse matrix, both with double-precision values.
### Matrix-Vector Operations
- [func sparse_matrix_vector_product_dense_double(CBLAS_TRANSPOSE, Double, sparse_matrix_double!, UnsafePointer<Double>!, sparse_stride, UnsafeMutablePointer<Double>!, sparse_stride) -> sparse_status](sparse_matrix_vector_product_dense_double(_:_:_:_:_:_:_:).md)
  Multiplies the dense vector  by the sparse matrix  and adds the result to the dense vector , with all operands containing double-precision values.
- [func sparse_matrix_vector_product_dense_float(CBLAS_TRANSPOSE, Float, sparse_matrix_float!, UnsafePointer<Float>!, sparse_stride, UnsafeMutablePointer<Float>!, sparse_stride) -> sparse_status](sparse_matrix_vector_product_dense_float(_:_:_:_:_:_:_:).md)
  Multiplies the dense vector  by the sparse matrix  and adds the result to the dense vector , with all operands containing single-precision values.
- [func sparse_vector_triangular_solve_dense_double(CBLAS_TRANSPOSE, Double, sparse_matrix_double!, UnsafeMutablePointer<Double>!, sparse_stride) -> sparse_status](sparse_vector_triangular_solve_dense_double(_:_:_:_:_:).md)
  Solves the system of equations  for x where  is a dense vector and  is a triangular sparse matrix, with all operands containing double-precision values.
- [func sparse_vector_triangular_solve_dense_float(CBLAS_TRANSPOSE, Float, sparse_matrix_float!, UnsafeMutablePointer<Float>!, sparse_stride) -> sparse_status](sparse_vector_triangular_solve_dense_float(_:_:_:_:_:).md)
  Solves the system of equations  for x where  is a dense vector and  is a triangular sparse matrix, with all operands containing single-precision values.
- [func sparse_outer_product_dense_double(sparse_dimension, sparse_dimension, sparse_dimension, Double, UnsafePointer<Double>!, sparse_stride, UnsafePointer<Double>!, UnsafePointer<sparse_index>!, UnsafeMutablePointer<sparse_matrix_double?>!) -> sparse_status](sparse_outer_product_dense_double(_:_:_:_:_:_:_:_:_:).md)
  Computes the outer product of the dense vector  and the sparse vector , with both operands containing double-precision values.
- [func sparse_outer_product_dense_float(sparse_dimension, sparse_dimension, sparse_dimension, Float, UnsafePointer<Float>!, sparse_stride, UnsafePointer<Float>!, UnsafePointer<sparse_index>!, UnsafeMutablePointer<sparse_matrix_float?>!) -> sparse_status](sparse_outer_product_dense_float(_:_:_:_:_:_:_:_:_:).md)
  Computes the outer product of the dense vector  and the sparse vector , with both operands containing single-precision values.
- [func sparse_permute_rows_double(sparse_matrix_double!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_permute_rows_double(_:_:).md)
  Permutes the rows of the double-precision sparse matrix  based on the provided permutation array.
- [func sparse_permute_rows_float(sparse_matrix_float!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_permute_rows_float(_:_:).md)
  Permutes the rows of the single-precision sparse matrix  based on the provided permutation array.
- [func sparse_permute_cols_double(sparse_matrix_double!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_permute_cols_double(_:_:).md)
  Permutes the columns of the double-precision sparse matrix  based on the provided permutation array.
- [func sparse_permute_cols_float(sparse_matrix_float!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_permute_cols_float(_:_:).md)
  Permutes the columns of the single-precision sparse matrix  based on the provided permutation array.
- [func sparse_elementwise_norm_double(sparse_matrix_double!, sparse_norm) -> Double](sparse_elementwise_norm_double(_:_:).md)
  Computes the specified element-wise norm of the double-precision sparse matrix .
- [func sparse_elementwise_norm_float(sparse_matrix_float!, sparse_norm) -> Float](sparse_elementwise_norm_float(_:_:).md)
  Computes the specified element-wise norm of the single-precision sparse matrix .
- [func sparse_operator_norm_double(sparse_matrix_double!, sparse_norm) -> Double](sparse_operator_norm_double(_:_:).md)
  Computes the specified operator norm of the double-precision sparse matrix .
- [func sparse_operator_norm_float(sparse_matrix_float!, sparse_norm) -> Float](sparse_operator_norm_float(_:_:).md)
  Computes the specified operator norm of the single-precision sparse matrix .
- [func sparse_matrix_trace_double(sparse_matrix_double!, sparse_index) -> Double](sparse_matrix_trace_double(_:_:).md)
  Computes the sum along the specified diagonal of the double-precision sparse matrix .
- [func sparse_matrix_trace_float(sparse_matrix_float!, sparse_index) -> Float](sparse_matrix_trace_float(_:_:).md)
  Computes the sum along the specified diagonal of the single-precision sparse matrix .
### Vector-Vector Operations
- [func sparse_inner_product_dense_double(sparse_dimension, UnsafePointer<Double>!, UnsafePointer<sparse_index>!, UnsafePointer<Double>!, sparse_stride) -> Double](sparse_inner_product_dense_double(_:_:_:_:_:).md)
  Computes the inner product of sparse vector  with double-precision , with both vectors containing double-precision values.
- [func sparse_inner_product_dense_float(sparse_dimension, UnsafePointer<Float>!, UnsafePointer<sparse_index>!, UnsafePointer<Float>!, sparse_stride) -> Float](sparse_inner_product_dense_float(_:_:_:_:_:).md)
  Computes the inner product of sparse vector  with dense vector  with both vectors containing single-precision values.
- [func sparse_inner_product_sparse_double(sparse_dimension, sparse_dimension, UnsafePointer<Double>!, UnsafePointer<sparse_index>!, UnsafePointer<Double>!, UnsafePointer<sparse_index>!) -> Double](sparse_inner_product_sparse_double(_:_:_:_:_:_:).md)
  Computes the inner product of sparse vector  with sparse vector  with both vectors containing double-precision values.
- [func sparse_inner_product_sparse_float(sparse_dimension, sparse_dimension, UnsafePointer<Float>!, UnsafePointer<sparse_index>!, UnsafePointer<Float>!, UnsafePointer<sparse_index>!) -> Float](sparse_inner_product_sparse_float(_:_:_:_:_:_:).md)
  Computes the inner product of sparse vector  with sparse vector  with both vectors containing single-precision values.
- [func sparse_vector_add_with_scale_dense_double(sparse_dimension, Double, UnsafePointer<Double>!, UnsafePointer<sparse_index>!, UnsafeMutablePointer<Double>!, sparse_stride)](sparse_vector_add_with_scale_dense_double(_:_:_:_:_:_:).md)
  Scales the sparse vector  by  and adds the result to the dense vector  with both vectors containing double-precision values.
- [func sparse_vector_add_with_scale_dense_float(sparse_dimension, Float, UnsafePointer<Float>!, UnsafePointer<sparse_index>!, UnsafeMutablePointer<Float>!, sparse_stride)](sparse_vector_add_with_scale_dense_float(_:_:_:_:_:_:).md)
  Scales the sparse vector  by  and adds the result to the dense vector  with both vectors containing single-precision values.
- [func sparse_vector_norm_double(sparse_dimension, UnsafePointer<Double>!, UnsafePointer<sparse_index>!, sparse_norm) -> Double](sparse_vector_norm_double(_:_:_:_:).md)
  Computes the specified norm of the double-precision sparse vector .
- [func sparse_vector_norm_float(sparse_dimension, UnsafePointer<Float>!, UnsafePointer<sparse_index>!, sparse_norm) -> Float](sparse_vector_norm_float(_:_:_:_:).md)
  Computes the specified norm of the single-precision sparse vector .
### Supporting Types
- [typealias sparse_matrix_double](sparse_matrix_double.md)
  Sparse matrix opaque type for double.
- [typealias sparse_matrix_float](sparse_matrix_float.md)
  Sparse matrix opaque type for float.
- [struct sparse_status](sparse_status.md)
  The type reflecting the status of an operations.
- [typealias sparse_dimension](sparse_dimension.md)
  The dimension type.
- [typealias sparse_index](sparse_index.md)
  The index type.
- [struct sparse_norm](sparse_norm.md)
  The norm specifier.
- [typealias sparse_stride](sparse_stride.md)
  The stride type.

## See Also

- [Pointwise Matrix Operations](pointwise-matrix-operations.md)
  Create, insert values into, and extract values from a pointwise sparse matrix.
- [Blockwise Matrix Operations](blockwise-matrix-operations.md)
  Create, insert values into, and extract values from a blockwise sparse matrix.
- [General Sparse Matrix Management Operations](general-sparse-matrix-management-operations.md)
  Manage and work with the properties of a sparse matrix.
- [Sparse Vector Utility Operations](sparse-vector-utility-operations.md)
  Create and work with sparse vector structures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/matrix-and-vector-operations)*