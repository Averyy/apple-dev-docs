# /(_:_:)

**Framework**: TabularData  
**Kind**: op  
**Role**: Operator

Generates a floating-point column by dividing a value by each element in an optional column type.

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

Available when `WrappedElement` conforms to `FloatingPoint`.

#### Return Value

A new column.

## Parameters

- `lhs`: A value of the same type as the optional column.
- `rhs`: An optional column type.

## See Also

### Generating an Optional Column by Combining a Value
- [static func + (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](./plus%28_,_%29-501gg.md)
  Generates a column by adding a value to each element in an optional column.
- [static func + (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](./plus%28_,_%29-6ko8x.md)
  Generates a column by adding each element in an optional column to a value.
- [static func - (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](./minus%28_,_%29-9mejf.md)
  Generates a column by subtracting a value from each element in an optional column type.
- [static func - (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](./minus%28_,_%29-5vffa.md)
  Generates a column by subtracting each element in an optional column from a value.
- [static func * (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](./star%28_,_%29-orkq.md)
  Generates a column by multiplying each element in an optional column by a value.
- [static func * (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](./star%28_,_%29-5vorv.md)
  Generates a column by multiplying a value by each element in an optional column type.
- [static func / (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](./op%28_,_%29-7tbmq.md)
  Generates an integer column by dividing each element in an optional column by a value.
- [static func / (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](./op%28_,_%29-56h1d.md)
  Generates an integer column by dividing a value by each element in an optional column type.
- [static func / (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](./op%28_,_%29-5qhxr.md)
  Generates a floating-point column by dividing each element in an optional column by a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/optionalcolumnprotocol/_(_:_:)-2xfqa)*