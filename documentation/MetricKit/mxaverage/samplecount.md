# sampleCount

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The number of samples used to calculate the average.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`count`](../averagestatistics/count.md) instead.

## Declaration

```swift
var sampleCount: Int { get }
```

```objc
@property (readonly) NSInteger sampleCount;
```

## See Also

### Reading the data
- [var averageMeasurement: Measurement<UnitType>](./averagemeasurement.md)
  The value of the average.
- [var standardDeviation: Double](./standarddeviation.md)
  The standard deviation of the distribution of values used to calculate the average.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxaverage/samplecount)*