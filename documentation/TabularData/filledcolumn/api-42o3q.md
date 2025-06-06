# *(_:_:)

**Framework**: TabularData  
**Kind**: op

Generates a column by multiplying each element in a column by a value.

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
static func * (lhs: Self, rhs: Self.Element) -> Column<Self.Element>
```

#### Return Value

A new column.

## Parameters

- `lhs`: A column type.
- `rhs`: A value of the same type as the column.

## See Also

- [static func * (Self.Element, Self) -> Column<Self.Element>](filledcolumn/*(_:_:)-6hhwp.md)
  Generates a column by multiplying a value by each element in a column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/filledcolumn/*(_:_:)-42o3q)*