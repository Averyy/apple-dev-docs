# /(_:_:)

**Framework**: TabularData  
**Kind**: op

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

#### Return Value

A new column.

## Parameters

- `lhs`: An optional column type.
- `rhs`: Another optional column type.

## See Also

- [static func / (Self, Self) -> Column<Self.WrappedElement>](optionalcolumnprotocol/_(_:_:)-4nmnl.md)
  Generates an integer column by dividing each element in an optional column type by the corresponding elements of another.
- [func / <L, R>(L, R) -> Column<L.Element>](_(_:_:)-9v3nw.md)
  Generates an integer column by dividing each element in a column type by the corresponding elements of an optional column type.
- [func / <L, R>(L, R) -> Column<R.Element>](_(_:_:)-4igyw.md)
  Generates an integer column by dividing each element in an optional column type by the corresponding elements of a column type.
- [func / <L, R>(L, R) -> Column<L.Element>](_(_:_:)-4pr65.md)
  Generates a floating-point column by dividing each element in a column type by the corresponding elements of an optional column type.
- [func / <L, R>(L, R) -> Column<R.Element>](_(_:_:)-58kg6.md)
  Generates a floating-point column by dividing each element in an optional column type by the corresponding elements of a column type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/optionalcolumnprotocol/_(_:_:)-3rlo3)*