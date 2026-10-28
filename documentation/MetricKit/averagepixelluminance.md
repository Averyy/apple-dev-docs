# AveragePixelLuminance

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

A unit for average pixel luminance measurements.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
@objc
final class AveragePixelLuminance
```

## Discussion

This is used as the `Dimension` type in [`value`](./pixelluminancemetric/value.md), which has type `AverageStatistics<AveragePixelLuminance>`. The base unit symbol is `"apl"` (average pixel luminance).

## Topics

### Type Methods
- [static func baseUnit() -> AveragePixelLuminance](./averagepixelluminance/baseunit%28%29.md)

## Relationships

### Inherits From
- [Dimension](../Foundation/dimension.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### GPU and display metrics
- [struct GPUTimeMetric](./gputimemetric.md)
  A metric that measures the total GPU time used by the app.
- [struct MetalFrameRateMetric](./metalframeratemetric.md)
  A metric that measures Metal frame rate statistics for a specific `CAMetalLayer`.
- [struct PixelLuminanceMetric](./pixelluminancemetric.md)
  A metric that measures the average luminosity of pixels on an OLED display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/averagepixelluminance)*