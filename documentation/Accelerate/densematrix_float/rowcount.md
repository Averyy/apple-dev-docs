# rowCount

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The number of rows in the matrix.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var rowCount: Int32
```

```c
int rowCount;
```

## See Also

### Inspecting a Matrix’s Structure and Data
- [var columnCount: Int32](./columncount.md)
  The number of columns in the matrix.
- [var columnStride: Int32](./columnstride.md)
  The stride between matrix columns, in elements.
- [var attributes: SparseAttributes_t](./attributes.md)
  The attributes of the matrix, such as whether it’s symmetrical or triangular.
- [struct SparseAttributes_t](../sparseattributes_t.md)
  A structure that represents the attributes of a matrix.
- [var data: UnsafeMutablePointer<Float>](./data.md)
  The array of single-precision, floating-point values in column-major order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/densematrix_float/rowcount)*