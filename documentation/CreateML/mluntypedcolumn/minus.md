# -(_:_:)

**Framework**: Create ML  
**Kind**: op

Creates a column by subtracting each element of the given column from the given value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func - (a: any MLDataValueConvertible, b: MLUntypedColumn) -> MLUntypedColumn
```

#### Return Value

A new column if the column and value have the same underlying type; otherwise an invalid column.

## Parameters

- `a`: An value.
- `b`: A column.

## See Also

- [static func + (any MLDataValueConvertible, MLUntypedColumn) -> MLUntypedColumn](mluntypedcolumn/+(_:_:)-miqp.md)
  Creates a column by adding the given value to each element of the given column.
- [static func * (any MLDataValueConvertible, MLUntypedColumn) -> MLUntypedColumn](mluntypedcolumn/*(_:_:)-7svdc.md)
  Creates a column by multiplying the given value by each element of the given column.
- [static func / (any MLDataValueConvertible, MLUntypedColumn) -> MLUntypedColumn](mluntypedcolumn/_(_:_:)-aw9o.md)
  Creates a column by dividing the given value by each element of the given column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/-(_:_:)-9gm9i)*