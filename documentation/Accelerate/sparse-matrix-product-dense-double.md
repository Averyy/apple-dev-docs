# sparse_matrix_product_dense_double(_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Multiplies the dense matrix  by the sparse matrix  and adds the result to the dense matrix , all with double-precision values.

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
func sparse_matrix_product_dense_double(_ order: CBLAS_ORDER, _ transa: CBLAS_TRANSPOSE, _ n: sparse_dimension, _ alpha: Double, _ A: sparse_matrix_double!, _ B: UnsafePointer<Double>!, _ ldb: sparse_dimension, _ C: UnsafeMutablePointer<Double>!, _ ldc: sparse_dimension) -> sparse_status
```

#### Return Value

On success, [`SPARSE_SUCCESS`](sparse_success.md) is returned and `C` has been updated with result of the operation.  Will return [`SPARSE_ILLEGAL_PARAMETER`](sparse_illegal_parameter.md) if order or `transa` is not valid or the leading dimension parameters do not meet their dimension requirements. On error, `C` is unchanged.

#### Discussion

Multiplies the dense matrix  by the sparse matrix  and adds the result to the dense matrix  (, where  is either  or the transpose of ). If  is of size , then  is of size  and  is of size .If the desired operation is , then an efficient option is to create the  buffer of zeros and then perform the operation with the zero filled .

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 19, iPadOS 19, macOS 16, tvOS 19, watchOS 19, and visionOS 3, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Parameters

- `order`: The storage order for the dense matrices   and  . Must be one of   or  .
- `transa`: Specifies whether to perform the operation with   or the transpose of  . Must be one of   or  .
- `n`: The number of columns of the matrices   and  .
- `alpha`: Scalar multiplier of  .
- `A`: The sparse matrix,  .
- `B`: Pointer to the dense matrix  . The number of rows must be equal to the number of columns of   and the number of columns is  . Behavior undefined if this is not met. The parameter   describes how many elements to move between one row (row major) or column (column major).
- `ldb`: Increment in elements between rows (row major) or columns (column major) of  . Must be greater than or equal to   when row major, or number of columns of   when column major.
- `C`: Pointer to the dense matrix  . The number of rows must be equal to the number of rows of   and the number of columns is  . Behavior undefined if this is not met. The argument   describes how many elements to move between one row (row major) or column (column major).   is updated with the result of the operation.
- `ldc`: Increment in elements between rows (row major) or columns (column major) of  . Must be greater than or equal to   when row major, or number of rows of   when column major.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_matrix_product_dense_double(_:_:_:_:_:_:_:_:_:))*