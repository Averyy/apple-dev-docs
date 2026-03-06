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

- [static func + (Self, Self.Element) -> Column<Self.Element>](columnprotocol/+(_:_:)-39k8v.md)
  Generates a column by adding a value to each element in a column.
- [static func - (Self.Element, Self) -> Column<Self.Element>](columnprotocol/-(_:_:)-4fynh.md)
  Generates a column by subtracting each element in a column from a value.
- [static func - (Self, Self.Element) -> Column<Self.Element>](columnprotocol/-(_:_:)-6up21.md)
  Generates a column by subtracting a value from each element in a column.
- [static func * (Self, Self.Element) -> Column<Self.Element>](columnprotocol/*(_:_:)-17vqd.md)
  Generates a column by multiplying each element in a column by a value.
- [static func * (Self.Element, Self) -> Column<Self.Element>](columnprotocol/*(_:_:)-3d6lu.md)
  Generates a column by multiplying a value by each element in a column.
- [static func / (Self, Self.Element) -> Column<Self.Element>](columnprotocol/_(_:_:)-4a632.md)
  Generates an integer column by dividing each element in a column by a value.
- [static func / (Self.Element, Self) -> Column<Self.Element>](columnprotocol/_(_:_:)-7pe3t.md)
  Generates an integer column by dividing a value by each element in a column.
- [static func / (Self, Self.Element) -> Column<Self.Element>](columnprotocol/_(_:_:)-6zigz.md)
  Generates a floating-point column by dividing each element in a column by a value.
- [static func / (Self.Element, Self) -> Column<Self.Element>](columnprotocol/_(_:_:)-4iv15.md)
  Generates a floating-point column by dividing a value by each element in a column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnprotocol/+(_:_:)-94kiv)*