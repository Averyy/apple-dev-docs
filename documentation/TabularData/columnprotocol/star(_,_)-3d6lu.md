# *(_:_:)

**Framework**: TabularData  
**Kind**: op  
**Role**: Operator

Generates a column by multiplying a value by each element in a column.

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
static func * (lhs: Self.Element, rhs: Self) -> Column<Self.Element>
```

Available when `Element` conforms to `Numeric`.

## Return Value

A new column.

## Parameters

- `lhs`: A value of the same type as the column.
- `rhs`: A column type.

## See Also

### Generating a column by multiplying a value
- [static func * (Self, Self.Element) -> Column<Self.Element>](./star%28_,_%29-17vqd.md)
  Generates a column by multiplying each element in a column by a value.
- [static func * (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](../optionalcolumnprotocol/star%28_,_%29-orkq.md)
  Generates a column by multiplying each element in an optional column by a value.
- [static func * (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](../optionalcolumnprotocol/star%28_,_%29-5vorv.md)
  Generates a column by multiplying a value by each element in an optional column type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnprotocol/*(_:_:)-3d6lu)*