# -(_:_:)

**Framework**: TabularData  
**Kind**: op

Generates a column by subtracting a value from each element in an optional column type.

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
static func - (lhs: Self, rhs: Self.WrappedElement) -> Column<Self.WrappedElement> where Self.WrappedElement : AdditiveArithmetic
```

#### Return Value

A new column.

## Parameters

- `lhs`: An optional column type.
- `rhs`: A value of the same type as the optional column’s type.

## See Also

- [static func + (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](optionalcolumnprotocol/+(_:_:)-501gg.md)
  Generates a column by adding a value to each element in an optional column.
- [static func + (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](optionalcolumnprotocol/+(_:_:)-6ko8x.md)
  Generates a column by adding each element in an optional column to a value.
- [static func - (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](optionalcolumnprotocol/-(_:_:)-5vffa.md)
  Generates a column by subtracting each element in an optional column from a value.
- [static func * (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](optionalcolumnprotocol/*(_:_:)-orkq.md)
  Generates a column by multiplying each element in an optional column by a value.
- [static func * (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](optionalcolumnprotocol/*(_:_:)-5vorv.md)
  Generates a column by multiplying a value by each element in an optional column type.
- [static func / (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](optionalcolumnprotocol/_(_:_:)-7tbmq.md)
  Generates an integer column by dividing each element in an optional column by a value.
- [static func / (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](optionalcolumnprotocol/_(_:_:)-56h1d.md)
  Generates an integer column by dividing a value by each element in an optional column type.
- [static func / (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](optionalcolumnprotocol/_(_:_:)-5qhxr.md)
  Generates a floating-point column by dividing each element in an optional column by a value.
- [static func / (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](optionalcolumnprotocol/_(_:_:)-2xfqa.md)
  Generates a floating-point column by dividing a value by each element in an optional column type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/optionalcolumnprotocol/-(_:_:)-9mejf)*