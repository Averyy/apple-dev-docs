# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript

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
subscript(range: (UnboundedRange_) -> ()) -> DiscontiguousColumnSlice<WrappedElement> { get set }
```

## Parameters

- `range`: An unbounded range of valid indices in the column slice.

## See Also

- [subscript(Int) -> DiscontiguousColumnSlice<WrappedElement>.Element](discontiguouscolumnslice/subscript(_:)-9y37v.md)
  Accesses an element at an index.
- [subscript(Range<Int>) -> DiscontiguousColumnSlice<WrappedElement>](discontiguouscolumnslice/subscript(_:)-8rd2f.md)
  Accesses a contiguous range of elements.
- [subscript<R>(R) -> DiscontiguousColumnSlice<WrappedElement>](discontiguouscolumnslice/subscript(_:)-4k2lh.md)
  Accesses a contiguous range of elements with a range expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice/subscript(_:)-5xvit)*