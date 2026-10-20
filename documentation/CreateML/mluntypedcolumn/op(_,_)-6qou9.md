# <(_:_:)

**Framework**: Create ML  
**Kind**: op  
**Role**: Operator

Creates a column of Booleans by testing whether the given value is less than each element in the given column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func < (a: any MLDataValueConvertible, b: MLUntypedColumn) -> MLUntypedColumn
```

**Other overloads**:

```swift
static func < (a: MLUntypedColumn, b: MLUntypedColumn) -> MLUntypedColumn
```

```swift
static func < (a: MLUntypedColumn, b: any MLDataValueConvertible) -> MLUntypedColumn
```

#### Return Value

A new column of Booleans if the column and value have the same underlying type; otherwise an invalid column.

## Parameters

- `a`: A value.
- `b`: A column.

## See Also

### Comparing a value with a column to generate an untyped column of booleans
- [static func == (any MLDataValueConvertible, MLUntypedColumn) -> MLUntypedColumn](./eqeq%28_,_%29-6z88q.md)
  Creates a column of Booleans by testing whether the given value is equal to each element in the given column.
- [static func != (any MLDataValueConvertible, MLUntypedColumn) -> MLUntypedColumn](./noteq%28_,_%29-6k3p6.md)
  Creates a column of Booleans by testing whether the given value is not equal to each element in the given column.
- [static func > (any MLDataValueConvertible, MLUntypedColumn) -> MLUntypedColumn](./op%28_,_%29-52drj.md)
  Creates a column of Booleans by testing whether the given value is greater than each element in the given column.
- [static func <= (any MLDataValueConvertible, MLUntypedColumn) -> MLUntypedColumn](./opeq%28_,_%29-t4bt.md)
  Creates a column of Booleans by testing whether the given value is less than or equal to each element in the given column.
- [static func >= (any MLDataValueConvertible, MLUntypedColumn) -> MLUntypedColumn](./opeq%28_,_%29-6yycf.md)
  Creates a column of Booleans by testing whether the given value is greater than or equal to each element in the given column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/_(_:_:)-6qou9)*