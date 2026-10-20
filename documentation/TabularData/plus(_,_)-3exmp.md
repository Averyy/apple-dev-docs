# +(_:_:)

**Framework**: TabularData  
**Kind**: op  
**Role**: Operator

Generates a column by adding each element in an optional column type to the corresponding elements of a column type.

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
func + <L, R>(lhs: L, rhs: R) -> Column<R.Element> where L : OptionalColumnProtocol, R : ColumnProtocol, L.WrappedElement : AdditiveArithmetic, L.WrappedElement == R.Element
```

#### Return Value

A new column with the same type as the right column.

## Parameters

- `lhs`: An optional column type.
- `rhs`: A column type.

## See Also

### Generating a Column by Adding Two Columns
- [static func + (Self, Self) -> Column<Self.Element>](./columnprotocol/plus%28_,_%29-yc11.md)
  Generates a column by adding each element in a column type to the corresponding elements of another.
- [func + <L, R>(L, R) -> Column<L.Element>](./plus%28_,_%29-1i7oh.md)
  Generates a column by adding each element in a column type to the corresponding elements of an optional column type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/+(_:_:)-3exmp)*