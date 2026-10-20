# DateBins

**Framework**: Swift Charts  
**Kind**: struct  
**Role**: Structure

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
- [init(data: [Date], desiredCount: Int?, calendar: Calendar)](./datebins/init%28data,desiredcount,calendar%29.md)
  Automatically determine the bins from data.
- [init(range: ClosedRange<Date>, desiredCount: Int, calendar: Calendar)](./datebins/init%28range,desiredcount,calendar%29.md)
  Automatically determine the bins from a range of data.
- [init(thresholds: [Date])](./datebins/init%28thresholds%29.md)
  Creates N-1 bins with the given N `thresholds`.
- [init(timeInterval: TimeInterval, range: ClosedRange<Date>)](./datebins/init%28timeinterval,range%29.md)
  Creates uniform bins covering the given range. The first bin starts at the lower bound of the range.
- [init(unit: Calendar.Component, by: Int, range: ClosedRange<Date>, calendar: Calendar)](./datebins/init%28unit,by,range,calendar%29.md)
  Creates uniform bins covering the given range.
### Instance Properties
- [var thresholds: [Date]](./datebins/thresholds.md)
  Find the bin thresholds.
### Instance Methods
- [func index(for: Date) -> Int](./datebins/index%28for%29.md)
  Returns the bin index for the given value.

## Relationships

### Conforms To
- [Collection](../Swift/collection.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Data bins
- [struct NumberBins](./numberbins.md)
  A collection of bins for a chart that plots data against numbers.
- [struct ChartBinRange](./chartbinrange.md)
  The range of data that a single bin of a chart represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/datebins)*