# sparse_operator_norm_double(_:_:)

**Framework**: Accelerate  
**Kind**: func

Computes the specified operator norm of the double-precision sparse matrix .

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
func sparse_operator_norm_double(_ A: sparse_matrix_double!, _ norm: sparse_norm) -> Double
```

#### Return Value

The requested norm.

#### Discussion

This is the norm of the matrix treated as an linear operator, not the element-wise norm.  Specify one of:

| [`SPARSE_NORM_ONE`](sparse_norm_one.md) |  | |—|—| | [`SPARSE_NORM_TWO`](sparse_norm_two.md) | Maximum singular value. This is significantly more expensive to compute than the other norms. | | [`SPARSE_NORM_INF`](sparse_norm_inf.md) |  | | [`SPARSE_NORM_R1`](sparse_norm_r1.md) | Not supported, undefined. |

If norm is not one of the enumerated norm types, the default value is [`SPARSE_NORM_INF`](sparse_norm_inf.md).

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 19, iPadOS 19, macOS 16, tvOS 19, watchOS 19, and visionOS 3, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Parameters

- `A`: The sparse matrix,  .
- `norm`: Specify the norm to be computed. Must be one of  ,  , or  . See discussion for further details.

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
- [func sparse_permute_cols_double(sparse_matrix_double!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_permute_cols_double(_:_:).md)
  Permutes the columns of the double-precision sparse matrix  based on the provided permutation array.
- [func sparse_permute_cols_float(sparse_matrix_float!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_permute_cols_float(_:_:).md)
  Permutes the columns of the single-precision sparse matrix  based on the provided permutation array.
- [func sparse_elementwise_norm_double(sparse_matrix_double!, sparse_norm) -> Double](sparse_elementwise_norm_double(_:_:).md)
  Computes the specified element-wise norm of the double-precision sparse matrix .
- [func sparse_elementwise_norm_float(sparse_matrix_float!, sparse_norm) -> Float](sparse_elementwise_norm_float(_:_:).md)
  Computes the specified element-wise norm of the single-precision sparse matrix .
- [func sparse_operator_norm_float(sparse_matrix_float!, sparse_norm) -> Float](sparse_operator_norm_float(_:_:).md)
  Computes the specified operator norm of the single-precision sparse matrix .
- [func sparse_matrix_trace_double(sparse_matrix_double!, sparse_index) -> Double](sparse_matrix_trace_double(_:_:).md)
  Computes the sum along the specified diagonal of the double-precision sparse matrix .
- [func sparse_matrix_trace_float(sparse_matrix_float!, sparse_index) -> Float](sparse_matrix_trace_float(_:_:).md)
  Computes the sum along the specified diagonal of the single-precision sparse matrix .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_operator_norm_double(_:_:))*