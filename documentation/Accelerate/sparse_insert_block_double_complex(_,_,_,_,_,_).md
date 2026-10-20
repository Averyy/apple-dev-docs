# sparse_insert_block_double_complex(_:_:_:_:_:_:)

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
func sparse_insert_block_double_complex(_ A: sparse_matrix_double_complex!, _ val: OpaquePointer!, _ row_stride: sparse_dimension, _ col_stride: sparse_dimension, _ bi: sparse_index, _ bj: sparse_index) -> sparse_status
```

```c
sparse_status sparse_insert_block_double_complex(sparse_matrix_double_complex A, const _Complex double * restrictval, sparse_dimension row_stride, sparse_dimension col_stride, sparse_index bi, sparse_index bj);
```

## See Also

### Value insertion
- [func sparse_insert_block_float_complex(sparse_matrix_float_complex!, OpaquePointer!, sparse_dimension, sparse_dimension, sparse_index, sparse_index) -> sparse_status](./sparse_insert_block_float_complex%28_,_,_,_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_insert_block_double_complex(_:_:_:_:_:_:))*