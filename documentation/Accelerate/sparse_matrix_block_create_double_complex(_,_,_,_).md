# sparse_matrix_block_create_double_complex(_:_:_:_:)

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
func sparse_matrix_block_create_double_complex(_ Mb: sparse_dimension, _ Nb: sparse_dimension, _ k: sparse_dimension, _ l: sparse_dimension) -> sparse_matrix_double_complex!
```

```c
sparse_matrix_double_complexsparse_matrix_block_create_double_complex(sparse_dimension Mb, sparse_dimension Nb, sparse_dimension k, sparse_dimension l);
```

## See Also

### Matrix creation and population
- [func sparse_matrix_block_create_double(sparse_dimension, sparse_dimension, sparse_dimension, sparse_dimension) -> sparse_matrix_double!](./sparse_matrix_block_create_double%28_,_,_,_%29.md)
  Returns a double-precision sparse matrix object that is stored in block-entry format with a fixed block size.
- [func sparse_matrix_block_create_float(sparse_dimension, sparse_dimension, sparse_dimension, sparse_dimension) -> sparse_matrix_float!](./sparse_matrix_block_create_float%28_,_,_,_%29.md)
  Returns a single-precision sparse matrix object that is stored in block-entry format with a fixed block size.
- [func sparse_matrix_variable_block_create_double(sparse_dimension, sparse_dimension, UnsafePointer<sparse_dimension>!, UnsafePointer<sparse_dimension>!) -> sparse_matrix_double!](./sparse_matrix_variable_block_create_double%28_,_,_,_%29.md)
  Returns a double-precision sparse matrix object that is stored in block-entry format with a variable block size.
- [func sparse_matrix_variable_block_create_float(sparse_dimension, sparse_dimension, UnsafePointer<sparse_dimension>!, UnsafePointer<sparse_dimension>!) -> sparse_matrix_float!](./sparse_matrix_variable_block_create_float%28_,_,_,_%29.md)
  Returns a single-precision sparse matrix object that is stored in block-entry format with a variable block size.
- [func sparse_insert_block_double(sparse_matrix_double!, UnsafePointer<Double>!, sparse_dimension, sparse_dimension, sparse_index, sparse_index) -> sparse_status](./sparse_insert_block_double%28_,_,_,_,_,_%29.md)
  Inserts a dense block of entries into a double-precision matrix.
- [func sparse_insert_block_float(sparse_matrix_float!, UnsafePointer<Float>!, sparse_dimension, sparse_dimension, sparse_index, sparse_index) -> sparse_status](./sparse_insert_block_float%28_,_,_,_,_,_%29.md)
  Inserts a dense block of entries into a single-precision matrix.
- [func sparse_matrix_block_create_float_complex(sparse_dimension, sparse_dimension, sparse_dimension, sparse_dimension) -> sparse_matrix_float_complex!](./sparse_matrix_block_create_float_complex%28_,_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_matrix_block_create_double_complex(_:_:_:_:))*