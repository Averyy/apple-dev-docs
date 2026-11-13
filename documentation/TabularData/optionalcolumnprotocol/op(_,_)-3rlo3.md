# /(_:_:)

**Framework**: TabularData  
**Kind**: op  
**Role**: Operator

Generates a floating-point column by dividing each element in an optional column type by the corresponding elements of another.

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
static func / (lhs: Self, rhs: Self) -> Column<Self.WrappedElement>
```

Available when `WrappedElement` conforms to `FloatingPoint`.

## Return Value

A new column.

## Parameters

- `lhs`: An optional column type.
- `rhs`: Another optional column type.

## See Also

### Generating a column by combining two columns
- [static func + (Self, Self) -> Column<Self.Element>](../columnprotocol/plus%28_,_%29-yc11.md)
  Generates a column by adding each element in a column type to the corresponding elements of another.
- [static func + (Self, Self) -> Column<Self.WrappedElement>](./plus%28_,_%29-2qex0.md)
  Generates a column by adding each element in an optional column type to the corresponding elements of another.
- [static func - (Self, Self) -> Column<Self.Element>](../columnprotocol/minus%28_,_%29-36zol.md)
  Generates a column by subtracting each element in a column type from the corresponding elements of another.
- [static func - (Self, Self) -> Column<Self.WrappedElement>](./minus%28_,_%29-5xfkx.md)
  Generates a column by subtracting each element in an optional column type from the corresponding elements of another.
- [static func * (Self, Self) -> Column<Self.Element>](../columnprotocol/star%28_,_%29-9db1q.md)
  Generates a column by multiplying each element in a column type by the corresponding elements of another.
- [static func * (Self, Self) -> Column<Self.WrappedElement>](./star%28_,_%29-5f5kx.md)
  Generates a column by multiplying each element in an optional column type by the corresponding elements of another.
- [static func / (Self, Self) -> Column<Self.Element>](../columnprotocol/op%28_,_%29-2urf0.md)
  Generates a floating-point column by dividing each element in a column type by the corresponding elements of another.
- [static func / (Self, Self) -> Column<Self.Element>](../columnprotocol/op%28_,_%29-922ku.md)
  Generates an integer column by dividing each element in a column type by the corresponding elements of another.
- [static func / (Self, Self) -> Column<Self.WrappedElement>](./op%28_,_%29-4nmnl.md)
  Generates an integer column by dividing each element in an optional column type by the corresponding elements of another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/optionalcolumnprotocol/_(_:_:)-3rlo3)*