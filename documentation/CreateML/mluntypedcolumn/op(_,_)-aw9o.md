# /(_:_:)

**Framework**: Create ML  
**Kind**: op  
**Role**: Operator

Creates a column by dividing the given value by each element of the given column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func / (a: any MLDataValueConvertible, b: MLUntypedColumn) -> MLUntypedColumn
```

**Other overloads**:

```swift
static func / (a: MLUntypedColumn, b: MLUntypedColumn) -> MLUntypedColumn
```

```swift
static func / (a: MLUntypedColumn, b: any MLDataValueConvertible) -> MLUntypedColumn
```

## Return Value

A new column if the column and value have the same underlying type; otherwise an invalid column.

## Parameters

- `a`: An value.
- `b`: A column.

## See Also

### Combining a value with a column to generate an untyped column
- [static func + (any MLDataValueConvertible, MLUntypedColumn) -> MLUntypedColumn](./plus%28_,_%29-miqp.md)
  Creates a column by adding the given value to each element of the given column.
- [static func - (any MLDataValueConvertible, MLUntypedColumn) -> MLUntypedColumn](./minus%28_,_%29-9gm9i.md)
  Creates a column by subtracting each element of the given column from the given value.
- [static func * (any MLDataValueConvertible, MLUntypedColumn) -> MLUntypedColumn](./star%28_,_%29-7svdc.md)
  Creates a column by multiplying the given value by each element of the given column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/_(_:_:)-aw9o)*