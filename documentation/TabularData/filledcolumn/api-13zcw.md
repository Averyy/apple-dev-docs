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

- [static func - (Self.Element, Self) -> Column<Self.Element>](filledcolumn/-(_:_:)-2zphx.md)
  Generates a column by subtracting each element in a column from a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/filledcolumn/-(_:_:)-13zcw)*