# totalDiskSpaceUsedSize

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The total amount of used disk storage on the current device.

**Availability**:
- iOS 26.0+ - Deprecated in 27.2
- iPadOS 26.0+ - Deprecated in 27.2
- Mac Catalyst 26.0+ - Deprecated in 27.0
- macOS 26.0+ - Deprecated in 27.2
- visionOS 26.0+ - Deprecated in 27.2

> **Deprecated**: Use [`TotalDiskSpaceCapacityMetric`](../totaldiskspacecapacitymetric.md) instead.

## Declaration

```swift
var totalDiskSpaceUsedSize: Measurement<UnitInformationStorage> { get }
```

```objc
@property (strong, readonly, nonnull) NSMeasurement<NSUnitInformationStorage *> * totalDiskSpaceUsedSize;
```

## See Also

### Reading disk capacity and space
- [var totalDiskSpaceCapacity: Measurement<UnitInformationStorage>](./totaldiskspacecapacity.md)
  The total disk space capacity of the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiskspaceusagemetric/totaldiskspaceusedsize)*