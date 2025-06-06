# /(_:_:)

**Framework**: TabularData  
**Kind**: op

Generates a floating-point column by dividing each element in an optional column type by the corresponding elements of a column type.

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
func / <L, R>(lhs: L, rhs: R) -> Column<R.Element> where L : OptionalColumnProtocol, R : ColumnProtocol, L.WrappedElement : FloatingPoint, L.WrappedElement == R.Element
```

#### Return Value

A new column with the same type as the right column.

## Parameters

- `lhs`: An optional column type.
- `rhs`: A column type.

## See Also

- [static func / (Self, Self) -> Column<Self.Element>](columnprotocol/_(_:_:)-922ku.md)
  Generates an integer column by dividing each element in a column type by the corresponding elements of another.
- [func / <L, R>(L, R) -> Column<L.Element>](_(_:_:)-9v3nw.md)
  Generates an integer column by dividing each element in a column type by the corresponding elements of an optional column type.
- [func / <L, R>(L, R) -> Column<R.Element>](_(_:_:)-4igyw.md)
  Generates an integer column by dividing each element in an optional column type by the corresponding elements of a column type.
- [static func / (Self, Self) -> Column<Self.Element>](columnprotocol/_(_:_:)-2urf0.md)
  Generates a floating-point column by dividing each element in a column type by the corresponding elements of another.
- [func / <L, R>(L, R) -> Column<L.Element>](_(_:_:)-4pr65.md)
  Generates a floating-point column by dividing each element in a column type by the corresponding elements of an optional column type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/_(_:_:)-58kg6)*