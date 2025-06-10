# sparse_insert_col_float_complex(_:_:_:_:_:)

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
func sparse_insert_col_float_complex(_ A: sparse_matrix_float_complex!, _ j: sparse_index, _ nz: sparse_dimension, _ val: OpaquePointer!, _ indx: UnsafePointer<sparse_index>!) -> sparse_status
```

## See Also

- [func sparse_insert_col_double_complex(sparse_matrix_double_complex!, sparse_index, sparse_dimension, OpaquePointer!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_col_double_complex(_:_:_:_:_:).md)
- [func sparse_insert_entries_double_complex(sparse_matrix_double_complex!, sparse_dimension, OpaquePointer!, UnsafePointer<sparse_index>!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_entries_double_complex(_:_:_:_:_:).md)
- [func sparse_insert_entries_float_complex(sparse_matrix_float_complex!, sparse_dimension, OpaquePointer!, UnsafePointer<sparse_index>!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_entries_float_complex(_:_:_:_:_:).md)
- [func sparse_insert_row_double_complex(sparse_matrix_double_complex!, sparse_index, sparse_dimension, OpaquePointer!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_row_double_complex(_:_:_:_:_:).md)
- [func sparse_insert_row_float_complex(sparse_matrix_float_complex!, sparse_index, sparse_dimension, OpaquePointer!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_row_float_complex(_:_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_insert_col_float_complex(_:_:_:_:_:))*