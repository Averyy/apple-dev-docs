# totalDiskSpaceCapacity

**Framework**: MetricKit  
**Kind**: property

The total disk space capacity of the current device.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var totalDiskSpaceCapacity: Measurement<UnitInformationStorage> { get }
```

#### Discussion

You can calulate the amount of free space on this device by subtracting [`totalDiskSpaceUsedSize`](mxdiskspaceusagemetric/totaldiskspaceusedsize.md) from this value.

## See Also

- [var totalDiskSpaceUsedSize: Measurement<UnitInformationStorage>](mxdiskspaceusagemetric/totaldiskspaceusedsize.md)
  The total amount of used disk storage on the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiskspaceusagemetric/totaldiskspacecapacity)*