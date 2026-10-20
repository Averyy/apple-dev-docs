# *(_:_:)

**Framework**: TabularData  
**Kind**: op  
**Role**: Operator

Generates a column by multiplying each element in an optional column type by the corresponding elements of another.

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
static func * (lhs: Self, rhs: Self) -> Column<Self.WrappedElement>
```

Available when `WrappedElement` conforms to `Numeric`.

#### Return Value

A new column.

## Parameters

- `lhs`: An optional column type.
- `rhs`: Another optional column type.

## See Also

### Generating an Optional Column by Multiplying Two Columns
- [func * <L, R>(L, R) -> Column<R.Element>](../star%28_,_%29-2toor.md)
  Generates a column by multiplying each element in an optional column type by the corresponding elements of a column type.
- [func * <L, R>(L, R) -> Column<L.Element>](../star%28_,_%29-l9r3.md)
  Generates a column by multiplying each element in a column type by the corresponding elements of an optional column type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/optionalcolumnprotocol/*(_:_:)-5f5kx)*