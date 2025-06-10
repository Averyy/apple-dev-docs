# rowCount

**Framework**: Accelerate  
**Kind**: property

The number of rows in the matrix.

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
var rowCount: Int32
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/densematrix_float/rowcount)*