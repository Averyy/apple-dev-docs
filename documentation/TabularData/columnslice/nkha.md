# -(_:_:)

**Framework**: TabularData  
**Kind**: op

Generates a column by subtracting a value from each element in an optional column type.

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
static func - (lhs: Self, rhs: Self.WrappedElement) -> Column<Self.WrappedElement> where Self.WrappedElement : AdditiveArithmetic
```

#### Return Value

A new column.

## Parameters

- `lhs`: An optional column type.
- `rhs`: A value of the same type as the optional column’s type.

## See Also

- [static func - (Self, Self.Element) -> Column<Self.Element>](columnslice/-(_:_:)-26wtz.md)
  Generates a column by subtracting a value from each element in a column.
- [static func - (Self.Element, Self) -> Column<Self.Element>](columnslice/-(_:_:)-8z15n.md)
  Generates a column by subtracting each element in a column from a value.
- [static func - (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](columnslice/-(_:_:)-5mbpd.md)
  Generates a column by subtracting each element in an optional column from a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnslice/-(_:_:)-nkha)*