# -(_:_:)

**Framework**: Create ML  
**Kind**: op  
**Role**: Operator

Creates a column by subtracting each element in the second column from the corresponding element in the first column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func - (a: MLUntypedColumn, b: MLUntypedColumn) -> MLUntypedColumn
```

**Other overloads**:

```swift
static func - (a: MLUntypedColumn, b: any MLDataValueConvertible) -> MLUntypedColumn
```

```swift
static func - (a: any MLDataValueConvertible, b: MLUntypedColumn) -> MLUntypedColumn
```

#### Return Value

A new column if the columns have the same size and underlying type; otherwise an invalid column.

## Parameters

- `a`: A column.
- `b`: A column.

## See Also

### Combining columns to generate an untyped column
- [static func + (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](./plus%28_,_%29-bcc5.md)
  Creates a column by adding each element in the first column to the corresponding element in the second column.
- [static func * (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](./star%28_,_%29-2p6nm.md)
  Creates a column by multiplying each element in the first column by the corresponding element in the second column.
- [static func / (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](./op%28_,_%29-45tpp.md)
  Creates a column by dividing each element in the first column by the corresponding element in the second column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/-(_:_:)-3h4o4)*