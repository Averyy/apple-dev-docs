# AverageStatistics

**Framework**: MetricKit  
**Kind**: struct

A value that encapsulates an average measurement with supporting statistical data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct AverageStatistics<DimensionType> where DimensionType : Dimension
```

## Mentions

- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)

#### Discussion

`AverageStatistics` provides the average value alongside a sample count and standard deviation. When statistical data is unavailable, `count` is `0` and `standardDeviation` is negative.

You encounter `AverageStatistics` as the type of certain metric properties, such as [`value`](suspendedmemorymetric/value.md) and [`averageMemory`](signpostintervalmetric/averagememory.md):

```swift
let statistics = metric.value // AverageStatistics<UnitInformationStorage>
print(statistics.average)           // Measurement<UnitInformationStorage>
print(statistics.count)             // Int — number of samples
print(statistics.standardDeviation) // Double — negative if unavailable
```

This type replaces [`MXAverage`](mxaverage.md).

## Topics

### Statistics
- [let average: Measurement<DimensionType>](averagestatistics/average.md)
  The average measurement value.
- [let count: Int](averagestatistics/count.md)
  The number of samples used to calculate the average.
- [let standardDeviation: Double?](averagestatistics/standarddeviation.md)
  The standard deviation of the distribution of values used to calculate the average.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct Histogram](histogram.md)
  A distribution of values organized into buckets.
- [class SignalBars](signalbars.md)
  A unit for cellular signal strength measurements in bars.
- [struct OSVersion](osversion.md)
  The version of the operating system on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/averagestatistics)*