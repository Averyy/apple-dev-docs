# +(_:_:)

**Framework**: TabularData  
**Kind**: op

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

#### Return Value

A new column.

## Parameters

- `lhs`: A value of the same type as the column.
- `rhs`: A column type.

## See Also

- [static func + (Self, Self.Element) -> Column<Self.Element>](filledcolumn/+(_:_:)-9slnq.md)
  Generates a column by adding a value to each element in a column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/filledcolumn/+(_:_:)-57z7f)*