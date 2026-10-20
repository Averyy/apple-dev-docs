# -(_:_:)

**Framework**: TabularData  
**Kind**: op  
**Role**: Operator

Generates a column by subtracting each element in an optional column type from the corresponding elements of a column type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func - <L, R>(lhs: L, rhs: R) -> Column<L.Element> where L : ColumnProtocol, R : OptionalColumnProtocol, L.Element : AdditiveArithmetic, L.Element == R.WrappedElement
```

#### Return Value

A new column with the same type as the left column.

## Parameters

- `lhs`: A column type.
- `rhs`: An optional column type.

## See Also

### Generating a Column by Subtracting Two Columns
- [static func - (Self, Self) -> Column<Self.Element>](./columnprotocol/minus%28_,_%29-36zol.md)
  Generates a column by subtracting each element in a column type from the corresponding elements of another.
- [func - <L, R>(L, R) -> Column<R.Element>](./minus%28_,_%29-95yoe.md)
  Generates a column by subtracting each element in a column type from the corresponding elements of an optional column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/-(_:_:)-25cs6)*