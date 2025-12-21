# <(_:_:)

**Framework**: Create ML  
**Kind**: op

Creates a column of Booleans by testing whether each element in the first column is less than the corresponding element in the second column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func < (a: MLUntypedColumn, b: MLUntypedColumn) -> MLUntypedColumn
```

#### Return Value

A new column of Booleans if the columns have the same size and underlying type; otherwise an invalid column.

## Parameters

- `a`: A column.
- `b`: A column.

## See Also

- [static ==(_:_:)](mluntypedcolumn/==(_:_:).md)
  Creates a column of Booleans by testing whether each element in the first column is equal to the corresponding element in the second column.
- [static !=(_:_:)](mluntypedcolumn/!=(_:_:).md)
  Creates a column of Booleans by testing whether each element in the first column is not equal to the corresponding element in the second column.
- [static >(_:_:)](mluntypedcolumn/_(_:_:)-1hr3j.md)
  Creates a column of Booleans by testing whether each element in the first column is greater than the corresponding element in the second column.
- [static <=(_:_:)](mluntypedcolumn/_=(_:_:)-2i3xz.md)
  Creates a column of Booleans by testing whether each element in the first column is less than or equal to the corresponding element in the second column.
- [static >=(_:_:)](mluntypedcolumn/_=(_:_:)-221lt.md)
  Creates a column of Booleans by testing whether each element in the first column is greater than or equal to the corresponding element in the second column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/_(_:_:)-9ke05)*