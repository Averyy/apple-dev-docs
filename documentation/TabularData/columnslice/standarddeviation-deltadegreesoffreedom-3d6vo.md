# standardDeviation(deltaDegreesOfFreedom:)

**Framework**: TabularData  
**Kind**: method

Returns the standard deviation of the floating-point column slice’s elements, ignoring missing elements.

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
func standardDeviation(deltaDegreesOfFreedom: Int = 1) -> ColumnSlice<WrappedElement>.Element
```

#### Return Value

The standard deviation; otherwise, `nil` if there are fewer than `deltaDegreesOfFreedom + 1` non-`nil` items in the column.

## Parameters

- `deltaDegreesOfFreedom`: A nonnegative integer.   The method calculates the standard deviation’s divisor by subtracting this parameter from the number of   non-  elements (  where   is the number of non-  elements).

## See Also

- [func sum() -> WrappedElement](columnslice/sum.md)
  Returns the sum of the column slice’s elements, ignoring missing elements.
- [func min() -> ColumnSlice<WrappedElement>.Element](columnslice/min.md)
  Returns the element with the lowest value, ignoring missing elements.
- [func max() -> ColumnSlice<WrappedElement>.Element](columnslice/max.md)
  Returns the element with the highest value, ignoring missing elements.
- [func mean() -> Double?](columnslice/mean-3inzf.md)
  Returns the mean average of the integer slice’s elements, ignoring missing elements.
- [func mean() -> ColumnSlice<WrappedElement>.Element](columnslice/mean-7u3i0.md)
  Returns the mean average of the floating-point slice’s elements, ignoring missing elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> Double?](columnslice/standarddeviation(deltadegreesoffreedom:)-1i05i.md)
  Returns the standard deviation of the integer column slice’s elements, ignoring missing elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnslice/standarddeviation(deltadegreesoffreedom:)-3d6vo)*