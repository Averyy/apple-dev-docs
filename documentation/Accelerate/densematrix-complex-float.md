# DenseMatrix_Complex_Float

**Framework**: Accelerate  
**Kind**: struct

Contains a dense `rowCount` x `columnCount` matrix of complex float values stored in column-major order.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct DenseMatrix_Complex_Float
```

#### Overview

- **`rowCount`**: Number of rows in the matrix.
- **`columnCount`**: Number of columns in the matrix.
- **`columnStride`**: The column stride of the matrix.
- **`attributes`**: The attributes of the matrix, for example whether the  matrix is symmetrical (Hermitian) or triangular.
- **`data`**: The array of float values in column-major order.

## Topics

### Initializers
- [init(rowCount: Int32, columnCount: Int32, columnStride: Int32, attributes: SparseAttributesComplex_t, data: OpaquePointer)](densematrix_complex_float/init(rowcount:columncount:columnstride:attributes:data:).md)
### Instance Properties
- [var attributes: SparseAttributesComplex_t](densematrix_complex_float/attributes.md)
  A type representing the attributes of a matrix.
- [var columnCount: Int32](densematrix_complex_float/columncount.md)
- [var columnStride: Int32](densematrix_complex_float/columnstride.md)
- [var data: OpaquePointer](densematrix_complex_float/data.md)
- [var rowCount: Int32](densematrix_complex_float/rowcount.md)

## See Also

- [struct DenseMatrix_Complex_Double](densematrix_complex_double.md)
  Contains a dense `rowCount` x `columnCount` matrix of complex double values stored in column-major order.
- [struct DenseVector_Complex_Double](densevector_complex_double.md)
  Contains a dense vector of double complex values.
- [struct DenseVector_Complex_Float](densevector_complex_float.md)
  Contains a dense vector of float complex values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/densematrix_complex_float)*