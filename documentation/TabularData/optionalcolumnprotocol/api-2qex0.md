# +(_:_:)

**Framework**: TabularData  
**Kind**: op

Generates a column by adding each element in an optional column type to the corresponding elements of another.

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
static func + (lhs: Self, rhs: Self) -> Column<Self.WrappedElement>
```

#### Return Value

A new column.

## Parameters

- `lhs`: An optional column type.
- `rhs`: Another optional column type.

## See Also

- [func + <L, R>(L, R) -> Column<L.Element>](+(_:_:)-1i7oh.md)
  Generates a column by adding each element in a column type to the corresponding elements of an optional column type.
- [func + <L, R>(L, R) -> Column<R.Element>](+(_:_:)-3exmp.md)
  Generates a column by adding each element in an optional column type to the corresponding elements of a column type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/optionalcolumnprotocol/+(_:_:)-2qex0)*