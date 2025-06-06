# -(_:_:)

**Framework**: TabularData  
**Kind**: op

Generates a column by subtracting each element in a column from a value.

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
static func - (lhs: Self.Element, rhs: Self) -> Column<Self.Element> where Self.Element : AdditiveArithmetic
```

#### Return Value

A new column.

## Parameters

- `lhs`: A value of the same type as the column.
- `rhs`: A column type.

## See Also

- [static func - (Self, Self.Element) -> Column<Self.Element>](discontiguouscolumnslice/-(_:_:)-2vlsk.md)
  Generates a column by subtracting a value from each element in a column.
- [static func - (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](discontiguouscolumnslice/-(_:_:)-hqv5.md)
  Generates a column by subtracting a value from each element in an optional column type.
- [static func - (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](discontiguouscolumnslice/-(_:_:)-5nwcb.md)
  Generates a column by subtracting each element in an optional column from a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice/-(_:_:)-1ynwr)*