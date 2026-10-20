# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript  
**Role**: Instance Subscript

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

### Accessing Elements
- [subscript(Int) -> DiscontiguousColumnSlice<WrappedElement>.Element](./subscript%28_%29-9y37v.md)
  Accesses an element at an index.
- [subscript(Range<Int>) -> DiscontiguousColumnSlice<WrappedElement>](./subscript%28_%29-8rd2f.md)
  Accesses a contiguous range of elements.
- [subscript(UnboundedRange) -> DiscontiguousColumnSlice<WrappedElement>](./subscript%28_%29-5xvit.md)
  Accesses a contiguous range of elements with an unbounded range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice/subscript(_:)-4k2lh)*