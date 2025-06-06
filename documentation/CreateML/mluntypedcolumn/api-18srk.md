# /(_:_:)

**Framework**: Create ML  
**Kind**: op

Creates a column by dividing each element of the given column by the given value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func / (a: MLUntypedColumn, b: any MLDataValueConvertible) -> MLUntypedColumn
```

#### Return Value

A new column if the column and value have the same underlying type; otherwise an invalid column.

## Parameters

- `a`: An column.
- `b`: A value.

## See Also

- [static func + (MLUntypedColumn, any MLDataValueConvertible) -> MLUntypedColumn](mluntypedcolumn/+(_:_:)-4vnbk.md)
  Creates a column by adding each element of the given column to the given value.
- [static func - (MLUntypedColumn, any MLDataValueConvertible) -> MLUntypedColumn](mluntypedcolumn/-(_:_:)-4uigi.md)
  Creates a column by subtracting the given value from each element of the given column.
- [static func * (MLUntypedColumn, any MLDataValueConvertible) -> MLUntypedColumn](mluntypedcolumn/*(_:_:)-6gnlx.md)
  Creates a column by multiplying each element of the given column by the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/_(_:_:)-18srk)*