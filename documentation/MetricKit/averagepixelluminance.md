# AveragePixelLuminance

**Framework**: MetricKit  
**Kind**: class

A unit for average pixel luminance measurements.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
@objc
final class AveragePixelLuminance
```

#### Discussion

This is used as the `Dimension` type in [`value`](pixelluminancemetric/value.md), which has type `AverageStatistics<AveragePixelLuminance>`. The base unit symbol is `"apl"` (average pixel luminance).

## Topics

### Type Methods
- [static func baseUnit() -> AveragePixelLuminance](averagepixelluminance/baseunit.md)

## Relationships

### Inherits From
- [Dimension](../Foundation/Dimension.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct GPUTimeMetric](gputimemetric.md)
  A metric that measures the total GPU time used by the app.
- [struct MetalFrameRateMetric](metalframeratemetric.md)
  A metric that measures Metal frame rate statistics for a specific `CAMetalLayer`.
- [struct PixelLuminanceMetric](pixelluminancemetric.md)
  A metric that measures the average luminosity of pixels on an OLED display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/averagepixelluminance)*