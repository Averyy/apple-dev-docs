# sparse_matrix_product_sparse_float(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Multiplies the sparse matrix *B* by the sparse matrix *A* and adds the result to the dense matrix *C*, all with single-precision values.

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
func sparse_matrix_product_sparse_float(_ order: CBLAS_ORDER, _ transa: CBLAS_TRANSPOSE, _ alpha: Float, _ A: sparse_matrix_float!, _ B: sparse_matrix_float!, _ C: UnsafeMutablePointer<Float>!, _ ldc: sparse_dimension) -> sparse_status
```

#### Return Value

On success, [`SPARSE_SUCCESS`](sparse_success.md) is returned and `C` has been updated with result of the operation.  Will return [`SPARSE_ILLEGAL_PARAMETER`](sparse_illegal_parameter.md) if order or `transa` is not valid or the leading dimension parameters do not meet their dimension requirements. On error, `C` is unchanged.

#### Discussion

Multiplies the sparse matrix *B* by the sparse matrix *A* and adds the result to the dense matrix *C* (*C = alpha * op(A) * B + C*, where *op(A)* is either *A* or the transpose of *A*). If *A* is of size *M x K*, then *B* is of size *K x N* and *C* is of size *M x N*.If the desired operation is *C = A * B*, then an efficient option is to create the *C* buffer of zeros and then perform the operation with the zero filled *C*.

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 26, iPadOS 26, macOS 26, tvOS 26, visionOS 26, and watchOS 26, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings under Apple Clang - Preprocessing > Preprocessor Macros.

## Parameters

- `order`: The storage order for the dense matrix *C*. Must be one of `CblasRowMajor` or `CblasColMajor`.
- `transa`: Specifies whether to perform the operation with *A* or the transpose of *A*. Must be one of `CblasNoTrans` or `CblasTrans`.
- `alpha`: Scalar multiplier of *A*.
- `A`: The sparse matrix, *A*.
- `B`: The sparse matrix, B.
- `C`: Pointer to the dense matrix *C*. The number of rows must be equal to the number of rows of *A* and the number of columns must be equal to the number of columns of *B*.  Behavior undefined if this is not met. The parameter `ldc` describes how many elements to move between one row (row major) or column (column major). *C* is updated with the result of the operation.
- `ldc`: Increment in elements between rows (row major) or columns (column major) of *C*. Must be greater than or equal to `B` when row major, or number of rows of *A* when column major.

## See Also

- [func sparse_matrix_product_dense_double(CBLAS_ORDER, CBLAS_TRANSPOSE, sparse_dimension, Double, sparse_matrix_double!, UnsafePointer<Double>!, sparse_dimension, UnsafeMutablePointer<Double>!, sparse_dimension) -> sparse_status](sparse_matrix_product_dense_double(_:_:_:_:_:_:_:_:_:).md)
  Multiplies the dense matrix *B* by the sparse matrix *A* and adds the result to the dense matrix *C*, all with double-precision values.
- [func sparse_matrix_product_dense_float(CBLAS_ORDER, CBLAS_TRANSPOSE, sparse_dimension, Float, sparse_matrix_float!, UnsafePointer<Float>!, sparse_dimension, UnsafeMutablePointer<Float>!, sparse_dimension) -> sparse_status](sparse_matrix_product_dense_float(_:_:_:_:_:_:_:_:_:).md)
  Multiplies the dense matrix *B* by the sparse matrix *A* and adds the result to the dense matrix *C*, all with single-precision values.
- [func sparse_matrix_product_sparse_double(CBLAS_ORDER, CBLAS_TRANSPOSE, Double, sparse_matrix_double!, sparse_matrix_double!, UnsafeMutablePointer<Double>!, sparse_dimension) -> sparse_status](sparse_matrix_product_sparse_double(_:_:_:_:_:_:_:).md)
  Multiplies the sparse matrix *B* by the sparse matrix *A* and adds the result to the dense matrix *C*, all with double-precision values.
- [func sparse_matrix_triangular_solve_dense_double(CBLAS_ORDER, CBLAS_TRANSPOSE, sparse_dimension, Double, sparse_matrix_double!, UnsafeMutablePointer<Double>!, sparse_dimension) -> sparse_status](sparse_matrix_triangular_solve_dense_double(_:_:_:_:_:_:_:).md)
  Solves the system of equations *B = alpha * T⁻¹  * B* for *B* where *B* is a dense matrix and *T* is a triangular sparse matrix, both with double-precision values.
- [func sparse_matrix_triangular_solve_dense_float(CBLAS_ORDER, CBLAS_TRANSPOSE, sparse_dimension, Float, sparse_matrix_float!, UnsafeMutablePointer<Float>!, sparse_dimension) -> sparse_status](sparse_matrix_triangular_solve_dense_float(_:_:_:_:_:_:_:).md)
  Solves the system of equations *B = alpha * T⁻¹  * B* for *B* where *B* is a dense matrix and *T* is a triangular sparse matrix, both with double-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_matrix_product_sparse_float(_:_:_:_:_:_:_:))*