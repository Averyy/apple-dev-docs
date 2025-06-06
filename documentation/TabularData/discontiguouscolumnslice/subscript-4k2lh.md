# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript

Accesses a contiguous range of elements with a range expression.

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
subscript<R>(range: R) -> DiscontiguousColumnSlice<WrappedElement> where R : RangeExpression, R.Bound == Int { get set }
```

## Parameters

- `range`: A range expression of valid indices in the column slice.

## See Also

- [subscript(Int) -> DiscontiguousColumnSlice<WrappedElement>.Element](discontiguouscolumnslice/subscript(_:)-9y37v.md)
  Accesses an element at an index.
- [subscript(Range<Int>) -> DiscontiguousColumnSlice<WrappedElement>](discontiguouscolumnslice/subscript(_:)-8rd2f.md)
  Accesses a contiguous range of elements.
- [subscript((UnboundedRange_) -> ()) -> DiscontiguousColumnSlice<WrappedElement>](discontiguouscolumnslice/subscript(_:)-5xvit.md)
  Accesses a contiguous range of elements with an unbounded range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice/subscript(_:)-4k2lh)*