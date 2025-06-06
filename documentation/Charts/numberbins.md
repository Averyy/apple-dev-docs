# NumberBins

**Framework**: Swift Charts  
**Kind**: struct

A collection of bins for a chart that plots data against numbers.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct NumberBins<Value> where Value : Comparable, Value : Numeric
```

## Topics

### Initializers
- [init(data: [Value], desiredCount: Int?, minimumStride: Value)](numberbins/init(data:desiredcount:minimumstride:)-3txi5.md)
  Automatically determine the bins from data.
- [init(data: [Value], desiredCount: Int?, minimumStride: Value)](numberbins/init(data:desiredcount:minimumstride:)-8pvv7.md)
  Automatically determine the bins from data.
- [init(range: ClosedRange<Value>, count: Int)](numberbins/init(range:count:)-6hip8.md)
  Creates the given number of bins for the range. Expects that the range length is a multiple of `count` to allow uniform integer bins.
- [init(range: ClosedRange<Value>, count: Int)](numberbins/init(range:count:)-7975l.md)
  Creates the given number of bins for the range.
- [init(range: ClosedRange<Value>, desiredCount: Int, minimumStride: Value)](numberbins/init(range:desiredcount:minimumstride:)-32ok2.md)
  Automatically determine the bins from a range of data.
- [init(range: ClosedRange<Value>, desiredCount: Int, minimumStride: Value)](numberbins/init(range:desiredcount:minimumstride:)-4qxfa.md)
  Automatically determine the bins from a range of data.
- [init(size: Value, range: ClosedRange<Value>)](numberbins/init(size:range:)-3ach2.md)
  Creates uniform bins covering the given range.
- [init(size: Value, range: ClosedRange<Value>)](numberbins/init(size:range:)-5me6y.md)
  Creates uniform bins covering the given range.
- [init(thresholds: [Value])](numberbins/init(thresholds:).md)
  Creates N-1 bins with the given N `thresholds`.
### Instance Properties
- [var thresholds: [Value]](numberbins/thresholds.md)
  Find the bin thresholds.
### Instance Methods
- [func index(for: Value) -> Int](numberbins/index(for:).md)
  Returns the bin index for the given value.

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct DateBins](datebins.md)
  A collection of bins for a chart that plots data against dates.
- [struct ChartBinRange](chartbinrange.md)
  The range of data that a single bin of a chart represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/numberbins)*