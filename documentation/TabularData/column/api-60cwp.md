# /(_:_:)

**Framework**: TabularData  
**Kind**: op

Generates an integer column by dividing each element in an optional column by a value.

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
static func / (lhs: Self, rhs: Self.WrappedElement) -> Column<Self.WrappedElement>
```

#### Return Value

A new column.

## Parameters

- `lhs`: An optional column type.
- `rhs`: A value of the same type as the optional column’s type.

## See Also

- [static func / (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](column/_(_:_:)-7or0v.md)
  Generates an integer column by dividing a value by each element in an optional column type.
- [static func / (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](column/_(_:_:)-1rwra.md)
  Generates a floating-point column by dividing each element in an optional column by a value.
- [static func / (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](column/_(_:_:)-2p0ex.md)
  Generates a floating-point column by dividing a value by each element in an optional column type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/_(_:_:)-60cwp)*