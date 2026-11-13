# /(_:_:)

**Framework**: TabularData  
**Kind**: op  
**Role**: Operator

Generates an integer column by dividing a value by each element in a column.

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
static func / (lhs: Self.Element, rhs: Self) -> Column<Self.Element>
```

Available when `Element` conforms to `BinaryInteger`.

## Return Value

A new column.

## Parameters

- `lhs`: A value of the same type as the column.
- `rhs`: A column type.

## See Also

### Generating a column by dividing a value
- [static func / (Self, Self.Element) -> Column<Self.Element>](./op%28_,_%29-4a632.md)
  Generates an integer column by dividing each element in a column by a value.
- [static func / (Self, Self.Element) -> Column<Self.Element>](./op%28_,_%29-6zigz.md)
  Generates a floating-point column by dividing each element in a column by a value.
- [static func / (Self.Element, Self) -> Column<Self.Element>](./op%28_,_%29-4iv15.md)
  Generates a floating-point column by dividing a value by each element in a column.
- [static func / (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](../optionalcolumnprotocol/op%28_,_%29-5qhxr.md)
  Generates a floating-point column by dividing each element in an optional column by a value.
- [static func / (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](../optionalcolumnprotocol/op%28_,_%29-7tbmq.md)
  Generates an integer column by dividing each element in an optional column by a value.
- [static func / (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](../optionalcolumnprotocol/op%28_,_%29-2xfqa.md)
  Generates a floating-point column by dividing a value by each element in an optional column type.
- [static func / (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](../optionalcolumnprotocol/op%28_,_%29-56h1d.md)
  Generates an integer column by dividing a value by each element in an optional column type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnprotocol/_(_:_:)-7pe3t)*