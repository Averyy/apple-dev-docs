# sparse_get_vector_nonzero_count_float(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns the number of nonzero values in the single-precision dense vector .

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
func sparse_get_vector_nonzero_count_float(_ N: sparse_dimension, _ x: UnsafePointer<Float>!, _ incx: sparse_stride) -> Int
```

#### Return Value

The count of the nonzero values in the vector .

#### Discussion

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 19, iPadOS 19, macOS 16, tvOS 19, watchOS 19, and visionOS 3, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Parameters

- `N`: The number of elements in the dense vector  .
- `x`: Pointer to the vector  .
- `incx`: Increment between valid values in the dense vector x.  Negative strides are supported.

## See Also

- [func sparse_get_vector_nonzero_count_double(sparse_dimension, UnsafePointer<Double>!, sparse_stride) -> Int](sparse_get_vector_nonzero_count_double(_:_:_:).md)
  Returns the number of nonzero values in the double-precision dense vector .
- [func sparse_pack_vector_double(sparse_dimension, sparse_dimension, UnsafePointer<Double>!, sparse_stride, UnsafeMutablePointer<Double>!, UnsafeMutablePointer<sparse_index>!) -> Int](sparse_pack_vector_double(_:_:_:_:_:_:).md)
  Packs nonzero values from a double-precision dense vector to a destination array.
- [func sparse_pack_vector_float(sparse_dimension, sparse_dimension, UnsafePointer<Float>!, sparse_stride, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<sparse_index>!) -> Int](sparse_pack_vector_float(_:_:_:_:_:_:).md)
  Packs nonzero values from a single-precision dense vector to a destination array.
- [func sparse_unpack_vector_double(sparse_dimension, sparse_dimension, Bool, UnsafePointer<Double>!, UnsafePointer<sparse_index>!, UnsafeMutablePointer<Double>!, sparse_stride)](sparse_unpack_vector_double(_:_:_:_:_:_:_:).md)
  Extracts elements from the sparse vector  into the corresponding location in the dense vector , with both vectors containing double-precision values.
- [func sparse_unpack_vector_float(sparse_dimension, sparse_dimension, Bool, UnsafePointer<Float>!, UnsafePointer<sparse_index>!, UnsafeMutablePointer<Float>!, sparse_stride)](sparse_unpack_vector_float(_:_:_:_:_:_:_:).md)
  Extracts elements from the sparse vector  into the corresponding location in the dense vector , with both vectors containing single-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_get_vector_nonzero_count_float(_:_:_:))*