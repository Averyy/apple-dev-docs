# sparse_matrix_triangular_solve_dense_float(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Solves the system of equations  for  where  is a dense matrix and  is a triangular sparse matrix, both with double-precision values.

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
func sparse_matrix_triangular_solve_dense_float(_ order: CBLAS_ORDER, _ transt: CBLAS_TRANSPOSE, _ nrhs: sparse_dimension, _ alpha: Float, _ T: sparse_matrix_float!, _ B: UnsafeMutablePointer<Float>!, _ ldb: sparse_dimension) -> sparse_status
```

#### Return Value

On success, [`SPARSE_SUCCESS`](sparse_success.md) is returned and  has been updated with result of the operation.  Will return [`SPARSE_ILLEGAL_PARAMETER`](sparse_illegal_parameter.md) if either of order or `transt` are invalid or the `ldb` does not meet its dimension requirements.  On error,  is unchanged.

#### Discussion

If  is of size , then  must be of size  `nrhs`. The matrix  must be an upper or lower triangular matrix.

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 26, iPadOS 26, macOS 26, tvOS 26, visionOS 26, and watchOS 26, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Parameters

- `order`: Specified the storage order for the dense matrix  . Must be one of   or  .
- `transt`: Specifies whether to perform the operation with   or the transpose of  . Must be one of   or  .
- `nrhs`: The number of columns of the matrix  .
- `alpha`: Scalar multiplier of  .
- `T`: The sparse triangular matrix,  .  Must be upper or lower triangular matrix. Will return   if not a triangular matrix.
- `B`: Pointer to the dense matrix  . The number of rows must be equal to the number of columns of   and the number of columns is  .  Behavior undefined if this is not met. The argument   describes how many elements to move between one row (row major) or column (column major). On exit holds the solution to the system of equations.
- `ldb`: Increment in elements between rows (row major) or columns (column major) of  . Must be greater than or equal to   when row major, or number of columns of   when column major.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_matrix_triangular_solve_dense_float(_:_:_:_:_:_:_:))*