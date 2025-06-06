# +(_:_:)

**Framework**: TabularData  
**Kind**: op

Generates a column by adding each element in an optional column to a value.

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
static func + (lhs: Self.WrappedElement, rhs: Self) -> Column<Self.WrappedElement> where Self.WrappedElement : AdditiveArithmetic
```

#### Return Value

A new column.

## Parameters

- `lhs`: A value of the same type as the optional column’s type.
- `rhs`: An optional column type.

## See Also

- [static func + (Self, Self.Element) -> Column<Self.Element>](columnslice/+(_:_:)-2l5ok.md)
  Generates a column by adding a value to each element in a column.
- [static func + (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](columnslice/+(_:_:)-3xsx4.md)
  Generates a column by adding a value to each element in an optional column.
- [static func + (Self.Element, Self) -> Column<Self.Element>](columnslice/+(_:_:)-4bxn6.md)
  Generates a column by adding each element in a column to a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnslice/+(_:_:)-ooqt)*