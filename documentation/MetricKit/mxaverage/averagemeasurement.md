# averageMeasurement

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The value of the average.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`average`](../averagestatistics/average.md) instead.

## Declaration

```swift
var averageMeasurement: Measurement<UnitType> { get }
```

```objc
@property (strong, readonly, nonnull) NSMeasurement<NSUnit *> * averageMeasurement;
```

## See Also

### Reading the data
- [var sampleCount: Int](./samplecount.md)
  The number of samples used to calculate the average.
- [var standardDeviation: Double](./standarddeviation.md)
  The standard deviation of the distribution of values used to calculate the average.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxaverage/averagemeasurement)*