# DenseMatrix_Float

**Framework**: Accelerate  
**Kind**: struct

A structure that contains a dense matrix of single-precision, floating-point values.

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
struct DenseMatrix_Float
```

#### Overview

You typically use dense matrices to represent the unknowns matrix, , and the right-hand-side matrix, , in the matrix equation  A [`DenseMatrix_Float`](densematrix_float.md) structure provides a pointer to its underlying data, and information about its structure and attributes.

The following code shows an example of how to create a dense matrix structure from an array of double-precision values. In this case, use [`withUnsafeMutableBufferPointer(_:)`](acceleratemutablebuffer/withunsafemutablebufferpointer(_:).md) to pass a pointer to your collection. The [`DenseMatrix_Float`](densematrix_float.md) structure is valid only during the execution of the closure. Don’t store or return the structure for later use.

```swift
// An array of `rowCount` x `columnCount` single-precision values.
var matrixValues = [...]
let rowCount = Int32(5)
let columnCount = Int32(5)

matrixValues.withUnsafeMutableBufferPointer {
    let matrix = DenseMatrix_Float(rowCount: rowCount,
                                   columnCount: columnCount,
                                   columnStride: rowCount,
                                   attributes: SparseAttributes_t(),
                                   data: $0.baseAddress!)
    
    // Perform operations using `matrix`.
}
```

## Topics

### Initializers
- [init(rowCount: Int32, columnCount: Int32, columnStride: Int32, attributes: SparseAttributes_t, data: UnsafeMutablePointer<Float>)](densematrix_float/init(rowcount:columncount:columnstride:attributes:data:).md)
  Creates a new matrix of single-precision values.
### Inspecting a Matrix’s Structure and Data
- [var rowCount: Int32](densematrix_float/rowcount.md)
  The number of rows in the matrix.
- [var columnCount: Int32](densematrix_float/columncount.md)
  The number of columns in the matrix.
- [var columnStride: Int32](densematrix_float/columnstride.md)
  The stride between matrix columns, in elements.
- [var attributes: SparseAttributes_t](densematrix_float/attributes.md)
  The attributes of the matrix, such as whether it’s symmetrical or triangular.
- [struct SparseAttributes_t](sparseattributes_t.md)
  A structure that represents the attributes of a matrix.
- [var data: UnsafeMutablePointer<Float>](densematrix_float/data.md)
  The array of single-precision, floating-point values in column-major order.

## See Also

- [struct DenseMatrix_Double](densematrix_double.md)
  A structure that contains a dense matrix of double-precision, floating-point values.
- [struct DenseVector_Double](densevector_double.md)
  A structure that contains a dense vector of double-precision, floating-point values.
- [struct DenseVector_Float](densevector_float.md)
  A structure that contains a dense vector of single-precision, floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/densematrix_float)*