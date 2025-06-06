# ||(_:_:)

**Framework**: Create ML  
**Kind**: op

Creates a column of Booleans by performing a logical OR operation on each row of two columns of Booleans.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func || (a: MLUntypedColumn, b: MLUntypedColumn) -> MLUntypedColumn
```

#### Return Value

A new column of Booleans if the column and value have the same Boolean/integer underlying type; otherwise an invalid column.

## Parameters

- `a`: A column.
- `b`: A column.

## See Also

- [static func && (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](mluntypedcolumn/&&(_:_:).md)
  Creates a column of Booleans by performing a logical AND operation on each row of two columns of Booleans.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/__(_:_:))*