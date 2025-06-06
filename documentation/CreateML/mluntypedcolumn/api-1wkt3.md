# <=(_:_:)

**Framework**: Create ML  
**Kind**: op

Creates a column of Booleans by testing whether each element in the given column is less than or equal to the given value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func <= (a: MLUntypedColumn, b: any MLDataValueConvertible) -> MLUntypedColumn
```

#### Return Value

A new column of Booleans if the column and value have the same underlying type; otherwise an invalid column.

## Parameters

- `a`: A column.
- `b`: A value.

## See Also

- [static func == (MLUntypedColumn, any MLDataValueConvertible) -> MLUntypedColumn](mluntypedcolumn/==(_:_:)-7xysh.md)
  Creates a column of Booleans by testing whether each element in the given column is equal to the given value.
- [static func != (MLUntypedColumn, any MLDataValueConvertible) -> MLUntypedColumn](mluntypedcolumn/!=(_:_:)-7do9.md)
  Creates a column of Booleans by testing whether each element in the given column is not equal to the given value.
- [static func > (MLUntypedColumn, any MLDataValueConvertible) -> MLUntypedColumn](mluntypedcolumn/_(_:_:)-2mdrt.md)
  Creates a column of Booleans by testing whether each element in the given column is greater than the given value.
- [static func < (MLUntypedColumn, any MLDataValueConvertible) -> MLUntypedColumn](mluntypedcolumn/_(_:_:)-8w60f.md)
  Creates a column of Booleans by testing whether each element in the given column is less than the given value.
- [static func >= (MLUntypedColumn, any MLDataValueConvertible) -> MLUntypedColumn](mluntypedcolumn/_=(_:_:)-2vu3g.md)
  Creates a column of Booleans by testing whether each element in the given column is greater than or equal to the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/_=(_:_:)-1wkt3)*