# sparse_extract_sparse_column_double_complex(_:_:_:_:_:_:_:)

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
func sparse_extract_sparse_column_double_complex(_ A: sparse_matrix_double_complex!, _ column: sparse_index, _ row_start: sparse_index, _ row_end: UnsafeMutablePointer<sparse_index>!, _ nz: sparse_dimension, _ val: OpaquePointer!, _ indx: UnsafeMutablePointer<sparse_index>!) -> sparse_status
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_extract_sparse_column_double_complex(_:_:_:_:_:_:_:))*