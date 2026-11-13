# +(_:_:)

**Framework**: TabularData  
**Kind**: op  
**Role**: Operator

Generates a column by adding each element in a column to a value.

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
static func + (lhs: Self.Element, rhs: Self) -> Column<Self.Element> where Self.Element : AdditiveArithmetic
```

## Return Value

A new column.

## Parameters

- `lhs`: A value of the same type as the column.
- `rhs`: A column type.

## See Also

### Generating a column by adding a value
- [static func + (Self, Self.Element) -> Column<Self.Element>](./plus%28_,_%29-39k8v.md)
  Generates a column by adding a value to each element in a column.
- [static func + (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](../optionalcolumnprotocol/plus%28_,_%29-501gg.md)
  Generates a column by adding a value to each element in an optional column.
- [static func + (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](../optionalcolumnprotocol/plus%28_,_%29-6ko8x.md)
  Generates a column by adding each element in an optional column to a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnprotocol/+(_:_:)-94kiv)*