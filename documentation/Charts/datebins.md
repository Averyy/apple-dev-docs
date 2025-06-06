# DateBins

**Framework**: Swift Charts  
**Kind**: struct

A collection of bins for a chart that plots data against dates.

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
struct DateBins
```

## Topics

### Initializers
- [init(data: [Date], desiredCount: Int?, calendar: Calendar)](datebins/init(data:desiredcount:calendar:).md)
  Automatically determine the bins from data.
- [init(range: ClosedRange<Date>, desiredCount: Int, calendar: Calendar)](datebins/init(range:desiredcount:calendar:).md)
  Automatically determine the bins from a range of data.
- [init(thresholds: [Date])](datebins/init(thresholds:).md)
  Creates N-1 bins with the given N `thresholds`.
- [init(timeInterval: TimeInterval, range: ClosedRange<Date>)](datebins/init(timeinterval:range:).md)
  Creates uniform bins covering the given range. The first bin starts at the lower bound of the range.
- [init(unit: Calendar.Component, by: Int, range: ClosedRange<Date>, calendar: Calendar)](datebins/init(unit:by:range:calendar:).md)
  Creates uniform bins covering the given range.
### Instance Properties
- [var thresholds: [Date]](datebins/thresholds.md)
  Find the bin thresholds.
### Instance Methods
- [func index(for: Date) -> Int](datebins/index(for:).md)
  Returns the bin index for the given value.

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct NumberBins](numberbins.md)
  A collection of bins for a chart that plots data against numbers.
- [struct ChartBinRange](chartbinrange.md)
  The range of data that a single bin of a chart represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/datebins)*