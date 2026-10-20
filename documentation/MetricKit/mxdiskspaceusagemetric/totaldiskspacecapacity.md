# totalDiskSpaceCapacity

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The total disk space capacity of the current device.

**Availability**:
- iOS 26.0+ - Deprecated in 27.2
- iPadOS 26.0+ - Deprecated in 27.2
- Mac Catalyst 26.0+ - Deprecated in 27.0
- macOS 26.0+ - Deprecated in 27.2
- visionOS 26.0+ - Deprecated in 27.2

> **Deprecated**: Use [`TotalDiskSpaceCapacityMetric`](../totaldiskspacecapacitymetric.md) instead.

## Declaration

```swift
var totalDiskSpaceCapacity: Measurement<UnitInformationStorage> { get }
```

```objc
@property (strong, readonly, nonnull) NSMeasurement<NSUnitInformationStorage *> * totalDiskSpaceCapacity;
```

#### Discussion

Calculate the amount of free space on this device by subtracting [`totalDiskSpaceUsedSize`](./totaldiskspaceusedsize.md) from this value.

## See Also

### Reading disk capacity and space
- [var totalDiskSpaceUsedSize: Measurement<UnitInformationStorage>](./totaldiskspaceusedsize.md)
  The total amount of used disk storage on the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiskspaceusagemetric/totaldiskspacecapacity)*