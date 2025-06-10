# sparse_extract_sparse_row_float_complex(_:_:_:_:_:_:_:)

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
func sparse_extract_sparse_row_float_complex(_ A: sparse_matrix_float_complex!, _ row: sparse_index, _ column_start: sparse_index, _ column_end: UnsafeMutablePointer<sparse_index>!, _ nz: sparse_dimension, _ val: OpaquePointer!, _ jndx: UnsafeMutablePointer<sparse_index>!) -> sparse_status
```

## See Also

- [func sparse_extract_sparse_row_double(sparse_matrix_double!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, UnsafeMutablePointer<Double>!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_row_double(_:_:_:_:_:_:_:).md)
  Extracts values from a specified row of a double-precision sparse matrix.
- [func sparse_extract_sparse_row_float(sparse_matrix_float!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_row_float(_:_:_:_:_:_:_:).md)
  Extracts values from a specified row of a single-precision sparse matrix.
- [func sparse_extract_sparse_column_double(sparse_matrix_double!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, UnsafeMutablePointer<Double>!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_column_double(_:_:_:_:_:_:_:).md)
  Extracts values from a specified column of a double-precision sparse matrix.
- [func sparse_extract_sparse_column_float(sparse_matrix_float!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_column_float(_:_:_:_:_:_:_:).md)
  Extracts values from a specified column of a single-precision sparse matrix.
- [func sparse_extract_sparse_column_double_complex(sparse_matrix_double_complex!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, OpaquePointer!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_column_double_complex(_:_:_:_:_:_:_:).md)
- [func sparse_extract_sparse_column_float_complex(sparse_matrix_float_complex!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, OpaquePointer!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_column_float_complex(_:_:_:_:_:_:_:).md)
- [func sparse_extract_sparse_row_double_complex(sparse_matrix_double_complex!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, OpaquePointer!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_row_double_complex(_:_:_:_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_extract_sparse_row_float_complex(_:_:_:_:_:_:_:))*