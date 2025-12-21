# sparse_permute_cols_double(_:_:)

**Framework**: Accelerate  
**Kind**: func

Permutes the columns of the double-precision sparse matrix  based on the provided permutation array.

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
func sparse_permute_cols_double(_ A: sparse_matrix_double!, _ perm: UnsafePointer<sparse_index>!) -> sparse_status
```

#### Return Value

On successful return, `A` has been permuted and [`SPARSE_SUCCESS`](sparse_success.md) is returned.

#### Discussion

Permute the columns of the sparse matrix  based on the provided permutation array. For each column in , swap columns as:

```swift
 tmp[:] = A[:,j];
 A[:,j] = A[:,perm[j]];
 A[:,perm[j]] = tmp[:];
```

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 26, iPadOS 26, macOS 26, tvOS 26, visionOS 26, and watchOS 26, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Parameters

- `A`: The sparse matrix,  .
- `perm`: The permutation array. Holds number of columns in   values indicating the permutation of the matrix. The indices in   are expected to be 0 based (first element of pointer is  ).  The indices in   are expected to be within bounds of the matrix. Undefined behavior if not met.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_permute_cols_double(_:_:))*