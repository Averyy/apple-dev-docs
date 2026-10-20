# histogrammedCellularConditionTime

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

An object representing the distribution of the different levels of connectivity to the cellular network.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`CellularConditionTimeMetric`](../cellularconditiontimemetric.md) instead.

## Declaration

```swift
var histogrammedCellularConditionTime: MXHistogram<MXUnitSignalBars> { get }
```

```objc
@property (strong, readonly, nonnull) MXHistogram<MXUnitSignalBars *> * histogrammedCellularConditionTime;
```

#### Discussion

Each bucket in the histogram is the percentage of total app runtime spent at the represented connectivity level during the reporting period.

## See Also

### Viewing cellular connectivity metrics
- [class MXUnitSignalBars](../mxunitsignalbars.md)
  A unit of measure for the number of bars of cellular network connectivity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcellularconditionmetric/histogrammedcellularconditiontime)*