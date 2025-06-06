# *(_:_:)

**Framework**: TabularData  
**Kind**: op

Generates a column by multiplying each element in an optional column by a value.

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
static func * (lhs: Self, rhs: Self.WrappedElement) -> Column<Self.WrappedElement>
```

#### Return Value

A new column.

## Parameters

- `lhs`: An optional column type.
- `rhs`: A value of the same type as the optional column’s type.

## See Also

- [static func * (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](discontiguouscolumnslice/*(_:_:)-3dsxf.md)
  Generates a column by multiplying a value by each element in an optional column type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice/*(_:_:)-8faxs)*