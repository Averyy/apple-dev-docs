# standardDeviation(deltaDegreesOfFreedom:)

**Framework**: TabularData  
**Kind**: method

Returns the standard deviation of the integer column’s elements, ignoring missing elements.

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

- [func sum() -> WrappedElement](column/sum.md)
  Returns the sum of the column’s elements, ignoring missing elements.
- [func min() -> Column<WrappedElement>.Element](column/min.md)
  Returns the element with the lowest value, ignoring missing elements.
- [func max() -> Column<WrappedElement>.Element](column/max.md)
  Returns the element with the highest value, ignoring missing elements.
- [func mean() -> Double?](column/mean-2si7j.md)
  Returns the mean average of the integer column’s elements, ignoring missing elements.
- [func mean() -> Column<WrappedElement>.Element](column/mean-ic5z.md)
  Returns the mean average of the floating-point column’s elements, ignoring missing elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> Column<WrappedElement>.Element](column/standarddeviation(deltadegreesoffreedom:)-4kc16.md)
  Returns the standard deviation of the floating-point column’s elements, ignoring missing elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/standarddeviation(deltadegreesoffreedom:)-9ffqu)*