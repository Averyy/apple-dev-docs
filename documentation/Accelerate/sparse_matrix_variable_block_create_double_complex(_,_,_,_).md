# sparse_matrix_variable_block_create_double_complex(_:_:_:_:)

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
func sparse_matrix_variable_block_create_double_complex(_ Mb: sparse_dimension, _ Nb: sparse_dimension, _ K: UnsafePointer<sparse_dimension>!, _ L: UnsafePointer<sparse_dimension>!) -> sparse_matrix_double_complex!
```

```c
sparse_matrix_double_complexsparse_matrix_variable_block_create_double_complex(sparse_dimension Mb, sparse_dimension Nb, const sparse_dimension *K, const sparse_dimension *L);
```

## See Also

### Complex matrix creation and population
- [func sparse_matrix_variable_block_create_float_complex(sparse_dimension, sparse_dimension, UnsafePointer<sparse_dimension>!, UnsafePointer<sparse_dimension>!) -> sparse_matrix_float_complex!](./sparse_matrix_variable_block_create_float_complex%28_,_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_matrix_variable_block_create_double_complex(_:_:_:_:))*