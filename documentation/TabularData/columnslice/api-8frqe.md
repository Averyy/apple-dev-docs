# /=(_:_:)

**Framework**: TabularData  
**Kind**: op

Modifies an integer column slice by dividing each element in the column by the corresponding optional value in a collection.

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
static func /= <C>(lhs: inout ColumnSlice<WrappedElement>, rhs: C) where WrappedElement : BinaryInteger, C : Collection, C.Element == WrappedElement?
```

## Parameters

- `lhs`: A column.
- `rhs`: A collection that contains elements of the same type as the column’s elements.

## See Also

- [static func += <C>(inout ColumnSlice<WrappedElement>, C)](columnslice/+=(_:_:)-47cwm.md)
  Modifies a column slice by adding each value in a collection to the corresponding element in the column.
- [static func += <C>(inout ColumnSlice<WrappedElement>, C)](columnslice/+=(_:_:)-4bgdt.md)
  Modifies a column slice by adding each optional value in a collection to the corresponding element in the column.
- [static func -= <C>(inout ColumnSlice<WrappedElement>, C)](columnslice/-=(_:_:)-3kauw.md)
  Modifies a column slice by subtracting each value in a collection from the corresponding element in the column.
- [static func -= <C>(inout ColumnSlice<WrappedElement>, C)](columnslice/-=(_:_:)-1bqy4.md)
  Modifies a column slice by subtracting each optional value in a collection from the corresponding element in the column.
- [static func *= <C>(inout ColumnSlice<WrappedElement>, C)](columnslice/*=(_:_:)-7lz8l.md)
  Modifies a column slice by multiplying each element in the column by the corresponding value in a collection.
- [static func *= <C>(inout ColumnSlice<WrappedElement>, C)](columnslice/*=(_:_:)-3v2q0.md)
  Modifies a column slice by multiplying each element in the column by the corresponding optional value in a collection.
- [static func /= <C>(inout ColumnSlice<WrappedElement>, C)](columnslice/_=(_:_:)-46jci.md)
  Modifies an integer column slice by dividing each element in the column by the corresponding value in a collection.
- [static func /= <C>(inout ColumnSlice<WrappedElement>, C)](columnslice/_=(_:_:)-1fciw.md)
  Modifies a floating-point column slice by dividing each element in the column by the corresponding value in a collection.
- [static func /= <C>(inout ColumnSlice<WrappedElement>, C)](columnslice/_=(_:_:)-6ujes.md)
  Modifies a floating-point column slice by dividing each element in the column by the corresponding optional value in a collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnslice/_=(_:_:)-8frqe)*