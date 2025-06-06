# +(_:_:)

**Framework**: TabularData  
**Kind**: op

Generates a column by adding each element in a column type to the corresponding elements of another.

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
static func + (lhs: Self, rhs: Self) -> Column<Self.Element>
```

#### Return Value

A new column.

## Parameters

- `lhs`: A column type.
- `rhs`: Another column type.

## See Also

- [static func - (Self, Self) -> Column<Self.Element>](filledcolumn/-(_:_:)-bzdl.md)
  Generates a column by subtracting each element in a column type from the corresponding elements of another.
- [static func * (Self, Self) -> Column<Self.Element>](filledcolumn/*(_:_:)-6fyqv.md)
  Generates a column by multiplying each element in a column type by the corresponding elements of another.
- [static func / (Self, Self) -> Column<Self.Element>](filledcolumn/_(_:_:)-9h88r.md)
  Generates an integer column by dividing each element in a column type by the corresponding elements of another.
- [static func / (Self, Self) -> Column<Self.Element>](filledcolumn/_(_:_:)-82d1w.md)
  Generates a floating-point column by dividing each element in a column type by the corresponding elements of another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/filledcolumn/+(_:_:)-8qqh)*