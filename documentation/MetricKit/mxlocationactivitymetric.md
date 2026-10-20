# MXLocationActivityMetric

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

An object representing metrics about the use of location-tracking features of a device.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`LocationActivityTimeMetric`](./locationactivitytimemetric.md) instead.

## Declaration

```swift
class MXLocationActivityMetric
```

```objc
@interface MXLocationActivityMetric : MXMetric
```

## Topics

### Reading location services use
- [var cumulativeBestAccuracyForNavigationTime: Measurement<UnitDuration>](./mxlocationactivitymetric/cumulativebestaccuracyfornavigationtime.md)
  The total time spent tracking the current location at the best accuracy for navigation.
- [var cumulativeBestAccuracyTime: Measurement<UnitDuration>](./mxlocationactivitymetric/cumulativebestaccuracytime.md)
  The total time spent tracking the current location at the best accuracy.
- [var cumulativeNearestTenMetersAccuracyTime: Measurement<UnitDuration>](./mxlocationactivitymetric/cumulativenearesttenmetersaccuracytime.md)
  The total time spent tracking the current location to an accuracy of 10 meters.
- [var cumulativeHundredMetersAccuracyTime: Measurement<UnitDuration>](./mxlocationactivitymetric/cumulativehundredmetersaccuracytime.md)
  The total time spent tracking the current location to an accuracy of 100 meters.
- [var cumulativeKilometerAccuracyTime: Measurement<UnitDuration>](./mxlocationactivitymetric/cumulativekilometeraccuracytime.md)
  The total time spent tracking the current location to an accuracy of 1 kilometer.
- [var cumulativeThreeKilometersAccuracyTime: Measurement<UnitDuration>](./mxlocationactivitymetric/cumulativethreekilometersaccuracytime.md)
  The total time spent tracking the current location to an accuracy of 3 kilometers.

## Relationships

### Inherits From
- [MXMetric](./mxmetric.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Battery and resource metrics
- [class MXCellularConditionMetric](./mxcellularconditionmetric.md)
  An object representing metrics about the condition of the cellular network.
- [class MXCPUMetric](./mxcpumetric.md)
  An object representing metrics about the use of the CPU.
- [class MXDisplayMetric](./mxdisplaymetric.md)
  An object representing metrics about the power used to display the app on the screen.
- [class MXGPUMetric](./mxgpumetric.md)
  An object representing metrics about the use of the GPU.
- [class MXNetworkTransferMetric](./mxnetworktransfermetric.md)
  An object representing metrics about network transfers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxlocationactivitymetric)*