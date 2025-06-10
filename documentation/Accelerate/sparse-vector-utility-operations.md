# Sparse Vector Utility Operations

**Framework**: Accelerate

Create and work with sparse vector structures.

## Topics

### Sparse Utility Operations
- [func sparse_get_vector_nonzero_count_double(sparse_dimension, UnsafePointer<Double>!, sparse_stride) -> Int](sparse_get_vector_nonzero_count_double(_:_:_:).md)
  Returns the number of nonzero values in the double-precision dense vector .
- [func sparse_get_vector_nonzero_count_float(sparse_dimension, UnsafePointer<Float>!, sparse_stride) -> Int](sparse_get_vector_nonzero_count_float(_:_:_:).md)
  Returns the number of nonzero values in the single-precision dense vector .
- [func sparse_pack_vector_double(sparse_dimension, sparse_dimension, UnsafePointer<Double>!, sparse_stride, UnsafeMutablePointer<Double>!, UnsafeMutablePointer<sparse_index>!) -> Int](sparse_pack_vector_double(_:_:_:_:_:_:).md)
  Packs nonzero values from a double-precision dense vector to a destination array.
- [func sparse_pack_vector_float(sparse_dimension, sparse_dimension, UnsafePointer<Float>!, sparse_stride, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<sparse_index>!) -> Int](sparse_pack_vector_float(_:_:_:_:_:_:).md)
  Packs nonzero values from a single-precision dense vector to a destination array.
- [func sparse_unpack_vector_double(sparse_dimension, sparse_dimension, Bool, UnsafePointer<Double>!, UnsafePointer<sparse_index>!, UnsafeMutablePointer<Double>!, sparse_stride)](sparse_unpack_vector_double(_:_:_:_:_:_:_:).md)
  Extracts elements from the sparse vector  into the corresponding location in the dense vector , with both vectors containing double-precision values.
- [func sparse_unpack_vector_float(sparse_dimension, sparse_dimension, Bool, UnsafePointer<Float>!, UnsafePointer<sparse_index>!, UnsafeMutablePointer<Float>!, sparse_stride)](sparse_unpack_vector_float(_:_:_:_:_:_:_:).md)
  Extracts elements from the sparse vector  into the corresponding location in the dense vector , with both vectors containing single-precision values.
### Supporting Types
- [typealias sparse_dimension](sparse_dimension.md)
  The dimension type.
- [typealias sparse_index](sparse_index.md)
  The index type.
- [typealias sparse_stride](sparse_stride.md)
  The stride type.

## See Also

- [Matrix and Vector Operations](matrix-and-vector-operations.md)
  Perform computations with matrices and vectors.
- [Pointwise Matrix Operations](pointwise-matrix-operations.md)
  Create, insert values into, and extract values from a pointwise sparse matrix.
- [Blockwise Matrix Operations](blockwise-matrix-operations.md)
  Create, insert values into, and extract values from a blockwise sparse matrix.
- [General Sparse Matrix Management Operations](general-sparse-matrix-management-operations.md)
  Manage and work with the properties of a sparse matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse-vector-utility-operations)*