# sparse_permute_rows_float_complex(_:_:)

**Framework**: Accelerate  
**Kind**: func

**Availability**:
- iOS 18.5+
- iPadOS 18.5+
- Mac Catalyst 18.5+
- macOS 15.5+
- tvOS 18.5+
- visionOS 2.5+
- watchOS 11.5+

## Declaration

```swift
func sparse_permute_rows_float_complex(_ A: sparse_matrix_float_complex!, _ perm: UnsafePointer<sparse_index>!) -> sparse_status
```

## See Also

- [func sparse_elementwise_norm_double_complex(sparse_matrix_double_complex!, sparse_norm) -> Double](sparse_elementwise_norm_double_complex(_:_:).md)
- [func sparse_elementwise_norm_float_complex(sparse_matrix_float_complex!, sparse_norm) -> Float](sparse_elementwise_norm_float_complex(_:_:).md)
- [func sparse_get_vector_nonzero_count_double_complex(sparse_dimension, OpaquePointer!, sparse_stride) -> Int](sparse_get_vector_nonzero_count_double_complex(_:_:_:).md)
- [func sparse_get_vector_nonzero_count_float_complex(sparse_dimension, OpaquePointer!, sparse_stride) -> Int](sparse_get_vector_nonzero_count_float_complex(_:_:_:).md)
- [func sparse_operator_norm_double_complex(sparse_matrix_double_complex!, sparse_norm) -> Double](sparse_operator_norm_double_complex(_:_:).md)
- [func sparse_operator_norm_float_complex(sparse_matrix_float_complex!, sparse_norm) -> Float](sparse_operator_norm_float_complex(_:_:).md)
- [func sparse_permute_cols_double_complex(sparse_matrix_double_complex!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_permute_cols_double_complex(_:_:).md)
- [func sparse_permute_cols_float_complex(sparse_matrix_float_complex!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_permute_cols_float_complex(_:_:).md)
- [func sparse_permute_rows_double_complex(sparse_matrix_double_complex!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_permute_rows_double_complex(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_permute_rows_float_complex(_:_:))*