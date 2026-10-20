# *=(_:_:)

**Framework**: TabularData  
**Kind**: op  
**Role**: Operator

Modifies a column by multiplying each element in the column by the corresponding optional value in a collection.

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
static func *= <C>(lhs: inout Column<WrappedElement>, rhs: C) where WrappedElement : Numeric, C : Collection, C.Element == WrappedElement?
```

## Parameters

- `lhs`: A column.
- `rhs`: A collection that contains elements of the same type as the column’s elements.

## See Also

### Modifying a Column with a Collection of Values
- [static func += <C>(inout Column<WrappedElement>, C)](./pluseq%28_,_%29-2w5o4.md)
  Modifies a column by adding each value in a collection to the corresponding element in the column.
- [static func += <C>(inout Column<WrappedElement>, C)](./pluseq%28_,_%29-2scuy.md)
  Modifies a column by adding each optional value in a collection to the corresponding element in the column.
- [static func -= <C>(inout Column<WrappedElement>, C)](./minuseq%28_,_%29-8rgjq.md)
  Modifies a column by subtracting each value in a collection from the corresponding element in the column.
- [static func -= <C>(inout Column<WrappedElement>, C)](./minuseq%28_,_%29-3v0hh.md)
  Modifies a column by subtracting each optional value in a collection from the corresponding element in the column.
- [static func *= <C>(inout Column<WrappedElement>, C)](./stareq%28_,_%29-8mmnn.md)
  Modifies a column by multiplying each element in the column by the corresponding value in a collection.
- [static func /= <C>(inout Column<WrappedElement>, C)](./opeq%28_,_%29-dnma.md)
  Modifies an integer column by dividing each element in the column by the corresponding value in a collection.
- [static func /= <C>(inout Column<WrappedElement>, C)](./opeq%28_,_%29-8xhzg.md)
  Modifies an integer column by dividing each element in the column by the corresponding optional value in a collection.
- [static func /= <C>(inout Column<WrappedElement>, C)](./opeq%28_,_%29-86t1j.md)
  Modifies a floating-point column by dividing each element in the column by the corresponding value in a collection.
- [static func /= <C>(inout Column<WrappedElement>, C)](./opeq%28_,_%29-3acz8.md)
  Modifies a floating-point column by dividing each element in the column by the corresponding optional value in a collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/*=(_:_:)-6kp11)*