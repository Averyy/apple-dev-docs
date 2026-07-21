# Histogram

**Framework**: MetricKit  
**Kind**: struct

A distribution of values organized into buckets.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct Histogram<DimensionType> where DimensionType : Dimension
```

## Mentions

- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)

#### Discussion

Each [`Histogram.Bucket`](histogram/bucket.md) in the [`buckets`](histogram/buckets.md) array covers a range from [`lowerBound`](histogram/bucket/lowerbound.md) to [`upperBound`](histogram/bucket/upperbound.md) and reports the number of samples in that range via [`count`](histogram/bucket/count.md).

You encounter `Histogram` as the type of properties on various metric structs, such as [`histogram`](hangtimemetric/histogram.md) and [`histogram`](timetofirstdrawmetric/histogram.md):

```swift
let histogram = metric.histogram // Histogram<UnitDuration>
for bucket in histogram.buckets {
    let lower = bucket.lowerBound
    let upper = bucket.upperBound
    let count = bucket.count
}
```

## Topics

### Buckets
- [let buckets: [Histogram<DimensionType>.Bucket]](histogram/buckets.md)
### Structures
- [Histogram.Bucket](histogram/bucket.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AverageStatistics](averagestatistics.md)
  A value that encapsulates an average measurement with supporting statistical data.
- [class SignalBars](signalbars.md)
  A unit for cellular signal strength measurements in bars.
- [struct OSVersion](osversion.md)
  The version of the operating system on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/histogram)*