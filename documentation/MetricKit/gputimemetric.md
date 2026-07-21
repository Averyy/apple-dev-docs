# GPUTimeMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that measures the total GPU time used by the app.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct GPUTimeMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.gpuTime(_:)`](metricresult/gputime(_:).md) case. It appears only in [`intervalEntries`](metricreport/intervalentries.md) and is not included in state entries.

## Topics

### Measurements
- [let value: Measurement<UnitDuration>](gputimemetric/value.md)
  The total amount of GPU time used by the app.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MetalFrameRateMetric](metalframeratemetric.md)
  A metric that measures Metal frame rate statistics for a specific `CAMetalLayer`.
- [struct PixelLuminanceMetric](pixelluminancemetric.md)
  A metric that measures the average luminosity of pixels on an OLED display.
- [class AveragePixelLuminance](averagepixelluminance.md)
  A unit for average pixel luminance measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/gputimemetric)*