# MXLocationActivityMetric

**Framework**: MetricKit  
**Kind**: class

An object representing metrics about the use of location-tracking features of a device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class MXLocationActivityMetric
```

## Topics

### Reading location services use
- [var cumulativeBestAccuracyForNavigationTime: Measurement<UnitDuration>](mxlocationactivitymetric/cumulativebestaccuracyfornavigationtime.md)
  The total time spent tracking the current location at the best accuracy for navigation.
- [var cumulativeBestAccuracyTime: Measurement<UnitDuration>](mxlocationactivitymetric/cumulativebestaccuracytime.md)
  The total time spent tracking the current location at the best accuracy.
- [var cumulativeNearestTenMetersAccuracyTime: Measurement<UnitDuration>](mxlocationactivitymetric/cumulativenearesttenmetersaccuracytime.md)
  The total time spent tracking the current location to an accuracy of 10 meters.
- [var cumulativeHundredMetersAccuracyTime: Measurement<UnitDuration>](mxlocationactivitymetric/cumulativehundredmetersaccuracytime.md)
  The total time spent tracking the current location to an accuracy of 100 meters.
- [var cumulativeKilometerAccuracyTime: Measurement<UnitDuration>](mxlocationactivitymetric/cumulativekilometeraccuracytime.md)
  The total time spent tracking the current location to an accuracy of 1 kilometer.
- [var cumulativeThreeKilometersAccuracyTime: Measurement<UnitDuration>](mxlocationactivitymetric/cumulativethreekilometersaccuracytime.md)
  The total time spent tracking the current location to an accuracy of 3 kilometers.

## Relationships

### Inherits From
- [MXMetric](mxmetric.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class MXCellularConditionMetric](mxcellularconditionmetric.md)
  An object representing metrics about the condition of the cellular network.
- [class MXCPUMetric](mxcpumetric.md)
  An object representing metrics about the use of the CPU.
- [class MXDisplayMetric](mxdisplaymetric.md)
  An object representing metrics about the power used to display the app on the screen.
- [class MXGPUMetric](mxgpumetric.md)
  An object representing metrics about the use of the GPU.
- [class MXNetworkTransferMetric](mxnetworktransfermetric.md)
  An object representing metrics about network transfers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxlocationactivitymetric)*