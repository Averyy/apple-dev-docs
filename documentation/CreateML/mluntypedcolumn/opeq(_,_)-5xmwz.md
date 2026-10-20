# <=(_:_:)

**Framework**: Create ML  
**Kind**: op  
**Role**: Operator

Creates a column of Booleans by testing whether each element in the first column is less than or equal to the corresponding element in the second column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func <= (a: MLUntypedColumn, b: MLUntypedColumn) -> MLUntypedColumn
```

**Other overloads**:

```swift
static func <= (a: MLUntypedColumn, b: any MLDataValueConvertible) -> MLUntypedColumn
```

```swift
static func <= (a: any MLDataValueConvertible, b: MLUntypedColumn) -> MLUntypedColumn
```

#### Return Value

A new column of Booleans if the columns have the same size and underlying type; otherwise an invalid column.

## Parameters

- `a`: A column.]
- `b`: A column.

## See Also

### Comparing columns to generate an untyped column of booleans
- [static func == (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](./eqeq%28_,_%29-3o7mo.md)
  Creates a column of Booleans by testing whether each element in the first column is equal to the corresponding element in the second column.
- [static func != (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](./noteq%28_,_%29-86hu4.md)
  Creates a column of Booleans by testing whether each element in the first column is not equal to the corresponding element in the second column.
- [static func > (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](./op%28_,_%29-9r2zq.md)
  Creates a column of Booleans by testing whether each element in the first column is greater than the corresponding element in the second column.
- [static func < (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](./op%28_,_%29-7zms0.md)
  Creates a column of Booleans by testing whether each element in the first column is less than the corresponding element in the second column.
- [static func >= (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](./opeq%28_,_%29-4u3ir.md)
  Creates a column of Booleans by testing whether each element in the first column is greater than or equal to the corresponding element in the second column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/_=(_:_:)-5xmwz)*