# !=(_:_:)

**Framework**: Create ML  
**Kind**: op

Creates a column of Booleans by testing whether each element in the first column is not equal to the corresponding element in the second column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func != (a: MLUntypedColumn, b: MLUntypedColumn) -> MLUntypedColumn
```

#### Return Value

A new column of Booleans if the columns have the same size and underlying type; otherwise an invalid column.

## Parameters

- `a`: A column.
- `b`: A column.

## See Also

- [static func == (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](mluntypedcolumn/==(_:_:)-3o7mo.md)
  Creates a column of Booleans by testing whether each element in the first column is equal to the corresponding element in the second column.
- [static func > (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](mluntypedcolumn/_(_:_:)-9r2zq.md)
  Creates a column of Booleans by testing whether each element in the first column is greater than the corresponding element in the second column.
- [static func < (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](mluntypedcolumn/_(_:_:)-7zms0.md)
  Creates a column of Booleans by testing whether each element in the first column is less than the corresponding element in the second column.
- [static func <= (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](mluntypedcolumn/_=(_:_:)-5xmwz.md)
  Creates a column of Booleans by testing whether each element in the first column is less than or equal to the corresponding element in the second column.
- [static func >= (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](mluntypedcolumn/_=(_:_:)-4u3ir.md)
  Creates a column of Booleans by testing whether each element in the first column is greater than or equal to the corresponding element in the second column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/!=(_:_:)-86hu4)*