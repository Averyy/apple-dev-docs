# standardDeviation(deltaDegreesOfFreedom:)

**Framework**: TabularData  
**Kind**: method

Returns the standard deviation of the integer column’s elements.

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
func standardDeviation(deltaDegreesOfFreedom: Int = 1) -> Double?
```

#### Return Value

The standard deviation; otherwise, `nil` if there are fewer than `deltaDegreesOfFreedom + 1` non-`nil` items in the column.

## Parameters

- `deltaDegreesOfFreedom`: A nonnegative integer.   The method calculates the standard deviation’s divisor by subtracting this parameter from the number of   non-  elements (  where   is the number of non-  elements).

## See Also

- [func sum() -> FilledColumn<Base>.Element](filledcolumn/sum-5836l.md)
  Returns the sum of the integer column’s elements.
- [func sum() -> FilledColumn<Base>.Element](filledcolumn/sum-2805h.md)
  Returns the sum of the floating-point column’s elements.
- [func min() -> FilledColumn<Base>.Element?](filledcolumn/min.md)
  Returns the element with the lowest value.
- [func max() -> FilledColumn<Base>.Element?](filledcolumn/max.md)
  Returns the element with the highest value.
- [func mean() -> Double?](filledcolumn/mean-8xs60.md)
  Returns the mean average of the integer column’s elements.
- [func mean() -> FilledColumn<Base>.Element?](filledcolumn/mean-jd3v.md)
  Returns the mean average of the floating-point column’s elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> FilledColumn<Base>.Element?](filledcolumn/standarddeviation(deltadegreesoffreedom:)-27xnl.md)
  Returns the standard deviation of the floating-point column’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/filledcolumn/standarddeviation(deltadegreesoffreedom:)-4cofd)*