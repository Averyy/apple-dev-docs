# GPUTimeMetric

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

A metric that measures the total GPU time used by the app.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
struct GPUTimeMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.gpuTime(_:)`](./metricresult/gputime%28_%29.md) case. It appears only in [`intervalEntries`](./metricreport/intervalentries.md) and is not included in state entries.

## Topics

### Measurements
- [let value: Measurement<UnitDuration>](./gputimemetric/value.md)
  The total amount of GPU time used by the app.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### GPU and display metrics
- [struct MetalFrameRateMetric](./metalframeratemetric.md)
  A metric that measures Metal frame rate statistics for a specific `CAMetalLayer`.
- [struct PixelLuminanceMetric](./pixelluminancemetric.md)
  A metric that measures the average luminosity of pixels on an OLED display.
- [class AveragePixelLuminance](./averagepixelluminance.md)
  A unit for average pixel luminance measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/gputimemetric)*