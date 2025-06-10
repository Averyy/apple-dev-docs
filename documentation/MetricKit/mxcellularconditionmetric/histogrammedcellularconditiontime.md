# histogrammedCellularConditionTime

**Framework**: MetricKit  
**Kind**: property

An object representing the distribution of the different levels of connectivity to the cellular network.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var histogrammedCellularConditionTime: MXHistogram<MXUnitSignalBars> { get }
```

#### Discussion

Each bucket in the histogram is the percentage of total app runtime spent at the represented connectivity level during the reporting period.

## See Also

- [class MXUnitSignalBars](mxunitsignalbars.md)
  A unit of measure for the number of bars of cellular network connectivity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcellularconditionmetric/histogrammedcellularconditiontime)*