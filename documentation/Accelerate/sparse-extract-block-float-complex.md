# sparse_extract_block_float_complex(_:_:_:_:_:_:)

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
func sparse_extract_block_float_complex(_ A: sparse_matrix_float_complex!, _ bi: sparse_index, _ bj: sparse_index, _ row_stride: sparse_dimension, _ col_stride: sparse_dimension, _ val: OpaquePointer!) -> sparse_status
```

## See Also

- [func sparse_extract_block_double(sparse_matrix_double!, sparse_index, sparse_index, sparse_dimension, sparse_dimension, UnsafeMutablePointer<Double>!) -> sparse_status](sparse_extract_block_double(_:_:_:_:_:_:).md)
  Extracts values from a specified block of a double-precision matrix.
- [func sparse_extract_block_float(sparse_matrix_float!, sparse_index, sparse_index, sparse_dimension, sparse_dimension, UnsafeMutablePointer<Float>!) -> sparse_status](sparse_extract_block_float(_:_:_:_:_:_:).md)
  Extracts values from a specified block of a single-precision matrix.
- [func sparse_extract_block_double_complex(sparse_matrix_double_complex!, sparse_index, sparse_index, sparse_dimension, sparse_dimension, OpaquePointer!) -> sparse_status](sparse_extract_block_double_complex(_:_:_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_extract_block_float_complex(_:_:_:_:_:_:))*