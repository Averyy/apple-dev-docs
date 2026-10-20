# min()

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

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
func min() -> ColumnSlice<WrappedElement>.Element
```

Available when `WrappedElement` conforms to `Comparable`.

## See Also

### Getting Statistical Values
- [func sum() -> WrappedElement](./sum%28%29.md)
  Returns the sum of the column slice’s elements, ignoring missing elements.
- [func max() -> ColumnSlice<WrappedElement>.Element](./max%28%29.md)
  Returns the element with the highest value, ignoring missing elements.
- [func mean() -> Double?](./mean%28%29-3inzf.md)
  Returns the mean average of the integer slice’s elements, ignoring missing elements.
- [func mean() -> ColumnSlice<WrappedElement>.Element](./mean%28%29-7u3i0.md)
  Returns the mean average of the floating-point slice’s elements, ignoring missing elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> Double?](./standarddeviation%28deltadegreesoffreedom%29-1i05i.md)
  Returns the standard deviation of the integer column slice’s elements, ignoring missing elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> ColumnSlice<WrappedElement>.Element](./standarddeviation%28deltadegreesoffreedom%29-3d6vo.md)
  Returns the standard deviation of the floating-point column slice’s elements, ignoring missing elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnslice/min())*