# *(_:_:)

**Framework**: TabularData  
**Kind**: op  
**Role**: Operator

Generates a column by multiplying a value by each element in an optional column type.

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
static func * (lhs: Self.WrappedElement, rhs: Self) -> Column<Self.WrappedElement>
```

Available when `WrappedElement` conforms to `Numeric`.

## Return Value

A new column.

## Parameters

- `lhs`: A value of the same type as the optional column’s type.
- `rhs`: An optional column type.

## See Also

### Generating a column by multiplying a value
- [static func * (Self, Self.Element) -> Column<Self.Element>](../columnprotocol/star%28_,_%29-17vqd.md)
  Generates a column by multiplying each element in a column by a value.
- [static func * (Self.Element, Self) -> Column<Self.Element>](../columnprotocol/star%28_,_%29-3d6lu.md)
  Generates a column by multiplying a value by each element in a column.
- [static func * (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](./star%28_,_%29-orkq.md)
  Generates a column by multiplying each element in an optional column by a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/optionalcolumnprotocol/*(_:_:)-5vorv)*