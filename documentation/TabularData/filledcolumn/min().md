# min()

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Returns the element with the lowest value.

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
func min() -> FilledColumn<Base>.Element?
```

Available when `Base` conforms to `OptionalColumnProtocol` and `Base.WrappedElement` conforms to `Comparable`.

## See Also

### Getting Statistical Values
- [func sum() -> FilledColumn<Base>.Element](./sum%28%29-5836l.md)
  Returns the sum of the integer column’s elements.
- [func sum() -> FilledColumn<Base>.Element](./sum%28%29-2805h.md)
  Returns the sum of the floating-point column’s elements.
- [func max() -> FilledColumn<Base>.Element?](./max%28%29.md)
  Returns the element with the highest value.
- [func mean() -> Double?](./mean%28%29-8xs60.md)
  Returns the mean average of the integer column’s elements.
- [func mean() -> FilledColumn<Base>.Element?](./mean%28%29-jd3v.md)
  Returns the mean average of the floating-point column’s elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> Double?](./standarddeviation%28deltadegreesoffreedom%29-4cofd.md)
  Returns the standard deviation of the integer column’s elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> FilledColumn<Base>.Element?](./standarddeviation%28deltadegreesoffreedom%29-27xnl.md)
  Returns the standard deviation of the floating-point column’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/filledcolumn/min())*