# -=(_:_:)

**Framework**: TabularData  
**Kind**: op  
**Role**: Operator

Modifies a column slice by subtracting each optional value in a collection from the corresponding element in the column.

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
static func -= <C>(lhs: inout ColumnSlice<WrappedElement>, rhs: C) where WrappedElement : AdditiveArithmetic, C : Collection, C.Element == WrappedElement?
```

## Parameters

- `lhs`: A column.
- `rhs`: A collection that contains elements of the same type as the column’s elements.

## See Also

### Modifying a Column Slice with a Collection of Values
- [static func += <C>(inout ColumnSlice<WrappedElement>, C)](./pluseq%28_,_%29-47cwm.md)
  Modifies a column slice by adding each value in a collection to the corresponding element in the column.
- [static func += <C>(inout ColumnSlice<WrappedElement>, C)](./pluseq%28_,_%29-4bgdt.md)
  Modifies a column slice by adding each optional value in a collection to the corresponding element in the column.
- [static func -= <C>(inout ColumnSlice<WrappedElement>, C)](./minuseq%28_,_%29-3kauw.md)
  Modifies a column slice by subtracting each value in a collection from the corresponding element in the column.
- [static func *= <C>(inout ColumnSlice<WrappedElement>, C)](./stareq%28_,_%29-7lz8l.md)
  Modifies a column slice by multiplying each element in the column by the corresponding value in a collection.
- [static func *= <C>(inout ColumnSlice<WrappedElement>, C)](./stareq%28_,_%29-3v2q0.md)
  Modifies a column slice by multiplying each element in the column by the corresponding optional value in a collection.
- [static func /= <C>(inout ColumnSlice<WrappedElement>, C)](./opeq%28_,_%29-46jci.md)
  Modifies an integer column slice by dividing each element in the column by the corresponding value in a collection.
- [static func /= <C>(inout ColumnSlice<WrappedElement>, C)](./opeq%28_,_%29-8frqe.md)
  Modifies an integer column slice by dividing each element in the column by the corresponding optional value in a collection.
- [static func /= <C>(inout ColumnSlice<WrappedElement>, C)](./opeq%28_,_%29-1fciw.md)
  Modifies a floating-point column slice by dividing each element in the column by the corresponding value in a collection.
- [static func /= <C>(inout ColumnSlice<WrappedElement>, C)](./opeq%28_,_%29-6ujes.md)
  Modifies a floating-point column slice by dividing each element in the column by the corresponding optional value in a collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnslice/-=(_:_:)-1bqy4)*