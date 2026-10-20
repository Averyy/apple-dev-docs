# cumulativeLogicalWrites

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The total amount of data written to disk or other long term storage.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`LogicalDiskWritesMetric`](../logicaldiskwritesmetric.md) instead.

## Declaration

```swift
var cumulativeLogicalWrites: Measurement<UnitInformationStorage> { get }
```

```objc
@property (strong, readonly, nonnull) NSMeasurement<NSUnitInformationStorage *> * cumulativeLogicalWrites;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiskiometric/cumulativelogicalwrites)*