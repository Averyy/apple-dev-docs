# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses a contiguous range of elements with an unbounded range.

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
subscript(range: UnboundedRange) -> DiscontiguousColumnSlice<WrappedElement> { get set }
```

## Parameters

- `range`: An unbounded range of valid indices in the column slice.

## See Also

### Accessing Elements
- [subscript(Int) -> DiscontiguousColumnSlice<WrappedElement>.Element](./subscript%28_%29-9y37v.md)
  Accesses an element at an index.
- [subscript(Range<Int>) -> DiscontiguousColumnSlice<WrappedElement>](./subscript%28_%29-8rd2f.md)
  Accesses a contiguous range of elements.
- [subscript<R>(R) -> DiscontiguousColumnSlice<WrappedElement>](./subscript%28_%29-4k2lh.md)
  Accesses a contiguous range of elements with a range expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice/subscript(_:)-5xvit)*