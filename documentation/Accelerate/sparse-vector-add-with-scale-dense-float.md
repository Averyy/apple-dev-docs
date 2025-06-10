# sparse_vector_add_with_scale_dense_float(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Scales the sparse vector  by  and adds the result to the dense vector  with both vectors containing single-precision values.

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
func sparse_vector_add_with_scale_dense_float(_ nz: sparse_dimension, _ alpha: Float, _ x: UnsafePointer<Float>!, _ indx: UnsafePointer<sparse_index>!, _ y: UnsafeMutablePointer<Float>!, _ incy: sparse_stride)
```

#### Discussion

Performs the operation  in place. If `alpha` or `nz` is zero,  is unchanged.

Scales the sparse vector x by alpha and adds the result to the dense vector y.

If the desired operation is , then an efficient option is to create the  buffer of zeros and then perform the operation with the zero filled .

Indices in `indx` are always assumed to be stored in ascending order. Additionally, indices are assumed to be unique.  The behavior of this function is undefined if either of these assumptions are not met.

All indices are 0 based (the first element of a pointer is `ptr[0]`).

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 19, iPadOS 19, macOS 16, tvOS 19, watchOS 19, and visionOS 3, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Parameters

- `nz`: The number of nonzero entries in the sparse vector  .
- `alpha`: Scalar multiplier of  .
- `x`: Pointer to the dense storage for the values of the sparse vector  . The corresponding entry in   holds the index of the value. Contains   values.
- `indx`: Pointer to the dense storage for the index values of the sparse vector  . The corresponding entry in   holds the values of the vector. Contains   values.
- `y`: Pointer to the dense vector  . Accessed as  , so dimension must be compatible with largest index value in  . The behavior of this function is undefined if this is not met. Negative strides are supported. Note, unlike dense BLAS routines, the pointer points to the last element when stride is negative.
- `incy`: Increment between valid values in the dense vector  . Negative strides are supported.

## See Also

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
- [func sparse_vector_norm_double(sparse_dimension, UnsafePointer<Double>!, UnsafePointer<sparse_index>!, sparse_norm) -> Double](sparse_vector_norm_double(_:_:_:_:).md)
  Computes the specified norm of the double-precision sparse vector .
- [func sparse_vector_norm_float(sparse_dimension, UnsafePointer<Float>!, UnsafePointer<sparse_index>!, sparse_norm) -> Float](sparse_vector_norm_float(_:_:_:_:).md)
  Computes the specified norm of the single-precision sparse vector .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_vector_add_with_scale_dense_float(_:_:_:_:_:_:))*