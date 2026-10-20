# sparse_elementwise_norm_float_complex(_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

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
func sparse_elementwise_norm_float_complex(_ A: sparse_matrix_float_complex!, _ norm: sparse_norm) -> Float
```

```c
float sparse_elementwise_norm_float_complex(sparse_matrix_float_complex A, sparse_norm norm);
```

## See Also

### Complex matrix operations
- [func sparse_elementwise_norm_double_complex(sparse_matrix_double_complex!, sparse_norm) -> Double](./sparse_elementwise_norm_double_complex%28_,_%29.md)
- [func sparse_get_vector_nonzero_count_double_complex(sparse_dimension, OpaquePointer!, sparse_stride) -> Int](./sparse_get_vector_nonzero_count_double_complex%28_,_,_%29.md)
- [func sparse_get_vector_nonzero_count_float_complex(sparse_dimension, OpaquePointer!, sparse_stride) -> Int](./sparse_get_vector_nonzero_count_float_complex%28_,_,_%29.md)
- [func sparse_operator_norm_double_complex(sparse_matrix_double_complex!, sparse_norm) -> Double](./sparse_operator_norm_double_complex%28_,_%29.md)
- [func sparse_operator_norm_float_complex(sparse_matrix_float_complex!, sparse_norm) -> Float](./sparse_operator_norm_float_complex%28_,_%29.md)
- [func sparse_permute_cols_double_complex(sparse_matrix_double_complex!, UnsafePointer<sparse_index>!) -> sparse_status](./sparse_permute_cols_double_complex%28_,_%29.md)
- [func sparse_permute_cols_float_complex(sparse_matrix_float_complex!, UnsafePointer<sparse_index>!) -> sparse_status](./sparse_permute_cols_float_complex%28_,_%29.md)
- [func sparse_permute_rows_double_complex(sparse_matrix_double_complex!, UnsafePointer<sparse_index>!) -> sparse_status](./sparse_permute_rows_double_complex%28_,_%29.md)
- [func sparse_permute_rows_float_complex(sparse_matrix_float_complex!, UnsafePointer<sparse_index>!) -> sparse_status](./sparse_permute_rows_float_complex%28_,_%29.md)
- [func sparse_permute_rows_float_complex(sparse_matrix_float_complex!, UnsafePointer<sparse_index>!) -> sparse_status](./sparse_permute_rows_float_complex%28_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_elementwise_norm_float_complex(_:_:))*