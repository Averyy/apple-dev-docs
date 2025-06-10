# init(rowCount:columnCount:columnStride:attributes:data:)

**Framework**: Accelerate  
**Kind**: init

Creates a new matrix of double-precision values.

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
init(rowCount: Int32, columnCount: Int32, columnStride: Int32, attributes: SparseAttributes_t, data: UnsafeMutablePointer<Double>)
```

## Parameters

- `rowCount`: The number of rows in the matrix.
- `columnCount`: The number of columns in the matrix.
- `columnStride`: The column stride of the matrix.
- `attributes`: The attributes of the matrix, such as whether it’s symmetrical or triangular.
- `data`: The array of double-precision, floating-point values in column-major order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/densematrix_double/init(rowcount:columncount:columnstride:attributes:data:))*