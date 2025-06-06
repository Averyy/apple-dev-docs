# +(_:_:)

**Framework**: TabularData  
**Kind**: op

Generates a column by adding a value to each element in an optional column.

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
static func + (lhs: Self, rhs: Self.WrappedElement) -> Column<Self.WrappedElement> where Self.WrappedElement : AdditiveArithmetic
```

#### Return Value

A new column.

## Parameters

- `lhs`: An optional column type.
- `rhs`: A value of the same type as the optional column.

## See Also

- [static func + (Self, Self.Element) -> Column<Self.Element>](discontiguouscolumnslice/+(_:_:)-75xxw.md)
  Generates a column by adding a value to each element in a column.
- [static func + (Self.Element, Self) -> Column<Self.Element>](discontiguouscolumnslice/+(_:_:)-2qwr7.md)
  Generates a column by adding each element in a column to a value.
- [static func + (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](discontiguouscolumnslice/+(_:_:)-77c23.md)
  Generates a column by adding each element in an optional column to a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice/+(_:_:)-2ba70)*