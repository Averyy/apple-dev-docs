# ChartBinRange

**Framework**: Swift Charts  
**Kind**: struct

The range of data that a single bin of a chart represents.

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
struct ChartBinRange<Bound> where Bound : Comparable
```

#### Overview

All bins except the last for a particular chart represent an open range, meaning that the range doesn’t include the upper bound. The last range of the last bin is closed, so that it does include the upper bound. The system keeps track of the open or closed state of a particular range.

## Topics

### Instance Properties
- [let lowerBound: Bound](chartbinrange/lowerbound.md)
- [let upperBound: Bound](chartbinrange/upperbound.md)

## Relationships

### Conforms To
- [RangeExpression](../Swift/RangeExpression.md)

## See Also

- [struct NumberBins](numberbins.md)
  A collection of bins for a chart that plots data against numbers.
- [struct DateBins](datebins.md)
  A collection of bins for a chart that plots data against dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartbinrange)*