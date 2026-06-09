# sparse_inner_product_sparse_double(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Computes the inner product of sparse vector *x* with sparse vector *y,* with both vectors containing double-precision values.

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
func sparse_inner_product_sparse_double(_ nzx: sparse_dimension, _ nzy: sparse_dimension, _ x: UnsafePointer<Double>!, _ indx: UnsafePointer<sparse_index>!, _ y: UnsafePointer<Double>!, _ indy: UnsafePointer<sparse_index>!) -> Double
```

#### Return Value

The inner product of sparse vector *x* with sparse vector *y*.  Returns zero if `nzx` or `nzy` is less than or equal to zero.

#### Discussion

Indices in `indx` and `indy` are always assumed to be stored in ascending order. Additionally, indices are assumed to be unique.  The behavior of this function is undefined if either of these assumptions are not met.

All indices are 0 based (the first element of a pointer is `ptr[0]`).

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 26, iPadOS 26, macOS 26, tvOS 26, visionOS 26, and watchOS 26, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings under Apple Clang - Preprocessing > Preprocessor Macros.

## Parameters

- `nzx`: The number of nonzero entries in the sparse vector *x*.
- `nzy`: The number of nonzero entries in the sparse vector *y*.
- `x`: Pointer to the dense storage for the values of the sparse vector *x*.  The corresponding entry in `indx` holds the index of the value. Contains `nzx` values.
- `indx`: Pointer to the dense storage for the index values of the sparse vector x. The corresponding entry in *x* holds the values of the vector. Contains `nzx` values.
- `y`: Pointer to the dense storage for the values of the sparse vector *y*. The corresponding entry in `indy` holds the index of the value. Contains `nzy` values.
- `indy`: Pointer to the dense storage for the index values of the sparse vector *y*. The corresponding entry in *y* holds the values of the vector. Contains `nzy` values.

## See Also

- [func sparse_inner_product_dense_double(sparse_dimension, UnsafePointer<Double>!, UnsafePointer<sparse_index>!, UnsafePointer<Double>!, sparse_stride) -> Double](sparse_inner_product_dense_double(_:_:_:_:_:).md)
  Computes the inner product of sparse vector *x* with double-precision *y*, with both vectors containing double-precision values.
- [func sparse_inner_product_dense_float(sparse_dimension, UnsafePointer<Float>!, UnsafePointer<sparse_index>!, UnsafePointer<Float>!, sparse_stride) -> Float](sparse_inner_product_dense_float(_:_:_:_:_:).md)
  Computes the inner product of sparse vector *x* with dense vector *y,* with both vectors containing single-precision values.
- [func sparse_inner_product_sparse_float(sparse_dimension, sparse_dimension, UnsafePointer<Float>!, UnsafePointer<sparse_index>!, UnsafePointer<Float>!, UnsafePointer<sparse_index>!) -> Float](sparse_inner_product_sparse_float(_:_:_:_:_:_:).md)
  Computes the inner product of sparse vector *x* with sparse vector *y,* with both vectors containing single-precision values.
- [func sparse_vector_add_with_scale_dense_double(sparse_dimension, Double, UnsafePointer<Double>!, UnsafePointer<sparse_index>!, UnsafeMutablePointer<Double>!, sparse_stride)](sparse_vector_add_with_scale_dense_double(_:_:_:_:_:_:).md)
  Scales the sparse vector *x* by *alpha* and adds the result to the dense vector *y,* with both vectors containing double-precision values.
- [func sparse_vector_add_with_scale_dense_float(sparse_dimension, Float, UnsafePointer<Float>!, UnsafePointer<sparse_index>!, UnsafeMutablePointer<Float>!, sparse_stride)](sparse_vector_add_with_scale_dense_float(_:_:_:_:_:_:).md)
  Scales the sparse vector *x* by *alpha* and adds the result to the dense vector *y,* with both vectors containing single-precision values.
- [func sparse_vector_norm_double(sparse_dimension, UnsafePointer<Double>!, UnsafePointer<sparse_index>!, sparse_norm) -> Double](sparse_vector_norm_double(_:_:_:_:).md)
  Computes the specified norm of the double-precision sparse vector *x*.
- [func sparse_vector_norm_float(sparse_dimension, UnsafePointer<Float>!, UnsafePointer<sparse_index>!, sparse_norm) -> Float](sparse_vector_norm_float(_:_:_:_:).md)
  Computes the specified norm of the single-precision sparse vector *x*.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_inner_product_sparse_double(_:_:_:_:_:_:))*