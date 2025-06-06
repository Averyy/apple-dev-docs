# /(_:_:)

**Framework**: TabularData  
**Kind**: op

Generates an integer column by dividing a value by each element in an optional column type.

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
static func / (lhs: Self.WrappedElement, rhs: Self) -> Column<Self.WrappedElement>
```

#### Return Value

A new column.

## Parameters

- `lhs`: A value of the same type as the optional column’s type.
- `rhs`: An optional column type.

## See Also

- [static func / (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](discontiguouscolumnslice/_(_:_:)-51brc.md)
  Generates an integer column by dividing each element in an optional column by a value.
- [static func / (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](discontiguouscolumnslice/_(_:_:)-3bul1.md)
  Generates a floating-point column by dividing each element in an optional column by a value.
- [static func / (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](discontiguouscolumnslice/_(_:_:)-80g7i.md)
  Generates a floating-point column by dividing a value by each element in an optional column type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice/_(_:_:)-29za6)*