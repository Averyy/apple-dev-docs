# -(_:_:)

**Framework**: TabularData  
**Kind**: op

Generates a column by subtracting a value from each element in a column.

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
static func - (lhs: Self, rhs: Self.Element) -> Column<Self.Element> where Self.Element : AdditiveArithmetic
```

#### Return Value

A new column.

## Parameters

- `lhs`: A column type.
- `rhs`: A value of the same type as the column.

## See Also

- [static func - (Self.Element, Self) -> Column<Self.Element>](discontiguouscolumnslice/-(_:_:)-1ynwr.md)
  Generates a column by subtracting each element in a column from a value.
- [static func - (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](discontiguouscolumnslice/-(_:_:)-hqv5.md)
  Generates a column by subtracting a value from each element in an optional column type.
- [static func - (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](discontiguouscolumnslice/-(_:_:)-5nwcb.md)
  Generates a column by subtracting each element in an optional column from a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice/-(_:_:)-2vlsk)*