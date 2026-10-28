# ==(_:_:)

**Framework**: Create ML  
**Kind**: op  
**Role**: Operator

Creates a column of Booleans by testing whether each element in the given column is equal to the given value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func == (a: MLUntypedColumn, b: any MLDataValueConvertible) -> MLUntypedColumn
```

**Other overloads**:

```swift
static func == (a: MLUntypedColumn, b: MLUntypedColumn) -> MLUntypedColumn
```

```swift
static func == (a: any MLDataValueConvertible, b: MLUntypedColumn) -> MLUntypedColumn
```

## Return Value

A new column of Booleans if the column and value have the same underlying type; otherwise an invalid column.

## Parameters

- `a`: A column.
- `b`: A value.

## See Also

### Comparing a column with a value to generate an untyped column of booleans
- [static func != (MLUntypedColumn, any MLDataValueConvertible) -> MLUntypedColumn](./noteq%28_,_%29-7do9.md)
  Creates a column of Booleans by testing whether each element in the given column is not equal to the given value.
- [static func > (MLUntypedColumn, any MLDataValueConvertible) -> MLUntypedColumn](./op%28_,_%29-2mdrt.md)
  Creates a column of Booleans by testing whether each element in the given column is greater than the given value.
- [static func < (MLUntypedColumn, any MLDataValueConvertible) -> MLUntypedColumn](./op%28_,_%29-8w60f.md)
  Creates a column of Booleans by testing whether each element in the given column is less than the given value.
- [static func <= (MLUntypedColumn, any MLDataValueConvertible) -> MLUntypedColumn](./opeq%28_,_%29-1wkt3.md)
  Creates a column of Booleans by testing whether each element in the given column is less than or equal to the given value.
- [static func >= (MLUntypedColumn, any MLDataValueConvertible) -> MLUntypedColumn](./opeq%28_,_%29-2vu3g.md)
  Creates a column of Booleans by testing whether each element in the given column is greater than or equal to the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/==(_:_:)-7xysh)*