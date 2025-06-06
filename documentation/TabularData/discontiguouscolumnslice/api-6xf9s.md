# /=(_:_:)

**Framework**: TabularData  
**Kind**: op

Modifies an integer column slice by dividing each element in the column by the corresponding value in a collection.

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
static func /= <C>(lhs: inout DiscontiguousColumnSlice<WrappedElement>, rhs: C) where WrappedElement : BinaryInteger, WrappedElement == C.Element, C : Collection
```

## Parameters

- `lhs`: A column.
- `rhs`: A collection that contains elements of the same type as the column’s elements.

## See Also

- [static func += <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](discontiguouscolumnslice/+=(_:_:)-2jxz1.md)
  Modifies a column slice by adding each value in a collection to the corresponding element in the column.
- [static func += <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](discontiguouscolumnslice/+=(_:_:)-lpai.md)
  Modifies a column slice by adding each optional value in a collection to the corresponding element in the column.
- [static func -= <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](discontiguouscolumnslice/-=(_:_:)-9nkq6.md)
  Modifies a column slice by subtracting each value in a collection from the corresponding element in the column.
- [static func -= <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](discontiguouscolumnslice/-=(_:_:)-8a20q.md)
  Modifies a column slice by subtracting each optional value in a collection from the corresponding element in the column.
- [static func *= <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](discontiguouscolumnslice/*=(_:_:)-9jg9h.md)
  Modifies a column slice by multiplying each element in the column by the corresponding value in a collection.
- [static func *= <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](discontiguouscolumnslice/*=(_:_:)-18nlr.md)
  Modifies a column slice by multiplying each element in the column by the corresponding optional value in a collection.
- [static func /= <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](discontiguouscolumnslice/_=(_:_:)-1mzcg.md)
  Modifies an integer column slice by dividing each element in the column by the corresponding optional value in a collection.
- [static func /= <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](discontiguouscolumnslice/_=(_:_:)-39wsi.md)
  Modifies a floating-point column slice by dividing each element in the column by the corresponding value in a collection.
- [static func /= <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](discontiguouscolumnslice/_=(_:_:)-6lzj.md)
  Modifies a floating-point column slice by dividing each element in the column by the corresponding optional value in a collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice/_=(_:_:)-6xf9s)*