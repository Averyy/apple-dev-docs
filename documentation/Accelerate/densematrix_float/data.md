# data

**Framework**: Accelerate  
**Kind**: property

The array of single-precision, floating-point values in column-major order.

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
var data: UnsafeMutablePointer<Float>
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/densematrix_float/data)*