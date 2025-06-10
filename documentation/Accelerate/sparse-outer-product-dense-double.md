# sparse_outer_product_dense_double(_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Computes the outer product of the dense vector  and the sparse vector , with both operands containing double-precision values.

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
func sparse_outer_product_dense_double(_ M: sparse_dimension, _ N: sparse_dimension, _ nz: sparse_dimension, _ alpha: Double, _ x: UnsafePointer<Double>!, _ incx: sparse_stride, _ y: UnsafePointer<Double>!, _ indy: UnsafePointer<sparse_index>!, _ C: UnsafeMutablePointer<sparse_matrix_double?>!) -> sparse_status
```

#### Return Value

On success [`SPARSE_SUCCESS`](sparse_success.md) is returned an `C` is valid matrix object.  The caller is responsible for cleaning up the sparse matrix object with [`sparse_matrix_destroy(_:)`](sparse_matrix_destroy(_:).md).

#### Discussion

Will return [`SPARSE_ILLEGAL_PARAMETER`](sparse_illegal_parameter.md) if `nz > N`, and `C` will be unchanged.

#### Discussion

Compute the outer product of the dense vector x and the sparse vector y and return a new sparse matrix in the uninitialized pointer sparse matrix pointer `C`.  `C = alpha * x * y'`.  You are responsible for calling [`sparse_matrix_destroy(_:)`](sparse_matrix_destroy(_:).md) on the returned matrix.The matrix object returned on success is a point wise based sparse matrix.

Indices in `indx` are always assumed to be stored in ascending order. Additionally, indices are assumed to be unique.  The behavior of this function is undefined if either of these assumptions are not met.

All indices are 0 based (the first element of a pointer is `ptr[0]`).

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 19, iPadOS 19, macOS 16, tvOS 19, watchOS 19, and visionOS 3, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Parameters

- `M`: The number of rows of   and the resulting matrix.
- `N`: The number of columns of the resulting matrix. The number of nonzero values must be less than or equal to  .
- `nz`: The number of nonzero values in the sparse vector  . Must be less than or equal to  .
- `alpha`: Scalar multiplier of  .
- `x`: Pointer to the dense vector  . Must be   number of elements. Negative strides  are supported.  Note, unlike dense BLAS routines, the pointer points to the last element when stride is negative.
- `incx`: Increment between valid values in the dense vector  .  Negative strides are supported.
- `y`: Pointer to the dense storage for the values of the sparse vector  . The corresponding entry in   holds the index of the value.  Contains   values.
- `indy`: Pointer to the dense storage for the index values of the sparse vector y.  The corresponding entry in   holds the values of the vector.  Contains   values.
- `C`: Pointer to an uninitialized sparse matrix object.  On success a newly allocated sparse matrix object is returned in this pointer.  On error, this set to  .You are responsible for calling   on this matrix object.

## See Also

- [func sparse_matrix_vector_product_dense_double(CBLAS_TRANSPOSE, Double, sparse_matrix_double!, UnsafePointer<Double>!, sparse_stride, UnsafeMutablePointer<Double>!, sparse_stride) -> sparse_status](sparse_matrix_vector_product_dense_double(_:_:_:_:_:_:_:).md)
  Multiplies the dense vector  by the sparse matrix  and adds the result to the dense vector , with all operands containing double-precision values.
- [func sparse_matrix_vector_product_dense_float(CBLAS_TRANSPOSE, Float, sparse_matrix_float!, UnsafePointer<Float>!, sparse_stride, UnsafeMutablePointer<Float>!, sparse_stride) -> sparse_status](sparse_matrix_vector_product_dense_float(_:_:_:_:_:_:_:).md)
  Multiplies the dense vector  by the sparse matrix  and adds the result to the dense vector , with all operands containing single-precision values.
- [func sparse_vector_triangular_solve_dense_double(CBLAS_TRANSPOSE, Double, sparse_matrix_double!, UnsafeMutablePointer<Double>!, sparse_stride) -> sparse_status](sparse_vector_triangular_solve_dense_double(_:_:_:_:_:).md)
  Solves the system of equations  for x where  is a dense vector and  is a triangular sparse matrix, with all operands containing double-precision values.
- [func sparse_vector_triangular_solve_dense_float(CBLAS_TRANSPOSE, Float, sparse_matrix_float!, UnsafeMutablePointer<Float>!, sparse_stride) -> sparse_status](sparse_vector_triangular_solve_dense_float(_:_:_:_:_:).md)
  Solves the system of equations  for x where  is a dense vector and  is a triangular sparse matrix, with all operands containing single-precision values.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_outer_product_dense_double(_:_:_:_:_:_:_:_:_:))*