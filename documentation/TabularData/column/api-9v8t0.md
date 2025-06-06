# +(_:_:)

**Framework**: TabularData  
**Kind**: op

Generates a column by adding a value to each element in a column.

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
static func + (lhs: Self, rhs: Self.Element) -> Column<Self.Element> where Self.Element : AdditiveArithmetic
```

#### Return Value

A new column.

## Parameters

- `lhs`: A column type.
- `rhs`: A value of the same type as the column.

## See Also

- [static func + (Self.Element, Self) -> Column<Self.Element>](column/+(_:_:)-579cq.md)
  Generates a column by adding each element in a column to a value.
- [static func + (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](column/+(_:_:)-7jy9x.md)
  Generates a column by adding a value to each element in an optional column.
- [static func + (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](column/+(_:_:)-8uo1v.md)
  Generates a column by adding each element in an optional column to a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/+(_:_:)-9v8t0)*