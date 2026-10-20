# MXDisplayMetric

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

An object representing metrics about the power used to display the app on the screen.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricResult`](./metricresult.md), and read the [`PixelLuminanceMetric`](./pixelluminancemetric.md) case instead.

## Declaration

```swift
class MXDisplayMetric
```

```objc
@interface MXDisplayMetric : MXMetric
```

## Topics

### Reading average active pixel use
- [var averagePixelLuminance: MXAverage<MXUnitAveragePixelLuminance>?](./mxdisplaymetric/averagepixelluminance.md)
  The average amount of luminosity of the pixels on an OLED display.
- [class MXUnitAveragePixelLuminance](./mxunitaveragepixelluminance.md)
  A unit of measure of pixel luminosity on an OLED display.

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
- [class MXGPUMetric](./mxgpumetric.md)
  An object representing metrics about the use of the GPU.
- [class MXLocationActivityMetric](./mxlocationactivitymetric.md)
  An object representing metrics about the use of location-tracking features of a device.
- [class MXNetworkTransferMetric](./mxnetworktransfermetric.md)
  An object representing metrics about network transfers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdisplaymetric)*