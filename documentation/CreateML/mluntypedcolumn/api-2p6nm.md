# *(_:_:)

**Framework**: Create ML  
**Kind**: op

Creates a column by multiplying each element in the first column by the corresponding element in the second column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func * (a: MLUntypedColumn, b: MLUntypedColumn) -> MLUntypedColumn
```

#### Return Value

A new column if the columns have the same size and underlying type; otherwise an invalid column.

## Parameters

- `a`: A column.
- `b`: A column.

## See Also

- [static func + (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](mluntypedcolumn/+(_:_:)-bcc5.md)
  Creates a column by adding each element in the first column to the corresponding element in the second column.
- [static func - (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](mluntypedcolumn/-(_:_:)-3h4o4.md)
  Creates a column by subtracting each element in the second column from the corresponding element in the first column.
- [static func / (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](mluntypedcolumn/_(_:_:)-45tpp.md)
  Creates a column by dividing each element in the first column by the corresponding element in the second column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/*(_:_:)-2p6nm)*