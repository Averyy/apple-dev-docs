# min()

**Framework**: TabularData  
**Kind**: method

Returns the element with the lowest value, ignoring missing elements.

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
func min() -> DiscontiguousColumnSlice<WrappedElement>.Element
```

## See Also

- [func sum() -> WrappedElement](discontiguouscolumnslice/sum.md)
  Returns the sum of the column slice’s elements, ignoring missing elements.
- [func max() -> DiscontiguousColumnSlice<WrappedElement>.Element](discontiguouscolumnslice/max.md)
  Returns the element with the highest value, ignoring missing elements.
- [func mean() -> DiscontiguousColumnSlice<WrappedElement>.Element](discontiguouscolumnslice/mean-3y11c.md)
  Returns the mean average of the floating-point slice’s elements, ignoring missing elements.
- [func mean() -> Double?](discontiguouscolumnslice/mean-49u93.md)
  Returns the mean average of the integer slice’s elements, ignoring missing elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> Double?](discontiguouscolumnslice/standarddeviation(deltadegreesoffreedom:)-36nx2.md)
  Returns the standard deviation of the integer column slice’s elements, ignoring missing elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> DiscontiguousColumnSlice<WrappedElement>.Element](discontiguouscolumnslice/standarddeviation(deltadegreesoffreedom:)-5vd4r.md)
  Returns the standard deviation of the floating-point column slice’s elements, ignoring missing elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice/min())*